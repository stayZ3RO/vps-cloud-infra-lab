# Phase 1 - VPS Baseline Architecture

## Access and Security Baseline

    Admin Workstation
          |
          | SSH key authentication
          v
    Netcup VPS - netcup-prod-01
          |
          ├── UFW Firewall
          │     ├── SSH allowed
          │     ├── HTTP allowed
          │     └── HTTPS allowed
          |
          ├── Fail2Ban
          │     └── SSH brute-force protection
          |
          ├── Docker Engine
          │     └── Future container workloads
          |
          ├── Tailscale
          │     └── Private administrative access
          |
          └── /opt/stayz3ro
                ├── apps
                ├── backups
                ├── monitoring
                ├── proxy
                └── scripts

## Public Exposure Strategy

Only the following ports are intended to be public:

| Port | Purpose |
|---|---|
| 22/tcp | SSH administration |
| 80/tcp | HTTP and certificate validation |
| 443/tcp | HTTPS public services |

Admin dashboards, databases, Portainer, and monitoring tools should not be directly exposed to the public internet.
