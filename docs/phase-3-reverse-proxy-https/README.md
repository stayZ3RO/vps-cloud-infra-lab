# Phase 3 - Reverse Proxy & HTTPS 🔒

![Status](https://img.shields.io/badge/status-complete-success)
![Proxy](https://img.shields.io/badge/proxy-Caddy-blue)
![TLS](https://img.shields.io/badge/tls-Let's%20Encrypt-success)
![Scope](https://img.shields.io/badge/scope-HTTPS%20edge-purple)

## Phase Summary

Phase 3 puts a reverse proxy in front of the Netcup VPS so a real public
service, `status.stayz3ro.dev` (Uptime Kuma), reaches the internet over
HTTPS, while backend application ports stay private. The `stayz3ro.dev`
apex + `www` are served elsewhere (Cloudflare Pages, the blog). This VPS
never serves them.

Caddy terminates TLS with automatically issued and renewed Let's Encrypt
certificates, reverse-proxies `status.stayz3ro.dev` to Uptime Kuma, and is
pre-staged to route `apps` and `api` subdomains later without publishing any
backend ports.

---

## What This Phase Demonstrates

| Area | Demonstrated Skill |
|---|---|
| Reverse proxy design | Single TLS-terminating edge, host-based routing |
| HTTPS / PKI | Automatic ACME issuance and renewal, HSTS, security headers |
| Container operations | Docker Compose stack, named volumes, internal networks |
| Exposure control | Only 80/443 public; app ports on an internal Docker network |
| Observability | Structured JSON access logging |
| Tooling judgement | Documented Caddy vs NPM vs Traefik tradeoff |

---

## Documentation

| Page | Description |
|---|---|
| [Overview](overview.md) | Case-study view of what was built and why |
| [Step-by-Step Guide](step-by-step.md) | Implementation runbook and commands |
| [Validation Evidence](validation.md) | Screenshots and proof of completion |
| [Architecture Diagram](../../diagrams/phase-3-reverse-proxy-https.md) | HTTPS edge and request flow |
| [Caddy Config](../../configs/caddy/) | Caddyfile, compose stack, env template |

---

## Completion Criteria

| Requirement | Status |
|---|---:|
| Reverse proxy platform chosen and justified | ✅ Complete |
| Caddy stack committed (Caddyfile, compose, env template) | ✅ Complete |
| Stack deployed on the VPS (2026-08-30) | ✅ Complete |
| Valid TLS certificate issued for `status.stayz3ro.dev` | ✅ Complete |
| HTTP redirects to HTTPS (308) | ✅ Complete |
| `www` -> apex redirect | ➖ Not applicable - apex/`www` moved to Cloudflare Pages before deploy; this VPS never serves them |
| External HTTPS validated (browser + `curl`) | ✅ Complete |
| Security headers present | ✅ Complete |
| JSON access log confirmed writing | ✅ Complete |
| Backend ports confirmed not publicly reachable | ✅ Complete |
| Redacted screenshots captured | ✅ Complete |

---

## Evidence

Redacted validation screenshots (captured 2026-08-30, including the
Cloudflare-zone bonus evidence for the DNS zone mismatch):

[Phase 3 Screenshot Evidence](../../screenshots/phase-3-reverse-proxy-https/)

---

## Next Phase

Next: **Phase 4 - Docker App Deployment**

That phase deploys the first backend container and enables one staged
`reverse_proxy` route.
