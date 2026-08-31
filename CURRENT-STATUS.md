# Current Status

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Current Phase](https://img.shields.io/badge/current_phase-Phase%203%20Complete-brightgreen)
![Security](https://img.shields.io/badge/ssh-Tailscale%20Only-success)

## Project State

The Netcup VPS has been provisioned, secured, connected to `stayz3ro.dev`, and is now serving a public HTTPS service (`status.stayz3ro.dev`, Uptime Kuma behind Caddy).

The project is currently at the end of:

**Phase 3 - Reverse Proxy & HTTPS**

---

## Current Architecture State

    Internet
       |
       v
    Cloudflare DNS - stayz3ro.dev
    (registrar: Porkbun; DNS hosting: Cloudflare. The domain's
     nameservers point to Cloudflare, not Porkbun's own DNS panel)
       |
       v
    Netcup VPS - netcup-prod-01
       |
       ├── Caddy (reverse proxy, automatic HTTPS) - 80/443 tcp
       │      └── status.stayz3ro.dev -> Uptime Kuma (internal only)
       └── Private SSH - tailscale0 only

    Admin Workstation
       |
       v
    Tailscale
       |
       v
    SSH to Netcup VPS

---

## Phase Completion Summary

| Area | Status |
|---|---:|
| VPS provisioned | ✅ Complete |
| Hostname configured | ✅ Complete |
| Non-root sudo user configured | ✅ Complete |
| SSH service validated | ✅ Complete |
| SSH configuration validated | ✅ Complete |
| Root SSH login disabled | ✅ Complete |
| Password SSH login disabled | ✅ Complete |
| UFW firewall enabled | ✅ Complete |
| Fail2Ban enabled for SSH | ✅ Complete |
| Unattended upgrades enabled | ✅ Complete |
| Docker installed | ✅ Complete |
| Docker Compose installed | ✅ Complete |
| Tailscale installed and connected | ✅ Complete |
| Porkbun DNS configured | ✅ Complete |
| Root domain record configured | ✅ Complete |
| `www` record configured | ✅ Complete |
| `apps` record configured | ✅ Complete |
| `status` record configured | ✅ Complete |
| `api` record configured | ✅ Complete |
| Local DNS validation completed | ✅ Complete |
| Public resolver validation completed | ✅ Complete |
| Public SSH blocked | ✅ Complete |
| SSH over Tailscale validated | ✅ Complete |
| Caddy reverse proxy deployed | ✅ Complete |
| Uptime Kuma deployed (private, proxied only) | ✅ Complete |
| Let's Encrypt certificate issued for `status.stayz3ro.dev` | ✅ Complete |
| HTTPS validated externally | ✅ Complete |
| Security headers validated | ✅ Complete |
| Backend ports confirmed not public | ✅ Complete |
| Uptime Kuma admin account secured pre-exposure | ✅ Complete |
| Redacted Phase 3 evidence captured | ✅ Complete |

---

## Current VPS Role

| Item | Value |
|---|---|
| Provider | Netcup |
| Hostname | netcup-prod-01 |
| Role | Primary production/public services VPS |
| Operating System | Ubuntu Linux |
| Domain | stayz3ro.dev |
| Domain Registrar | Porkbun |
| DNS Hosting (actual, authoritative) | Cloudflare. Porkbun's own DNS panel is not consulted by the live domain, see Lessons Learned |
| Access Method | SSH over Tailscale |
| Firewall | UFW |
| Intrusion Protection | Fail2Ban |
| Container Runtime | Docker and Docker Compose |
| Public Exposure | HTTPS via Caddy (`status.stayz3ro.dev` -> Uptime Kuma); apex/`www` served separately by Cloudflare Pages, not this VPS |

---

## Current Security Posture

The VPS now uses a stronger management-plane design.

Current access and exposure model:

- SSH is blocked on the public VPS IP
- SSH is allowed through Tailscale only
- HTTP is open, redirects to HTTPS via Caddy
- HTTPS is open, serves `status.stayz3ro.dev` (Uptime Kuma) via Caddy
- Direct application ports (`3000`, `3001`) are not exposed, confirmed by
  external probe
- Databases are not exposed
- Admin dashboards are not exposed publicly; Uptime Kuma's admin account
  was created over a private SSH tunnel before the certificate made the
  hostname publicly discoverable

---

## Next Workstream

Next phase:

**Phase 4 - Docker App Deployment**

Planned tasks:

- Deploy the first real public Dockerized app behind Caddy
- Route it through the reverse proxy
- Validate external access
- Document environment variables and `.env.example`
- Capture deployment screenshots
