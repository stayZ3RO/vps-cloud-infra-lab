# Current Status

## Project State

The Netcup VPS has been provisioned and secured as the primary public services host for this VPS cloud infrastructure lab.

The project is currently at the end of:

**Phase 1 - VPS Baseline & Security Hardening**

---

## Current Architecture State

    Admin Workstation
          |
          | SSH Key Authentication / Tailscale
          v
    Netcup VPS - netcup-prod-01
          |
          ├── UFW Firewall
          ├── Fail2Ban
          ├── Docker Engine
          ├── Tailscale
          └── /opt/stayz3ro
                ├── apps
                ├── backups
                ├── monitoring
                ├── proxy
                └── scripts

---

## Phase 1 Completion Summary

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
| SSH, HTTP, and HTTPS allowed | ✅ Complete |
| Fail2Ban enabled for SSH | ✅ Complete |
| Unattended upgrades enabled | ✅ Complete |
| Docker installed | ✅ Complete |
| Docker Compose installed | ✅ Complete |
| Tailscale installed and connected | ✅ Complete |
| VPS folder structure created | ✅ Complete |
| Listening ports reviewed | ✅ Complete |

---

## Current VPS Role

| Item | Value |
|---|---|
| Provider | Netcup |
| Hostname | netcup-prod-01 |
| Role | Primary production/public services VPS |
| Operating System | Ubuntu Linux |
| Access Method | SSH key authentication and Tailscale |
| Firewall | UFW |
| Intrusion Protection | Fail2Ban |
| Container Runtime | Docker and Docker Compose |
| Public Exposure | SSH, HTTP, HTTPS only |

---

## Current Security Posture

The VPS has a secure baseline before public applications are deployed.

Current access and exposure model:

- SSH is enabled for administrative access
- Root SSH login is disabled
- Password-based SSH login is disabled
- UFW is enabled with a limited ruleset
- Fail2Ban is active for SSH brute-force protection
- Tailscale is available for private administrative access
- No application ports are directly exposed
- No databases or admin dashboards are publicly exposed

---

## Next Workstream

Next phase:

**Phase 2 - Domain DNS & Public Routing**

Planned tasks:

- Configure DNS for stayz3ro.dev
- Add root domain record
- Add www record
- Plan service subdomains
- Validate DNS resolution
- Document public routing strategy
- Capture redacted DNS screenshots
- Prepare for reverse proxy and HTTPS configuration
