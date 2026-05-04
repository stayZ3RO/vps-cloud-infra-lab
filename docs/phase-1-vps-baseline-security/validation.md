# Phase 1 - Validation Evidence

## Completion Criteria

Phase 1 is complete because:

- Hostname resolves correctly with no sudo warning
- Non-root sudo user works
- SSH service is active
- SSH config validates successfully
- Root SSH login is disabled
- Password SSH login is disabled
- UFW is enabled
- Only SSH, HTTP, and HTTPS are allowed
- Fail2Ban is active for SSH
- Unattended upgrades are enabled
- Docker and Docker Compose work
- Tailscale is installed and connected
- `/opt/stayz3ro` folder structure exists
- Listening ports are understood and documented

---

## Screenshot Evidence

| Evidence | Screenshot |
|---|---|
| Netcup VPS dashboard | `../../screenshots/phase-1-vps-baseline-security/01-netcup-vps-dashboard-redacted.png` |
| Hostname validation | `../../screenshots/phase-1-vps-baseline-security/02-hostnamectl.png` |
| OS version | `../../screenshots/phase-1-vps-baseline-security/03-os-version.png` |
| Sudo user validation | `../../screenshots/phase-1-vps-baseline-security/04-sudo-user-groups.png` |
| SSH service status | `../../screenshots/phase-1-vps-baseline-security/05-ssh-service-status.png` |
| SSH config validation | `../../screenshots/phase-1-vps-baseline-security/06-ssh-config-validation.png` |
| UFW firewall status | `../../screenshots/phase-1-vps-baseline-security/07-ufw-firewall-status.png` |
| Fail2Ban status | `../../screenshots/phase-1-vps-baseline-security/08-fail2ban-status.png` |
| Unattended upgrades | `../../screenshots/phase-1-vps-baseline-security/09-unattended-upgrades-status.png` |
| Swap and memory check | `../../screenshots/phase-1-vps-baseline-security/10-swap-memory-check.png` |
| Docker validation | `../../screenshots/phase-1-vps-baseline-security/11-docker-version.png` |
| Tailscale status | `../../screenshots/phase-1-vps-baseline-security/12-tailscale-status-redacted.png` |
| VPS folder structure | `../../screenshots/phase-1-vps-baseline-security/13-folder-structure.png` |
| Listening ports | `../../screenshots/phase-1-vps-baseline-security/14-listening-ports-redacted.png` |

---

## Redaction Rules

The following information was redacted before committing screenshots:

- Public IPv4 address
- IPv6 address
- Tailscale IPs
- Tailscale device identifiers where needed
- Netcup customer/account details
- Email addresses
- Authentication URLs
- API keys or tokens
- Billing details
