# VPS Cloud Infrastructure Lab 🚀

This repository documents my VPS-based cloud infrastructure lab built around public Linux servers, domain DNS, Docker, reverse proxying, HTTPS, monitoring, backups, and future AI/homelab automation.

The goal of this project is to build a production-style cloud environment that demonstrates practical Linux administration, security hardening, Docker hosting, public DNS routing, observability, and disaster recovery practices.

---

## Project Goals

- Build a secure public VPS foundation
- Host services using Docker and Docker Compose
- Configure domain DNS for public service routing
- Deploy a reverse proxy with HTTPS
- Separate production, staging, monitoring, and backup responsibilities
- Document each phase with validation screenshots
- Build portfolio-ready infrastructure documentation

---

## Planned Architecture

| Component | Role |
|---|---|
| Netcup VPS | Primary production/public services host |
| RackNerd VPS | Staging, monitoring, backups, and secondary services |
| stayz3ro.dev | Public domain for hosted services |
| Docker | Containerized application hosting |
| Reverse Proxy | Public routing and HTTPS termination |
| Tailscale | Private administrative access |
| UFW + Fail2Ban | Basic host-level security |
| Monitoring Stack | Availability and infrastructure visibility |

---

## Current Status

| Phase | Status |
|---|---|
| Phase 1 - VPS Baseline & Security Hardening | Complete |
| Phase 2 - Domain DNS & Public Routing | Planned |
| Phase 3 - Reverse Proxy & HTTPS | Planned |
| Phase 4 - Docker App Deployment | Planned |
| Phase 5 - Monitoring & Alerts | Planned |
| Phase 6 - Backups & Disaster Recovery | Planned |
| Phase 7 - Secondary VPS / Staging | Planned |
| Phase 8 - AI Agent / Homelab Ops Bot | Planned |

---

## Documentation

| Phase | Documentation |
|---|---|
| Phase 1 - VPS Baseline & Security Hardening | [View Phase 1](docs/phase-1-vps-baseline-security/README.md) |
| Architecture | [View Architecture Notes](docs/architecture/README.md) |
| Scripts | [View Scripts Notes](scripts/README.md) |

---

## Phase 1 Summary

Phase 1 focused on preparing the Netcup VPS as a secure Linux baseline before exposing any public services.

Completed items:

- Configured hostname
- Created non-root sudo user
- Validated SSH service
- Hardened SSH access
- Disabled root SSH login
- Disabled password SSH login
- Enabled UFW firewall
- Allowed only SSH, HTTP, and HTTPS
- Enabled Fail2Ban for SSH protection
- Enabled unattended upgrades
- Installed Docker and Docker Compose
- Installed Tailscale for private admin access
- Created organized `/opt/stayz3ro` server folder structure
- Reviewed listening ports

---

## Security Notes

This repository intentionally excludes:

- Public IP addresses
- Private IP addresses where unnecessary
- SSH keys
- API keys
- Provider credentials
- Tailscale authentication data
- Billing or account information
- Unredacted screenshots

Screenshots are redacted before being committed.

---

## Future Roadmap

- Configure domain DNS for `stayz3ro.dev`
- Deploy reverse proxy with HTTPS
- Deploy first public Docker service
- Add uptime monitoring
- Add offsite backups to secondary VPS
- Build staging/production split
- Build an AI-powered infrastructure assistant for quick homelab and VPS checks
