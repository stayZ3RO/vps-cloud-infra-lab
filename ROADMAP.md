# Roadmap

This roadmap tracks the planned buildout for the VPS Cloud Infrastructure Lab.

The project starts with a secure Linux baseline, then layers on DNS, HTTPS, container hosting, monitoring, backups, a secondary VPS, and future AI-assisted infrastructure operations.

---

## Phase Overview

| Phase | Status | Focus |
|---|---:|---|
| Phase 1 - VPS Baseline & Security Hardening | ✅ Complete | Secure the Netcup VPS before public hosting |
| Phase 2 - Domain DNS & Public Routing | ✅ Complete | Connected stayz3ro.dev to the VPS |
| Phase 3 - Reverse Proxy & HTTPS | ✅ Complete | Route services through HTTPS |
| Phase 4 - Docker App Deployment | 🚧 In Progress | Deploy public containerized services (app chosen: Umami) |
| Phase 5 - Monitoring & Alerts | ⏳ Planned | Add uptime and service visibility |
| Phase 6 - Backups & Disaster Recovery | ⏳ Planned | Build recovery and backup strategy |
| Phase 7 - Secondary VPS / Staging | ⏳ Planned | Use RackNerd for staging, monitoring, and backups |
| Phase 8 - AI Agent / Homelab Ops Bot | ⏳ Planned | Experiment with infrastructure assistant workflows |

---

## Phase 1 - VPS Baseline & Security Hardening

Status: ✅ Complete

Purpose:

Establish a secure and validated Linux server baseline before exposing applications or services to the public internet.

Completed:

- Provisioned Netcup VPS
- Configured hostname
- Created non-root sudo user
- Hardened SSH
- Disabled root SSH login
- Disabled password SSH login
- Enabled UFW firewall
- Allowed only SSH, HTTP, and HTTPS
- Enabled Fail2Ban for SSH protection
- Enabled unattended upgrades
- Installed Docker and Docker Compose
- Installed Tailscale
- Created /opt/stayz3ro folder structure
- Reviewed listening ports
- Captured validation screenshots

---

## Phase 2 - Domain DNS & Public Routing

Status: ✅ Complete

Purpose:

Connect the stayz3ro.dev domain to the VPS and establish a clean DNS foundation for public services.

Completed:

- Configured Porkbun DNS records
- Removed default parking records
- Added root domain record
- Added www record
- Added apps, status, and api records
- Validated local DNS resolution
- Validated public resolvers
- Restricted SSH to Tailscale
- Captured redacted DNS and security screenshots

Example future subdomain plan:

| Subdomain | Intended Purpose |
|---|---|
| stayz3ro.dev | Main landing page or portfolio |
| www.stayz3ro.dev | Web alias |
| apps.stayz3ro.dev | Public app entry point |
| status.stayz3ro.dev | Status or uptime page |
| lab.stayz3ro.dev | Lab services |
| api.stayz3ro.dev | API services |

---

## Phase 3 - Reverse Proxy & HTTPS

Status: ✅ Complete

Purpose:

Deploy a reverse proxy to route public services securely through HTTPS.

Completed:

- Chose Caddy (automatic HTTPS, no admin port, no database)
- Configured HTTP to HTTPS routing (`308` redirect)
- Issued a Let's Encrypt TLS certificate for `status.stayz3ro.dev`
- Routed `status.stayz3ro.dev` to Uptime Kuma; `apps`/`api` staged for later
- Application ports never published to the host
- Documented proxy design (`configs/caddy/README.md`)
- Validated HTTPS externally (curl + browser)
- Secured Uptime Kuma's admin account before public exposure

See `CHANGELOG.md` and `LESSONS-LEARNED.md` for the full deployment record,
including the DNS zone mismatch that blocked the first deploy attempt.

---

## Phase 4 - Docker App Deployment

Status: 🚧 In Progress

Purpose:

Deploy the first public Dockerized service on the VPS.

App selected (2026-08-30): **Umami** — privacy-first web analytics at
`analytics.stayz3ro.dev` (Umami + PostgreSQL). Candidate comparison:
`docs/phase-4-docker-app-deployment/overview.md`.

Planned tasks:

- Create Docker Compose service layout
- Deploy first public app
- Route app through reverse proxy
- Validate external access
- Document environment variables
- Add .env.example files
- Capture deployment screenshots

---

## Phase 5 - Monitoring & Alerts

Status: ⏳ Planned

Purpose:

Add visibility into service availability and VPS health.

Planned tasks:

- Add uptime monitoring
- Monitor public endpoints
- Monitor system health
- Add alerts
- Document response process
- Capture monitoring screenshots

Possible tools:

- Uptime Kuma
- Prometheus
- Grafana
- Beszel
- Netdata

---

## Phase 6 - Backups & Disaster Recovery

Status: ⏳ Planned

Purpose:

Create a backup and restore strategy for hosted services.

Planned tasks:

- Define backup targets
- Back up Docker volumes
- Back up app data
- Back up databases
- Test restore process
- Document recovery steps
- Plan offsite backups

---

## Phase 7 - Secondary VPS / Staging

Status: ⏳ Planned

Purpose:

Use the RackNerd VPS as a secondary node for staging, monitoring, backups, and experiments.

Planned tasks:

- Provision RackNerd VPS
- Apply same baseline security hardening
- Configure staging services
- Add monitoring responsibilities
- Configure offsite backup target
- Document role separation between VPS nodes

---

## Phase 8 - AI Agent / Homelab Ops Bot

Status: ⏳ Planned

Purpose:

Experiment with an AI-assisted infrastructure helper that can answer quick questions about VPS and homelab status.

Planned capabilities:

- Query uptime status
- Summarize service health
- Check documentation
- Provide quick operational reminders
- Support private access through secure channels
- Avoid exposing privileged systems publicly
