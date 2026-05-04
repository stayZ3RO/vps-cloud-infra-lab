# Phase 1 - VPS Baseline & Security Hardening 🔐

![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Provider](https://img.shields.io/badge/provider-Netcup-orange)
![Scope](https://img.shields.io/badge/scope-VPS%20Security%20Baseline-blue)
![Access](https://img.shields.io/badge/access-SSH%20%2B%20Tailscale-purple)

## Phase Summary

Phase 1 established the secure baseline for the Netcup VPS before connecting a domain, deploying a reverse proxy, or hosting public applications.

The goal was to turn a fresh public VPS into a controlled Linux server with hardened access, limited public exposure, brute-force protection, Docker readiness, private administrative access, and validation evidence.

---

## What This Phase Demonstrates

| Area | Demonstrated Skill |
|---|---|
| Linux administration | Hostname, packages, users, services |
| SSH hardening | Key-based access, root login disabled, password login disabled |
| Firewalling | UFW default deny with minimal public exposure |
| Security operations | Fail2Ban, unattended upgrades, listening port review |
| Container readiness | Docker and Docker Compose installed |
| Private access | Tailscale connected for admin paths |
| Documentation | Screenshots, validation, diagrams, and sanitized configs |

---

## Documentation

| Page | Description |
|---|---|
| [Overview](overview.md) | Case-study view of what was built and why |
| [Step-by-Step Guide](step-by-step.md) | Implementation flow and commands |
| [Validation Evidence](validation.md) | Screenshots and proof of completion |
| [Architecture Diagram](../../diagrams/phase-1-vps-baseline-security.md) | Security baseline diagram |

---

## Validation Highlights

| Control | Status |
|---|---:|
| Non-root sudo user | ✅ Complete |
| SSH service active | ✅ Complete |
| SSH config validated | ✅ Complete |
| Root SSH login disabled | ✅ Complete |
| Password SSH login disabled | ✅ Complete |
| UFW enabled | ✅ Complete |
| Fail2Ban active | ✅ Complete |
| Unattended upgrades enabled | ✅ Complete |
| Docker installed | ✅ Complete |
| Tailscale connected | ✅ Complete |
| Listening ports reviewed | ✅ Complete |

---

## Evidence

Redacted validation screenshots are stored here:

[View Screenshot Evidence](../../screenshots/phase-1-vps-baseline-security/)

---

## Next Phase

Next: **Phase 2 - Domain DNS & Public Routing**

That phase will connect `stayz3ro.dev` to the VPS and prepare the environment for reverse proxy and HTTPS routing.
