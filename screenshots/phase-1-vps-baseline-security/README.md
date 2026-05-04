# Phase 1 - Screenshot Evidence 📸

This folder contains redacted validation screenshots for Phase 1: VPS Baseline & Security Hardening.

The screenshots provide visual proof that the VPS baseline was configured and validated.

---

## Screenshot Index

| # | Evidence | Purpose |
|---|---|---|
| 02 | Hostname validation | Confirms clean hostname configuration |
| 03 | OS version | Documents the Ubuntu Linux baseline |
| 05 | SSH service status | Confirms SSH is active and running |
| 06 | SSH config validation | Confirms SSH configuration syntax passed |
| 07 | UFW firewall status | Confirms firewall rules and limited exposure |
| 08 | Fail2Ban status | Confirms SSH brute-force protection |
| 09 | Unattended upgrades | Confirms automatic security updates |
| 10 | Swap and memory check | Confirms memory and swap state |
| 11 | Docker validation | Confirms Docker and Docker Compose are installed |
| 12 | Tailscale status | Confirms private access is connected |
| 13 | VPS folder structure | Confirms /opt/stayz3ro layout |
| 14 | Listening ports | Confirms active listening services were reviewed |

---

## Optional Screenshots

The following screenshots can be added later if needed:

| # | Evidence | Note |
|---|---|---|
| 01 | Netcup VPS dashboard | Must be fully redacted before committing |
| 04 | Sudo user group validation | Useful but not required for current evidence set |

---

## Redaction Notice

Sensitive values are redacted before committing screenshots.

Redacted or excluded items include:

- Public IPv4 addresses
- IPv6 addresses
- Tailscale IPs
- Tailscale device names where needed
- Provider account details
- Customer numbers
- Email addresses
- Authentication URLs
- API keys
- SSH keys
- Billing details

---

## Related Documentation

| Document | Link |
|---|---|
| Phase 1 Overview | ../../docs/phase-1-vps-baseline-security/overview.md |
| Phase 1 Step-by-Step Guide | ../../docs/phase-1-vps-baseline-security/step-by-step.md |
| Phase 1 Validation Evidence | ../../docs/phase-1-vps-baseline-security/validation.md |
