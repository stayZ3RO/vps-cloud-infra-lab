# VPS Cloud Infrastructure Lab 🚀

### Building a Production-Style VPS Cloud Lab with Linux, Docker, DNS, HTTPS, Monitoring, Backups, and Secure Access

---

## About This Project

This project documents the process of building a production-style VPS cloud infrastructure lab using public Linux servers, Docker, domain DNS, reverse proxying, HTTPS, monitoring, backups, and secure administrative access.

The goal is to build practical cloud and infrastructure experience by managing real VPS environments from the ground up.

This lab is designed to demonstrate:

- Linux server administration
- VPS security hardening
- SSH access control
- Firewall configuration
- Docker-based application hosting
- Domain DNS management
- Reverse proxy and HTTPS routing
- Monitoring and alerting
- Backup and disaster recovery planning
- Staging and production separation
- Infrastructure documentation

---

## Architecture Overview

Current baseline:

    Admin Workstation
          |
          | SSH key authentication / Tailscale
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

Planned cloud architecture:

    Internet
       |
       v
    stayz3ro.dev DNS
       |
       v
    Netcup VPS - Production/Public Services
       |
       ├── Reverse Proxy
       ├── HTTPS
       ├── Public Docker Apps
       └── Private Admin Access via Tailscale

    RackNerd VPS - Planned
       |
       ├── Staging
       ├── Monitoring
       ├── Backups
       └── Secondary Services

---

## Current State

- Netcup VPS provisioned
- Hostname configured as `netcup-prod-01`
- Non-root sudo user configured
- SSH hardened
- Root SSH login disabled
- Password SSH login disabled
- UFW firewall enabled
- Only SSH, HTTP, and HTTPS allowed
- Fail2Ban enabled for SSH protection
- Unattended upgrades enabled
- Docker and Docker Compose installed
- Tailscale installed for private administrative access
- `/opt/stayz3ro` folder structure created
- Listening ports reviewed and documented

---

## Current Progress

- ✅ Phase 1 - VPS Baseline & Security Hardening
- ⏳ Phase 2 - Domain DNS & Public Routing
- ⏳ Phase 3 - Reverse Proxy & HTTPS
- ⏳ Phase 4 - Docker App Deployment
- ⏳ Phase 5 - Monitoring & Alerts
- ⏳ Phase 6 - Backups & Disaster Recovery
- ⏳ Phase 7 - Secondary VPS / Staging
- ⏳ Phase 8 - AI Agent / Homelab Ops Bot

---

## Documentation

### Phase 1 - VPS Baseline & Security Hardening

- [Overview](docs/phase-1-vps-baseline-security/overview.md)
- [Step-by-Step Guide](docs/phase-1-vps-baseline-security/step-by-step.md)
- [Validation Evidence](docs/phase-1-vps-baseline-security/validation.md)
- [Architecture Diagram](diagrams/phase-1-vps-baseline-security.md)
- [Screenshots](screenshots/phase-1-vps-baseline-security/)

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

- Ubuntu Linux
- SSH
- UFW
- Fail2Ban
- Unattended Upgrades
- Docker
- Docker Compose
- Tailscale
- Netcup VPS
- RackNerd VPS planned
- Porkbun domain planned
- Reverse proxy planned
- HTTPS planned

---

## What This Project Demonstrates

- Linux server administration
- Secure VPS baseline configuration
- SSH hardening and access control
- Firewall policy management
- Brute-force protection
- Container runtime setup
- Private administrative access with Tailscale
- Infrastructure documentation
- Cloud hosting fundamentals
- Portfolio-ready technical validation

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

Admin dashboards, databases, and internal services should not be directly exposed to the public internet.

---

## Current Status

For the latest status, see:

- [Current Status](CURRENT-STATUS.md)

---

## Roadmap

For planned phases, see:

- [Roadmap](ROADMAP.md)

---

## Lessons Learned

For troubleshooting notes and design decisions, see:

- [Lessons Learned](LESSONS-LEARNED.md)
