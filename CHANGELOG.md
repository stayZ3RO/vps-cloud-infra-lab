# Changelog 📝

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Phase 1](https://img.shields.io/badge/phase_1-complete-success)
![Phase 2](https://img.shields.io/badge/phase_2-complete-success)
![Next](https://img.shields.io/badge/next-Reverse%20Proxy%20%26%20HTTPS-blue)

This changelog tracks major documentation and infrastructure milestones for the VPS Cloud Infrastructure Lab.

---

## Current State

| Phase | Status |
|---|---:|
| Phase 1 - VPS Baseline & Security Hardening | ✅ Complete |
| Phase 2 - Domain DNS & Public Routing | ✅ Complete |
| Phase 3 - Reverse Proxy & HTTPS | ⏳ Planned |

---

# Phase 1 - VPS Baseline & Security Hardening

Status: ✅ Complete

## Added

- Main project README
- Current status document
- Roadmap document
- Lessons learned document
- Phase 1 overview
- Phase 1 step-by-step guide
- Phase 1 validation evidence
- Phase 1 architecture diagram
- Screenshot evidence folder
- Sanitized SSH configuration example
- Sanitized UFW rules example
- Sanitized Fail2Ban jail example
- Scripts folder placeholder
- Config folder structure

## Completed

- Provisioned Netcup VPS
- Configured hostname as `netcup-prod-01`
- Created non-root sudo user
- Confirmed sudo access
- Validated SSH service status
- Validated SSH configuration syntax
- Disabled root SSH login
- Disabled password-based SSH login
- Enabled UFW firewall
- Allowed SSH, HTTP, and HTTPS
- Enabled Fail2Ban for SSH
- Enabled unattended upgrades
- Installed Docker
- Installed Docker Compose
- Installed Tailscale
- Created `/opt/stayz3ro` service folder structure
- Reviewed listening ports
- Captured redacted validation screenshots

## Documentation Improvements

- Restructured repo to match phase-based infrastructure documentation style
- Moved screenshots into a top-level screenshots folder
- Embedded Phase 1 validation screenshots directly in the validation page
- Added project-level roadmap and current status
- Added lessons learned for operational reflection
- Added sanitized config examples for security controls
- Polished the main README for clearer project presentation

---

# Phase 2 - Domain DNS & Public Routing

Status: ✅ Complete

## Added

- Phase 2 documentation folder
- Phase 2 overview
- Phase 2 step-by-step guide
- Phase 2 validation evidence
- Phase 2 screenshot evidence folder
- Phase 2 DNS routing diagram
- Phase 2 screenshot index
- Project-level navigation links for Phase 2

## Completed

- Removed Porkbun parking DNS records
- Added root domain A record for `stayz3ro.dev`
- Added `www` CNAME record
- Added `apps` subdomain A record
- Added `status` subdomain A record
- Added `api` subdomain A record
- Validated local DNS resolution
- Validated public resolver DNS results
- Confirmed SSH listening state
- Validated SSH over Tailscale
- Removed public SSH firewall rules
- Blocked public SSH access
- Confirmed UFW allows SSH only over Tailscale
- Confirmed HTTP and HTTPS remain public for future reverse proxy traffic
- Captured and redacted Phase 2 screenshots

## Security Improvement

Administrative SSH access is now restricted to the Tailscale private network.

Final management-plane model:

| Access | Status |
|---|---:|
| Public SSH | Blocked |
| Tailscale SSH | Allowed |
| Public HTTP | Allowed |
| Public HTTPS | Allowed |
| Direct app ports | Blocked |
| Admin dashboards | Not publicly exposed |

## Validation Evidence

Phase 2 validation screenshots cover:

- Porkbun DNS records
- Local DNS resolution
- Public resolver validation
- UFW state before public SSH cleanup
- SSH listening port
- Tailscale SSH success
- Final UFW Tailscale-only SSH state
- Public SSH blocked test

---

# Upcoming

## Phase 3 - Reverse Proxy & HTTPS

Status: ⏳ Planned

Planned work:

- Choose reverse proxy platform
- Deploy reverse proxy with Docker Compose
- Configure HTTP to HTTPS behavior
- Issue TLS certificates
- Route `stayz3ro.dev`
- Route `www.stayz3ro.dev`
- Prepare `apps`, `status`, and `api` subdomains
- Keep backend application ports private
- Validate HTTPS externally
- Capture redacted screenshots
- Document Phase 3 implementation and validation

Recommended reverse proxy direction:

| Option | Notes |
|---|---|
| Caddy | Clean config, automatic HTTPS, strong fit for this repo |
| NGINX | Traditional reverse proxy, useful for deeper web-server experience |
| Nginx Proxy Manager | Easy UI, but less infrastructure-as-code focused |
| Traefik | Strong Docker-native option, more complex |

Current recommendation:

**Caddy for Phase 3** because it keeps the reverse proxy and HTTPS story clean, version-controlled, and easy to document.
