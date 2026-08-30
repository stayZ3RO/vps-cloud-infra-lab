# Phase 3 - Screenshot Evidence 📸

This folder contains redacted validation screenshots for Phase 3: Reverse
Proxy & HTTPS.

---

## Screenshot Index

| # | Evidence | Purpose |
|---|---|---|
| 01 | `docker compose ps` | Caddy running, ports 80/443 published |
| 02 | Compose logs - cert issuance | Let's Encrypt certificate obtained |
| 03 | `curl -I http://` | HTTP returns 308 redirect to HTTPS |
| 04 | `curl -Iv https://` | Valid Let's Encrypt certificate chain |
| 05 | Browser padlock | Public HTTPS on `stayz3ro.dev` |
| 06 | `curl -I https://www` | `www` redirects to apex |
| 07 | Response headers | Security headers present |
| 08 | `access.log` | Structured JSON logging active |
| 09 | Backend port probe | App ports not reachable publicly |

---

## Redaction Notice

Sensitive values are redacted before committing screenshots.

Redacted or excluded items include:

- Public IPv4 address
- Public IPv6 address
- Tailscale IP
- ACME / account email
- SSH host fingerprint
- Provider account data

---

## Related Documentation

| Document | Link |
|---|---|
| Phase 3 Overview | [overview.md](../../docs/phase-3-reverse-proxy-https/overview.md) |
| Phase 3 Step-by-Step Guide | [step-by-step.md](../../docs/phase-3-reverse-proxy-https/step-by-step.md) |
| Phase 3 Validation Evidence | [validation.md](../../docs/phase-3-reverse-proxy-https/validation.md) |
