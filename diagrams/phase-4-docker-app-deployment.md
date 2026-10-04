# Phase 4 - Docker App Deployment 🐳

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![App](https://img.shields.io/badge/app-Umami-success)
![Proxy](https://img.shields.io/badge/proxy-behind%20Caddy-success)
![Domain](https://img.shields.io/badge/domain-analytics.stayz3ro.dev-purple)

## Purpose

This is the target state for Phase 4, not the live deployment. Umami is staged
but has not been deployed. It would sit behind the Phase 3 HTTPS edge at
`analytics.stayz3ro.dev`, with PostgreSQL on an internal-only Docker network.

---

## Request Flow

    Internet Visitor / Blog Reader
         |
         |  https://analytics.stayz3ro.dev
         v
     Public DNS Resolver  ->  Cloudflare zone (analytics A record, DNS only)
                              ->  Netcup VPS public IP
         |
         v
     Netcup VPS - netcup-prod-01
         |
         ├── UFW: only 80/tcp, 443/tcp public (SSH is Tailscale only)
         v
     Caddy container  (published on 80 / 443 / 443-udp)
         |
         ├── :80  ->  redirect to :443
         ├── automatic Let's Encrypt cert (analytics.stayz3ro.dev)
         ├── JSON access log  -> /var/log/caddy/access.log
         |
         ├── status.chrisalorenzo.com -> public Kuma status page only
         └── analytics.stayz3ro.dev ->  reverse_proxy  umami:3000        (Phase 4)
                    |
                    v
             external "web" Docker network
             (backend ports never published to the host)
                    |
                    v
     umami container
         |
         | umami_internal network (internal: true - no route outside,
         |                          NOT attached to "web")
         v
     umami-db container  (PostgreSQL 16, port 5432 internal)
         |     reachable by the umami container only
         |
         └── umami_db_data named volume
             (first stateful data on the VPS -> Phase 6 backup target)

Blog (separate project, Cloudflare Pages)
         |
         | <script src="https://analytics.stayz3ro.dev/script.js"
         |         data-website-id="...">
         v
     analytics events flow to Umami through the same public HTTPS path

---

## Administrative Access

    Admin Workstation
         |
         | Tailscale
         v
     Netcup VPS Tailscale IP
         |
         | SSH; Kuma admin through tailscale serve on port 8443
         | Umami pre-exposure admin claim through an SSH local-forward
         v
     netcup-prod-01

---

## Exposure Model After Phase 4

| Traffic | Exposure |
|---|---|
| HTTP (80) | Public - redirects to HTTPS, serves ACME challenge |
| HTTPS (443) | Public - `status` + `analytics` behind Caddy |
| Kuma admin | Tailnet-only through `tailscale serve`; public admin paths return 404 |
| `analytics.stayz3ro.dev` (Umami) | Public, single authenticated admin, no signup |
| Umami app port (3000) | Internal Docker network only, never published |
| PostgreSQL (5432) | Internal-only network, unreachable from `web` or the host |
| `apps` / `api` subdomains | Not routed yet (staged in Caddyfile) |
| Caddy admin API | Disabled |
| SSH | Tailscale only |

---

## Design Decisions

| Decision | Reason |
|---|---|
| Umami over Shlink / Vikunja | Feeds the active portfolio/blog goals directly; smallest abuse surface for a first stateful service - full comparison in the Phase 4 overview |
| New `analytics` subdomain | Dedicated, long-lived embed-script URL; `apps`/`api` stay staged |
| DNS record in Cloudflare, DNS-only | The registry delegates to Cloudflare, not Porkbun (Phase 3 lesson); Caddy terminates TLS itself |
| Postgres on an `internal: true` network | Database unreachable from the `web` network, Caddy, or the host - exposure control by default |
| No published ports in the app stack | Extends the Phase 3 rule: only Caddy is ever public |
| Admin claimed over SSH tunnel pre-exposure | Umami ships default credentials; Certificate Transparency makes new hostnames discoverable - the Phase 3 race-window lesson, applied by default |
| `umami_db_data` named volume | Analytics data persists across restarts and becomes the first real backup target (Phase 6) |
| Monitor added in Uptime Kuma on day one | The proxy stack's own service now watches the app it fronts |

---

## Next Architecture Layer

**Phase 5 - Monitoring & Alerts**

After deployment, Umami would be a stateful workload to monitor and back up.
The separate public-edge monitoring work in Phase 5 is already live.
