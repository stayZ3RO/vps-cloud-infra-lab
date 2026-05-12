# VPS Cloud Infrastructure Lab 🚀

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Current Phase](https://img.shields.io/badge/current_phase-Reverse%20Proxy%20%26%20HTTPS-blue)
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
| Changelog | [CHANGELOG.md](CHANGELOG.md) |
| Documentation Hub | [docs/](docs/) |
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
          | SSH over Tailscale
          v
    Netcup VPS - netcup-prod-01
          |
          ├── UFW Firewall
          │     ├── HTTP public
          │     ├── HTTPS public
          │     └── SSH over tailscale0 only
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

## Completed Work

### Phase 1 - VPS Baseline & Security Hardening

Phase 1 prepared the Netcup VPS as a secure Linux baseline before deploying public services.

Highlights:

- Configured hostname: `netcup-prod-01`
- Created a non-root sudo user
- Hardened SSH access
- Disabled root SSH login
- Disabled password-based SSH login
- Enabled UFW firewall
- Enabled Fail2Ban
- Enabled unattended security updates
- Installed Docker and Docker Compose
- Installed Tailscale
- Created `/opt/stayz3ro` folder structure
- Reviewed listening ports

### Phase 2 - Domain DNS & Public Routing

Phase 2 connected `stayz3ro.dev` to the VPS and improved the management-plane security model.

Highlights:

- Removed Porkbun parking records
- Added root domain DNS record
- Added `www`, `apps`, `status`, and `api` records
- Validated local DNS resolution
- Validated public DNS resolvers
- Confirmed SSH over Tailscale
- Removed public SSH access
- Confirmed UFW allows SSH only over `tailscale0`
- Captured redacted validation screenshots

---

## Documentation

### Phase 1 - VPS Baseline & Security Hardening

| Document | Description |
|---|---|
| [Phase Home](docs/phase-1-vps-baseline-security/) | Phase 1 landing page |
| [Overview](docs/phase-1-vps-baseline-security/overview.md) | What was built and why |
| [Step-by-Step Guide](docs/phase-1-vps-baseline-security/step-by-step.md) | Commands and setup process |
| [Validation Evidence](docs/phase-1-vps-baseline-security/validation.md) | Screenshots and proof |
| [Architecture Diagram](diagrams/phase-1-vps-baseline-security.md) | Phase 1 infrastructure layout |

### Phase 2 - Domain DNS & Public Routing

| Document | Description |
|---|---|
| [Phase Home](docs/phase-2-domain-dns-public-routing/) | Phase 2 landing page |
| [Overview](docs/phase-2-domain-dns-public-routing/overview.md) | DNS and access model overview |
| [Step-by-Step Guide](docs/phase-2-domain-dns-public-routing/step-by-step.md) | DNS and SSH access implementation flow |
| [Validation Evidence](docs/phase-2-domain-dns-public-routing/validation.md) | DNS and Tailscale-only SSH proof |
| [Architecture Diagram](diagrams/phase-2-domain-dns-public-routing.md) | Public DNS and private admin access model |

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
| Access | SSH over Tailscale |
| Firewall | UFW |
| Intrusion Protection | Fail2Ban |
| Updates | Unattended Upgrades |
| Containers | Docker, Docker Compose |
| Domain | stayz3ro.dev |
| DNS Provider | Porkbun |
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
- Public DNS routing
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

Next up: **Phase 3 - Reverse Proxy & HTTPS**

This phase will deploy a reverse proxy, configure HTTPS certificates, and route public services through `stayz3ro.dev` and planned subdomains.

---

## Related Infrastructure Labs

This repository is part of a broader infrastructure lab portfolio.

| Repository | Focus | Relationship |
|---|---|---|
| [Home Network Infrastructure Lab](https://github.com/stayZ3RO/home-network-infrastructure-HA-DNS) | HA DNS, Pi-hole, Unbound, monitoring, Tailscale, Proxmox, RustDesk | Demonstrates the local infrastructure foundation and HA service layer |
| [Home Network Managed Infrastructure Lab](https://github.com/stayZ3RO/home-network-managed-infrastructure-lab) | Managed router, switching, VLANs, firewall policy, network segmentation | Demonstrates managed networking and segmentation architecture |
| [VPS Cloud Infrastructure Lab](https://github.com/stayZ3RO/vps-cloud-infra-lab) | Linux VPS hardening, Docker, DNS, HTTPS, monitoring, backups, secure access | Demonstrates cloud-hosted infrastructure and service operations |
