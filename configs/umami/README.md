# Umami Analytics Config 📊

Self-hosted, privacy-first (cookieless) web analytics for the blog and
portfolio, deployed as the Phase 4 application behind the Phase 3 Caddy
reverse proxy.

Chosen over Shlink and Vikunja - full comparison and rationale in
[docs/phase-4-docker-app-deployment/overview.md](../../docs/phase-4-docker-app-deployment/overview.md).

---

## Files

| File | Purpose |
|---|---|
| [docker-compose.yml](docker-compose.yml) | Umami + PostgreSQL stack; joins the external `web` network; no published ports |
| [.env.example](.env.example) | Public-safe environment template (real `.env` is gitignored, VPS-only) |

---

## Architecture

| Component | Network | Reachable from |
|---|---|---|
| `umami` (port 3000, not published) | `web` + `umami_internal` | Caddy (`web`), Postgres peer |
| `umami-db` (Postgres 16, port 5432, not published) | `umami_internal` (internal-only) | The `umami` container only - never the `web` network, never the host |

Caddy route (staged in `configs/caddy/Caddyfile`, enabled by the runbook):

    analytics.{$SITE_DOMAIN} {
        import security_headers
        reverse_proxy umami:3000
    }

---

## Usage

On the VPS, over Tailscale SSH, from the repo checkout:

    cd configs/umami
    cp .env.example .env
    nano .env            # POSTGRES_PASSWORD + APP_SECRET
    docker compose up -d

Rollback:

    docker compose down  # add -v to also delete analytics data - destructive

Full deployment procedure (admin claim over an SSH tunnel, DNS record in
Cloudflare, Caddy reload, validation):
[Phase 4 step-by-step guide](../../docs/phase-4-docker-app-deployment/step-by-step.md).

---

## First-Run Security

Umami ships with default credentials (`admin` / `umami`) and has no public
signup - but those defaults must be changed **before** the public hostname
exists, or Certificate Transparency log scanners get a window to log in
first. The runbook claims the admin account over an SSH tunnel to the
container's internal Docker network IP before the Caddy route or DNS record
is enabled - the same pattern that closed Uptime Kuma's race window in
Phase 3.

---

## Blog / Portfolio Embed

After deployment, Umami provides a website-specific embed script for the
Astro blog (a separate project/repo - coordinate the change there):

    <script defer src="https://analytics.stayz3ro.dev/script.js"
            data-website-id="..."></script>

The `data-website-id` is created in Umami's dashboard when the website
entry is added. Coordinate the blog-side change explicitly - the Phase 3
lesson about parallel repos making conflicting decisions applies.
