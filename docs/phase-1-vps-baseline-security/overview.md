# Phase 1 - VPS Baseline & Security Hardening 🔐

## Objective

Prepare the Netcup VPS as a secure, production-ready Linux server before adding domain DNS, reverse proxying, HTTPS, or public application hosting.

This phase focuses on establishing a clean baseline:

- Secure administrative access
- Reduced public attack surface
- Host-level firewall protection
- SSH brute-force protection
- Automatic security updates
- Docker runtime readiness
- Private administrative access through Tailscale
- Redacted validation evidence

---

## Why This Phase Matters

A public VPS is exposed to the internet immediately after provisioning.

Before hosting applications, the server needs a secure baseline so future services are deployed on top of a controlled foundation instead of a default installation.

This phase answers the basic operational question:

**Is this VPS safe and ready to become a public services host?**

---

## Server Role

| Item | Value |
|---|---|
| Provider | Netcup |
| Hostname | netcup-prod-01 |
| Role | Primary production/public services VPS |
| Operating System | Ubuntu Linux |
| Admin Model | Non-root sudo user |
| Remote Access | SSH key authentication and Tailscale |
| Firewall | UFW |
| Intrusion Protection | Fail2Ban |
| Container Runtime | Docker and Docker Compose |
| Planned Domain | stayz3ro.dev |

---

## Baseline Architecture

    Admin Workstation
          |
          | SSH Key Authentication / Tailscale
          v
    Netcup VPS - netcup-prod-01
          |
          ├── UFW Firewall
          │     ├── SSH
          │     ├── HTTP
          │     └── HTTPS
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

---

## Completed Work

### System Baseline

- Verified operating system version
- Configured hostname
- Fixed local hostname resolution
- Updated system packages
- Installed baseline administration tools
- Configured timezone
- Added swap for additional stability

### User and Access Management

- Created a non-root sudo user
- Confirmed sudo group membership
- Confirmed sudo elevation works
- Configured SSH key-based access
- Disabled root SSH login
- Disabled password-based SSH login

### SSH Hardening

- Confirmed SSH service is active
- Validated SSH configuration syntax
- Reloaded SSH safely
- Tested access from a second terminal session

### Firewall

- Enabled UFW
- Set default incoming policy to deny
- Set default outgoing policy to allow
- Allowed SSH
- Allowed HTTP
- Allowed HTTPS
- Verified active firewall rules

### Intrusion Protection

- Installed Fail2Ban
- Enabled SSH jail
- Configured retry limits
- Verified Fail2Ban status

### Updates

- Enabled unattended security upgrades
- Verified unattended upgrades service

### Container Runtime

- Installed Docker
- Installed Docker Compose
- Verified Docker functionality

### Private Administration

- Installed Tailscale
- Connected VPS to private tailnet
- Verified Tailscale status

### Filesystem Organization

Created a clean service directory layout:

    /opt/stayz3ro
    ├── apps
    ├── backups
    ├── monitoring
    ├── proxy
    └── scripts

---

## Security Posture After Phase 1

| Control | Status |
|---|---:|
| Non-root sudo user | Enabled |
| Root SSH login | Disabled |
| Password SSH login | Disabled |
| SSH key authentication | Enabled |
| UFW firewall | Enabled |
| Fail2Ban SSH jail | Active |
| Unattended upgrades | Enabled |
| Tailscale private access | Connected |
| Direct app port exposure | Not allowed |
| Public database exposure | Not allowed |

---

## Public Exposure Model

Only the following ports are intended to be publicly reachable at this stage:

| Port | Purpose |
|---|---|
| SSH | Administrative access |
| HTTP | Web traffic and certificate validation |
| HTTPS | Secure public services |

Application ports, database ports, admin dashboards, Portainer, and monitoring tools should not be exposed directly to the public internet.

---

## Validation Evidence

Validation screenshots are documented here:

[View Phase 1 Validation Evidence](validation.md)

---

## Step-by-Step Guide

The implementation steps are documented here:

[View Phase 1 Step-by-Step Guide](step-by-step.md)

---

## Next Phase

Next phase:

**Phase 2 - Domain DNS & Public Routing**

This will connect stayz3ro.dev to the VPS and prepare the environment for reverse proxy and HTTPS configuration.
