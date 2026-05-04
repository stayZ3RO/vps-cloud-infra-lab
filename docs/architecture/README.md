# Architecture Notes 🧱

## Target High-Level Architecture

    Internet
       |
       v
    stayz3ro.dev DNS
       |
       v
    Netcup VPS - netcup-prod-01
       |
       ├── Reverse Proxy
       ├── Public Docker Apps
       ├── HTTPS Certificates
       └── Tailscale Private Admin Access

    RackNerd VPS - planned
       |
       ├── Staging Apps
       ├── Monitoring
       ├── Backups
       └── Secondary Services

---

## VPS Role Separation

| VPS | Role |
|---|---|
| Netcup VPS | Primary public production host |
| RackNerd VPS | Staging, monitoring, backups, and secondary infrastructure |

---

## Planned Public Services

| Service Type | Exposure Method |
|---|---|
| Public website | HTTPS through reverse proxy |
| Public APIs | HTTPS through reverse proxy |
| Admin dashboards | Tailscale/private access only |
| Databases | Internal Docker network only |
| Portainer | Tailscale/private access only |
| Monitoring dashboards | Private or restricted access |

---

## Network Exposure Strategy

Only these ports should be public by default:

| Port | Purpose |
|---|---|
| 22/tcp | SSH administration |
| 80/tcp | HTTP / certificate validation |
| 443/tcp | HTTPS public services |

Application ports such as `3000`, `5000`, `8000`, `9000`, and database ports should not be exposed directly to the public internet.

---

## Current Phase

The project is currently at:

**Phase 1 - VPS Baseline & Security Hardening**

The VPS is secured and ready for domain/DNS integration.
