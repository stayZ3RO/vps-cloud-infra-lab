# Caddy Reverse Proxy ⚙️

Reverse proxy and automatic HTTPS for the VPS Cloud Infrastructure Lab.

Phase: **Phase 3 - Reverse Proxy & HTTPS**

---

## Files

| File | Purpose |
|---|---|
| `Caddyfile` | Proxy + TLS + static site config (public-safe, no secrets) |
| `docker-compose.yml` | Caddy container stack |
| `.env.example` | Template for `SITE_DOMAIN` and `ACME_EMAIL` |
| `logs/` | JSON access logs (gitignored, created at runtime) |

---

## Why Caddy

| Option | Verdict |
|---|---|
| **Caddy** | Chosen. Single config file, automatic Let's Encrypt issuance and renewal, no admin port, no database. Smallest attack surface for a public node. |
| Nginx Proxy Manager | Rejected. Adds a database and an admin dashboard port that would then need Tailscale-only lockdown - cuts against the "administration lives on Tailscale" model. Its database stores proxy config, not logs. |
| Traefik | Deferred. Strong Docker-native / Kubernetes-ingress option; heavier config for a single-service start. A good later on-ramp when the Kubernetes track begins. |

Access logging (the "corp practice" requirement) is a config option, not a
reason to pick a heavier proxy - Caddy emits structured JSON access logs here.

---

## What is exposed

| Surface | Exposure |
|---|---|
| `https://stayz3ro.dev` | Public - static landing page only |
| `https://www.stayz3ro.dev` | Public - 308 redirect to apex |
| `apps` / `status` / `api` subdomains | Staged in `Caddyfile`, disabled until Phase 4 |
| Backend application ports | Never published - internal `web` Docker network only |
| Caddy admin API | Disabled (`admin off`) |

---

## Run

On the VPS, over Tailscale SSH:

    cd <repo>/configs/caddy
    cp .env.example .env
    # edit .env - set ACME_EMAIL to a real inbox
    mkdir -p logs
    docker compose up -d
    docker compose logs -f caddy   # watch for "certificate obtained successfully"

## Update config

    # after editing Caddyfile
    docker compose exec caddy caddy validate --config /etc/caddy/Caddyfile
    docker compose exec caddy caddy reload --config /etc/caddy/Caddyfile

## Certificate persistence

Issued certificates and the ACME account live in the `caddy_data` named
volume. Do not delete it - Let's Encrypt rate limits (50 certs/week per
registered domain) make repeated re-issuance costly.

---

## Security notes

- `.env` is gitignored. Never commit it.
- `logs/` is gitignored.
- No public IPs, keys, or account data belong in this folder.
- HSTS is set to 1 year in the `Caddyfile`. Lower it while testing if unsure.
