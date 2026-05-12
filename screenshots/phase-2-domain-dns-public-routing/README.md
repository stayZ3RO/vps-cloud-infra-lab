# Phase 2 - Screenshot Evidence 📸

This folder contains redacted validation screenshots for Phase 2: Domain DNS & Public Routing.

---

## Screenshot Index

| # | Evidence | Purpose |
|---|---|---|
| 01 | Porkbun DNS records | Confirms DNS records were configured |
| 02 | Local DNS resolution | Confirms local `dig +short` results |
| 03 | Public resolver validation | Confirms Cloudflare and Google DNS resolution |
| 04 | UFW before SSH cleanup | Shows public SSH before Tailscale-only hardening |
| 05 | SSH listening port | Confirms SSH service listening state |
| 06 | Tailscale SSH access success | Confirms private SSH access works |
| 07 | Final UFW state | Confirms SSH is only allowed over Tailscale |
| 08 | Public SSH blocked | Confirms public SSH access fails |

---

## Redaction Notice

Sensitive values are redacted before committing screenshots.

Redacted or excluded items include:

- Public IPv4 address
- IPv6 address
- Tailscale IP
- SSH host fingerprint
- Porkbun account details
- Email addresses
- API access details
- Billing details
- Provider account data

---

## Related Documentation

| Document | Link |
|---|---|
| Phase 2 Overview | [overview.md](../../docs/phase-2-domain-dns-public-routing/overview.md) |
| Phase 2 Step-by-Step Guide | [step-by-step.md](../../docs/phase-2-domain-dns-public-routing/step-by-step.md) |
| Phase 2 Validation Evidence | [validation.md](../../docs/phase-2-domain-dns-public-routing/validation.md) |
