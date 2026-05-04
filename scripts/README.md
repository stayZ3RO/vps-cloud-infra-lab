# Scripts 🧰

This folder will hold future VPS maintenance, validation, backup, and automation scripts.

No production scripts are required for Phase 1 yet.

---

## Planned Script Categories

| Category | Purpose |
|---|---|
| Health checks | Quick VPS and service status checks |
| Docker checks | Validate running containers, networks, and volumes |
| Backup jobs | Back up Docker volumes, app data, and databases |
| Restore tests | Validate recovery workflows |
| Reverse proxy checks | Confirm routing and HTTPS behavior |
| DNS checks | Validate domain and subdomain resolution |
| Security checks | Review firewall, listening ports, and service exposure |
| Deployment helpers | Standardize app deployment steps |

---

## Future Examples

Potential future scripts:

| Script | Purpose |
|---|---|
| check-vps-baseline.sh | Validate hostname, firewall, SSH, Docker, and Tailscale |
| check-listening-ports.sh | Show listening services and public exposure |
| docker-backup.sh | Back up selected Docker volumes |
| restore-test.sh | Test backup restoration |
| dns-check.sh | Validate DNS records for stayz3ro.dev |
| proxy-check.sh | Validate reverse proxy and HTTPS routing |

---

## Script Safety Rules

Future scripts should follow these rules:

- Do not hardcode secrets
- Do not commit API keys
- Do not include private IPs unless sanitized
- Use .env.example for safe placeholders
- Prefer read-only checks where possible
- Add comments explaining each command
- Test scripts before documenting them
- Avoid destructive actions unless clearly labeled

---

## Current Status

Phase 1 did not require custom scripts.

This folder is included to support future automation as the VPS lab expands into DNS, reverse proxy, monitoring, backups, and multi-VPS workflows.
