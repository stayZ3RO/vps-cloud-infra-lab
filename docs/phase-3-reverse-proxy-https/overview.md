# Phase 3 - Reverse Proxy & HTTPS 🔒

---

## Quick Navigation

| Page | Link |
|---|---|
| Phase 3 Home | [README](README.md) |
| Overview | [overview.md](overview.md) |
| Step-by-Step Guide | [step-by-step.md](step-by-step.md) |
| Validation Evidence | [validation.md](validation.md) |
| Architecture Diagram | [Diagram](../../diagrams/phase-3-reverse-proxy-https.md) |

---

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![Proxy](https://img.shields.io/badge/proxy-Caddy-blue)
![TLS](https://img.shields.io/badge/tls-Let's%20Encrypt-success)
![Domain](https://img.shields.io/badge/domain-stayz3ro.dev-purple)

## Overview

Phase 2 pointed `stayz3ro.dev` at the VPS but nothing answered on ports 80 or
443. Phase 3 adds the HTTPS edge: a reverse proxy that terminates TLS, serves
public content, and becomes the single controlled entry point for every future
service.

The proxy is deployed as a Docker Compose stack and configured entirely from
version-controlled files.

---

## Objective

Stand up a public HTTPS entry point that:

- Serves `status.stayz3ro.dev` over TLS
- Obtains and renews certificates automatically
- Redirects all HTTP to HTTPS
- Reverse-proxies a real service (Uptime Kuma), so HTTPS is externally verifiable now
- Is pre-wired to route additional backend services **without** exposing their ports
- Produces structured access logs

Deploying applications is still out of scope - that is Phase 4. Phase 3 builds
the door they will sit behind.

---

## Why This Phase Matters

Without a reverse proxy, every service would need its own public port, its own
certificate handling, and its own exposure decisions. That does not scale and
it widens the attack surface with each app.

A single TLS-terminating proxy answers one question cleanly:

> How does public traffic reach a service safely, and how does everything
> else stay private?

---

## Reverse Proxy Selection

| Option | Assessment |
|---|---|
| **Caddy** | **Chosen.** One declarative `Caddyfile`, automatic Let's Encrypt issuance and renewal, HTTP/3, no separate admin port, no database. Minimal moving parts on a public node. |
| Nginx Proxy Manager | GUI-driven, but adds a database and an admin dashboard port. That dashboard would then need Tailscale-only lockdown, which cuts against the management-plane model from Phase 2. The database stores proxy configuration, not logs. |
| Traefik | Strong Docker-native option and a common Kubernetes ingress controller. Heavier configuration model than needed for a single-service start. A sensible later exercise when the Kubernetes track begins. |
| Plain Nginx | Full control, but manual certificate automation (certbot) and more config for the same result. |

Access logging - the "matches corporate practice" requirement - is a
configuration choice, not a reason to run a heavier proxy. Caddy is configured
here to write structured JSON access logs from the start.

---

## What Was Built

### TLS-Terminating Edge

Caddy runs as a single container publishing only:

| Port | Purpose |
|---|---|
| 80/tcp | HTTP - ACME challenge and redirect to HTTPS |
| 443/tcp | HTTPS |
| 443/udp | HTTP/3 |

Certificates for `status.stayz3ro.dev` are issued automatically via the
Let's Encrypt HTTP-01 challenge and renewed by Caddy before expiry. The ACME
account and issued certificates persist in the `caddy_data` named volume so
restarts do not trigger re-issuance.

### Public Content

| Host | Behaviour |
|---|---|
| `status.stayz3ro.dev` | Reverse-proxied to the `uptime-kuma` container on the internal `web` network |

Uptime Kuma is the first real service behind the proxy. The public surface
is one monitored, actively-updated service, not a static placeholder page.

### Response Hardening

Every response carries:

- `Strict-Transport-Security` (1 year, includeSubDomains)
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Server` header removed

### Staged Backend Routes

`apps.stayz3ro.dev` and `api.stayz3ro.dev` are present in the `Caddyfile` as
commented `reverse_proxy` blocks for future services. Once a matching
container joins the internal `web` Docker network, the block is uncommented.
Backend ports are never published to the host.

### Access Logging

Caddy writes JSON access logs to `/var/log/caddy/access.log` with size-based
rotation. This is the input for uptime and traffic visibility in Phase 5.

---

## Exposure Model After Phase 3

| Surface | Exposure |
|---|---|
| HTTP / HTTPS | Public |
| `status.stayz3ro.dev` (Uptime Kuma) | Public |
| `stayz3ro.dev` apex / `www` | Not served by this VPS, Cloudflare Pages (blog) |
| `apps` / `api` | Not routed yet |
| Backend application ports | Internal Docker network only |
| Caddy admin API | Disabled |
| SSH | Tailscale only (unchanged) |
| Databases | Not present yet; will stay on internal networks |

---

## Validation Evidence

Phase 3 is validated with:

- External `curl -I` showing HTTP 308 -> HTTPS and a valid certificate chain
- Browser padlock on `https://status.stayz3ro.dev`, loading Uptime Kuma
- Security headers in the response
- `docker compose logs` showing certificate issuance
- The JSON access log receiving entries
- A port scan / `curl` confirming no backend ports answer publicly

See [validation.md](validation.md).

---

## Related Documentation

| Document | Purpose |
|---|---|
| [Step-by-Step Guide](step-by-step.md) | Commands and implementation flow |
| [Validation Evidence](validation.md) | Screenshots and verification |
| [Architecture Diagram](../../diagrams/phase-3-reverse-proxy-https.md) | HTTPS edge and request flow |
| [Caddy Config](../../configs/caddy/) | Caddyfile, compose stack, env template |

---

## Key Takeaway

Phase 3 does not add every future service, but it does put one real,
monitored service in front of the public: Uptime Kuma at
`status.stayz3ro.dev`.

It establishes the rule every later phase depends on:

> Public traffic enters through exactly one hardened, TLS-terminating proxy.
> Everything else stays private.
