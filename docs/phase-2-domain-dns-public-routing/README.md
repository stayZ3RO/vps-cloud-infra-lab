# Phase 2 - Domain DNS & Public Routing 🌐

![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Domain](https://img.shields.io/badge/domain-stayz3ro.dev-blue)
![DNS](https://img.shields.io/badge/dns-Porkbun-orange)
![VPS](https://img.shields.io/badge/vps-Netcup-purple)
![SSH](https://img.shields.io/badge/ssh-Tailscale%20Only-success)

## Phase Summary

Phase 2 connected the `stayz3ro.dev` domain to the Netcup VPS and established the DNS foundation for future public services.

This phase did not deploy applications yet. It focused on DNS records, public resolution, planned subdomains, and a stronger administrative access model where SSH is reachable only through Tailscale.

---

## What This Phase Demonstrates

| Area | Demonstrated Skill |
|---|---|
| Domain management | Porkbun DNS record configuration |
| Public DNS routing | Root domain and subdomain resolution |
| DNS validation | Local and public resolver checks |
| Security hardening | Public SSH blocked |
| Private administration | SSH allowed through Tailscale |
| Documentation | Screenshots, validation, and redaction |

---

## DNS Records Configured

| Type | Host | Purpose |
|---|---|---|
| A | `@` | Root domain pointing to Netcup VPS |
| CNAME | `www` | Web alias for root domain |
| A | `apps` | Future public application entry point |
| A | `status` | Future status page |
| A | `api` | Future API services |

---

## Access Model After Phase 2

| Access Type | Result |
|---|---|
| SSH to public VPS IP | Blocked |
| SSH to Tailscale IP | Allowed |
| HTTP public access | Allowed for future reverse proxy |
| HTTPS public access | Allowed for future reverse proxy |
| Direct app ports | Blocked |
| Admin dashboards | Not publicly exposed |

---

## Documentation

| Page | Description |
|---|---|
| [Overview](overview.md) | Case-study overview |
| [Step-by-Step Guide](step-by-step.md) | DNS and SSH access implementation flow |
| [Validation Evidence](validation.md) | Screenshots and proof of completion |

---

## Screenshot Evidence

Redacted validation screenshots are stored here:

[View Screenshot Evidence](../../screenshots/phase-2-domain-dns-public-routing/)

---

## Next Phase

Next: **Phase 3 - Reverse Proxy & HTTPS**

That phase will deploy the reverse proxy and configure HTTPS routing for the domain and subdomains.
