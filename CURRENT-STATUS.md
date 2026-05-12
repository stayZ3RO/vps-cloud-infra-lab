# Current Status

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Current Phase](https://img.shields.io/badge/current_phase-Phase%203%20Planned-blue)
![Security](https://img.shields.io/badge/ssh-Tailscale%20Only-success)

## Project State

The Netcup VPS has been provisioned, secured, connected to `stayz3ro.dev`, and validated for public DNS routing.

The project is currently at the end of:

**Phase 2 - Domain DNS & Public Routing**

---

## Current Architecture State

    Internet
       |
       v
    Porkbun DNS - stayz3ro.dev
       |
       v
    Netcup VPS - netcup-prod-01
       |
       ├── Public HTTP - 80/tcp
       ├── Public HTTPS - 443/tcp
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

---

## Current VPS Role

| Item | Value |
|---|---|
| Provider | Netcup |
| Hostname | netcup-prod-01 |
| Role | Primary production/public services VPS |
| Operating System | Ubuntu Linux |
| Domain | stayz3ro.dev |
| DNS Provider | Porkbun |
| Access Method | SSH over Tailscale |
| Firewall | UFW |
| Intrusion Protection | Fail2Ban |
| Container Runtime | Docker and Docker Compose |
| Public Exposure | HTTP and HTTPS only |

---

## Current Security Posture

The VPS now uses a stronger management-plane design.

Current access and exposure model:

- SSH is blocked on the public VPS IP
- SSH is allowed through Tailscale only
- HTTP is open for future reverse proxy/certificate traffic
- HTTPS is open for future reverse proxy traffic
- Direct application ports are not exposed
- Databases are not exposed
- Admin dashboards are not exposed publicly

---

## Next Workstream

Next phase:

**Phase 3 - Reverse Proxy & HTTPS**

Planned tasks:

- Choose reverse proxy platform
- Deploy reverse proxy stack
- Configure HTTP to HTTPS routing
- Issue TLS certificates
- Route root domain and subdomains
- Validate HTTPS externally
- Keep application ports private behind the proxy
