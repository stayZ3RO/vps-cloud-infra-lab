# Changelog

This changelog tracks major documentation and infrastructure milestones for the VPS Cloud Infrastructure Lab.

---

## Phase 1 - VPS Baseline & Security Hardening

Status: ✅ Complete

### Added

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

### Completed

- Provisioned Netcup VPS
- Configured hostname as netcup-prod-01
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
- Created /opt/stayz3ro service folder structure
- Reviewed listening ports
- Captured redacted validation screenshots

### Documentation Improvements

- Restructured repo to match phase-based infrastructure documentation style
- Moved screenshots into a top-level screenshots folder
- Embedded Phase 1 validation screenshots directly in the validation page
- Added project-level roadmap and current status
- Added lessons learned for operational reflection
- Added sanitized config examples for security controls
- Polished the main README for clearer project presentation

---

## Upcoming

### Phase 2 - Domain DNS & Public Routing

Planned:

- Configure stayz3ro.dev DNS
- Add root domain record
- Add www record
- Plan service subdomains
- Validate DNS resolution
- Document DNS routing
- Capture redacted DNS screenshots

### Phase 3 - Reverse Proxy & HTTPS

Planned:

- Deploy reverse proxy
- Configure HTTPS certificates
- Route services through subdomains
- Validate HTTP to HTTPS behavior
- Avoid direct app port exposure

---

## Phase 2 - Domain DNS & Public Routing

### Added

- Phase 2 documentation folder
- Phase 2 overview
- Phase 2 step-by-step guide
- Phase 2 validation evidence
- Phase 2 screenshot evidence folder
- Phase 2 DNS routing diagram

### Completed

- Removed Porkbun parking DNS records
- Added root domain A record
- Added www CNAME record
- Added apps subdomain A record
- Added status subdomain A record
- Added api subdomain A record
- Validated local DNS resolution
- Validated public resolver DNS results
- Confirmed SSH listening state
- Validated SSH over Tailscale
- Blocked public SSH access
- Confirmed UFW allows SSH only over Tailscale
- Captured and redacted Phase 2 screenshots

### Security Improvement

Administrative SSH access is now restricted to the Tailscale private network.

Public exposure is limited to HTTP and HTTPS for future reverse proxy traffic.
