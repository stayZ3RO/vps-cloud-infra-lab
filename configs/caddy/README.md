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
| Backend application ports | Internal `web` Docker network; Kuma also publishes IPv4 loopback port 3001 for Stage 0b |
| Caddy admin API | Disabled (`admin off`) |

---

## Stage 0b: deployment gates

Run these checks during the live session, before Stage 3b restricts the public
status routes. Before enabling the Kuma loopback mapping, check the Docker
server version on the VPS:

```bash
docker version --format '{{.Server.Version}}'
```

Require Docker Engine 28.0.0 or newer. Earlier releases can expose a
localhost-published port to other hosts on the same L2 segment; see
[Docker's port-publishing warning](https://docs.docker.com/engine/network/port-publishing/).
If the server is older or its version cannot be checked, stop before enabling
the mapping. Handle any upgrade as a separate approved change.

After recreating only Kuma as directed in Stage 0b, check from this directory:

```bash
docker compose ps --format '{{.Name}} {{.Status}} {{.Ports}}'
curl -sS -o /dev/null -w 'kuma loopback %{http_code}\n' http://127.0.0.1:3001/
```

Require `127.0.0.1:3001->3001/tcp`, no wildcard or IPv6 port 3001 mapping,
and loopback HTTP `302`.

From a separate machine off the tailnet, with working public DNS and no HTTP
proxy, first confirm the public HTTPS host responds, then check port 3001:

```bash
curl --noproxy '*' -sS -m 10 -o /dev/null -w 'https %{http_code}\n' https://status.stayz3ro.dev/
curl --noproxy '*' -sS -m 5 -o /dev/null -w 'http=%{http_code} connects=%{num_connects}\n' http://status.stayz3ro.dev:3001/
```

Require a normal HTTPS response and `http=000 connects=0` on port 3001,
with curl reporting connection refusal or timeout (exit 7 or 28). DNS failure,
proxy failure, a successful TCP connection or a failing HTTPS control does not
pass this gate. If the test fails, stop and use the Stage 0b rollback; do not
continue to the public route restriction.

Before Stage 3b, check every push client. Configure its protected destination
as `$KUMA_TS_URL/api/push/<token>` on a host with the required tailnet access.
Verify one real client run and its monitor returning UP. Record client names
and results only; keep tokens and full push URLs out of Git and logs. If no
push clients exist, record that after checking. Any unverified client blocks
Stage 3b: the public host will reject `/api/push/*`, including requests redirected
from the old status hostname.

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
