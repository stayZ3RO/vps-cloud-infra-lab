# VPS Cloud Infrastructure Lab 🚀

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Current Phase](https://img.shields.io/badge/current_phase-VPS%20Baseline%20Security-blue)
![Platform](https://img.shields.io/badge/platform-Netcup%20VPS-orange)
![Docker](https://img.shields.io/badge/container_runtime-Docker-blue)
![Security](https://img.shields.io/badge/security-hardened-success)
![Access](https://img.shields.io/badge/private_access-Tailscale-purple)

## Quick Links

| Area | Link |
|---|---|
| Current Status | [CURRENT-STATUS.md](CURRENT-STATUS.md) |
| Roadmap | [ROADMAP.md](ROADMAP.md) |
| Lessons Learned | [LESSONS-LEARNED.md](LESSONS-LEARNED.md) |
| Phase 1 Documentation | [Phase 1 - VPS Baseline & Security Hardening](docs/phase-1-vps-baseline-security/) |
| Validation Evidence | [Phase 1 Validation](docs/phase-1-vps-baseline-security/validation.md) |
| Architecture Diagrams | [diagrams/](diagrams/) |
| Config Examples | [configs/](configs/) |
| Screenshots | [screenshots/](screenshots/) |

---

## Building a Production-Style VPS Cloud Lab

This repository documents my process of building a real VPS-based cloud infrastructure lab using Linux, Docker, domain DNS, reverse proxying, HTTPS, monitoring, backups, and secure remote administration.

The goal is to move beyond local-only homelab infrastructure and build practical experience with public cloud-style hosting, Linux server hardening, DNS routing, containerized deployments, and production-minded documentation.

This project is part of my broader infrastructure learning path toward cloud, network, and systems engineering roles.

---

## Why I Built This

After building out my home network infrastructure lab, I wanted to extend the same hands-on approach into public-facing cloud infrastructure.

This VPS lab gives me a place to practice:

- Managing real Linux servers exposed to the public internet
- Hardening SSH and host-level access
- Using firewall rules and brute-force protection
- Hosting containerized services with Docker
- Connecting a custom domain to public infrastructure
- Deploying services behind a reverse proxy with HTTPS
- Building monitoring, backups, and staging workflows
- Documenting infrastructure decisions like an engineer

---

## Current Architecture

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

## Target Architecture

    Internet
       |
       v
    stayz3ro.dev DNS
       |
       v
    Netcup VPS - Production/Public Services
       |
       ├── Reverse Proxy
       ├── HTTPS Certificates
       ├── Public Docker Apps
       └── Private Admin Access via Tailscale

    RackNerd VPS - Planned Secondary Node
       |
       ├── Staging Services
       ├── Monitoring
       ├── Backups
       └── Secondary Infrastructure

---

## Current Progress

| Phase | Status | Focus |
|---|---:|---|
| Phase 1 - VPS Baseline & Security Hardening | ✅ Complete | Secure Linux baseline |
| Phase 2 - Domain DNS & Public Routing | ✅ Complete | stayz3ro.dev DNS records and Tailscale-only SSH |
| Phase 3 - Reverse Proxy & HTTPS | ⏳ Planned | Public routing and TLS |
| Phase 4 - Docker App Deployment | ⏳ Planned | First public containerized services |
| Phase 5 - Monitoring & Alerts | ⏳ Planned | Uptime and service visibility |
| Phase 6 - Backups & Disaster Recovery | ⏳ Planned | Recovery strategy |
| Phase 7 - Secondary VPS / Staging | ⏳ Planned | RackNerd staging and backup node |
| Phase 8 - AI Agent / Homelab Ops Bot | ⏳ Planned | Infrastructure assistant experiments |

---

## Phase 1 Highlights

Phase 1 focused on preparing the Netcup VPS as a secure baseline before deploying any public services.

Completed:

- Configured hostname: netcup-prod-01
- Created a non-root sudo user
- Hardened SSH access
- Disabled root SSH login
- Disabled password-based SSH login
- Enabled UFW firewall
- Allowed only SSH, HTTP, and HTTPS
- Enabled Fail2Ban for SSH protection
- Enabled unattended security updates
- Installed Docker and Docker Compose
- Installed Tailscale for private administrative access
- Created a clean /opt/stayz3ro folder structure
- Reviewed listening ports before public service deployment

---

## Validation Preview

| Area | Evidence |
|---|---|
| SSH service | Confirmed active and running |
| SSH config | Validated successfully |
| Firewall | UFW enabled with limited public exposure |
| Intrusion protection | Fail2Ban active for SSH |
| Container runtime | Docker and Docker Compose installed |
| Private access | Tailscale connected |
| Filesystem layout | /opt/stayz3ro service folders created |

Full validation screenshots are available here:

[View Phase 1 Validation Evidence](docs/phase-1-vps-baseline-security/validation.md)

---

## Documentation

### Phase 1 - VPS Baseline & Security Hardening

| Document | Description |
|---|---|
| [Overview](docs/phase-1-vps-baseline-security/overview.md) | What was built and why |
| [Step-by-Step Guide](docs/phase-1-vps-baseline-security/step-by-step.md) | Commands and setup process |
| [Validation Evidence](docs/phase-1-vps-baseline-security/validation.md) | Screenshots and proof |
| [Architecture Diagram](diagrams/phase-1-vps-baseline-security.md) | Phase 1 infrastructure layout |
| [Phase 2 Documentation](docs/phase-2-domain-dns-public-routing/) | Domain DNS and public routing validation |

### Project-Level Docs

| Document | Description |
|---|---|
| [Current Status](CURRENT-STATUS.md) | Current project state |
| [Roadmap](ROADMAP.md) | Planned phases |
| [Lessons Learned](LESSONS-LEARNED.md) | Troubleshooting notes and design decisions |
| [Changelog](CHANGELOG.md) | Project update history |

---

## Repository Structure

    configs/
      Sanitized service and security configuration examples

    diagrams/
      Architecture diagrams and infrastructure flow documentation

    docs/
      Phase-based documentation

    screenshots/
      Redacted validation screenshots and implementation evidence

    scripts/
      Future maintenance and automation scripts

---

## Core Tools and Services

| Category | Tools |
|---|---|
| VPS Provider | Netcup |
| Planned Secondary VPS | RackNerd |
| OS | Ubuntu Linux |
| Access | SSH, Tailscale |
| Firewall | UFW |
| Intrusion Protection | Fail2Ban |
| Updates | Unattended Upgrades |
| Containers | Docker, Docker Compose |
| Domain | stayz3ro.dev planned |
| Reverse Proxy | Planned |
| HTTPS | Planned |

---

## What This Project Demonstrates

This project demonstrates practical infrastructure skills across:

- Linux server administration
- VPS security hardening
- SSH access control
- Firewall policy management
- Brute-force protection
- Secure remote administration
- Docker runtime setup
- Public DNS planning
- Infrastructure documentation
- Cloud hosting fundamentals
- Production-minded validation

---

## Security Notes

This repository intentionally excludes:

- Public IP addresses
- Private keys
- API keys
- Provider credentials
- Tailscale authentication data
- Billing information
- Unredacted screenshots
- Production secrets

Admin dashboards, databases, Portainer, and monitoring tools should not be directly exposed to the public internet.

---

## Next Phase

Next up: Phase 2 - Domain DNS & Public Routing.

This phase will connect stayz3ro.dev to the VPS, configure DNS records, validate public resolution, and prepare the environment for reverse proxy and HTTPS deployment.
