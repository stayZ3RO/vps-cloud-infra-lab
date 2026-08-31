# Phase 4 - Step-by-Step Guide 🛠️

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![Scope](https://img.shields.io/badge/scope-Docker%20App%20Deployment-blue)
![App](https://img.shields.io/badge/app-Umami-success)
![Proxy](https://img.shields.io/badge/proxy-behind%20Caddy-success)

## Purpose

This guide is the implementation runbook for deploying Umami web analytics
(`analytics.stayz3ro.dev`) as the first application container behind the
Phase 3 Caddy reverse proxy.

Run it on the VPS over Tailscale SSH.

**Prerequisite**: capture the 9 outstanding Phase 3 evidence screenshots
([screenshots/phase-3-reverse-proxy-https/README.md](../../screenshots/phase-3-reverse-proxy-https/README.md))
before starting - this run changes the live deployment, and that evidence
window closes when it does.

---

## Implementation Flow

| Step | Task | Status |
|---|---|---:|
| 1 | Confirm prerequisites (proxy stack, `web` network, headroom) | ⏳ Pending |
| 2 | Create `.env` from the template | ⏳ Pending |
| 3 | Validate the compose config | ⏳ Pending |
| 4 | Bring up the Umami stack | ⏳ Pending |
| 5 | Claim the admin account over an SSH tunnel (before exposure) | ⏳ Pending |
| 6 | Add the `analytics` DNS record in Cloudflare (the live zone) | ⏳ Pending |
| 7 | Enable the Caddy route (uncomment, validate, reload) | ⏳ Pending |
| 8 | Validate HTTPS externally | ⏳ Pending |
| 9 | Confirm backend and database ports are not public | ⏳ Pending |
| 10 | Add an Uptime Kuma monitor for the new host | ⏳ Pending |
| 11 | Wire the blog embed (separate repo) | ⏳ Pending |
| 12 | Capture redacted screenshots | ⏳ Pending |

---

## Step 1 - Confirm Prerequisites

The Phase 3 proxy stack must be running, since it creates the `web` network
this app joins:

    cd /opt/stayz3ro/proxy   # or wherever the repo is checked out
    git pull
    cd configs/caddy && docker compose ps

Expected: `caddy` and `uptime-kuma` running.

    docker network ls | grep -w web

Expected: a network named `web` exists.

Confirm the VPS has headroom for a second stack (small VPS - check before
adding, not after):

    free -h

---

## Step 2 - Create the Environment File

    cd configs/umami
    cp .env.example .env
    nano .env
    chmod 600 .env

Set:

| Variable | Value |
|---|---|
| `POSTGRES_PASSWORD` | Long random value. Avoid URL-special characters (`!`, `#`, `%`, `&`, ...) - it is embedded in `DATABASE_URL` |
| `APP_SECRET` | Output of `openssl rand -base64 32` |

`.env` is gitignored - it stays on the VPS only.

---

## Step 3 - Validate the Compose Config

    docker compose config --quiet

Expected: no output, exit 0.

Note the `--quiet`: the resolved config interpolates the real password into
`DATABASE_URL`, so printing it (the default) would put the secret on screen
and into any terminal capture.

---

## Step 4 - Bring Up the Umami Stack

    docker compose up -d
    docker compose ps

Expected: `umami` and `umami-db` running, **no ports published** for either
service.

Confirm the database initialized and the app connected and migrated:

    docker compose logs umami | tail -n 20

Expected: Umami startup without database errors.

---

## Step 5 - Claim the Admin Account BEFORE Public Exposure

Umami ships with default credentials (`admin` / `umami`). The moment a Let's
Encrypt certificate is issued, Certificate Transparency logs make the
hostname discoverable to scanners - so the default login must be replaced
first, over a private path.

Get the `umami` container's internal Docker network IP:

    docker inspect -f '{{range $k, $v := .NetworkSettings.Networks}}{{$k}} {{.IPAddress}}{{"\n"}}{{end}}' umami

From the workstation, tunnel to the container's `web`-network IP (local port
`13000`; keep the SSH session open):

    ssh -L 13000:<umami_web_network_ip>:3000 <user>@<tailscale-ip>

Open `http://localhost:13000` in the browser, sign in with the defaults, and
immediately:

- Change the admin username and password
- Add the first website entry (the blog) so the embed script exists before
  the public route does

No public hostname, DNS record, or certificate exists yet - the race window
cannot open. This is the Phase 3 Uptime Kuma pattern, applied by default.

---

## Step 6 - Add the DNS Record in Cloudflare (the Live Zone)

`stayz3ro.dev`'s registry-delegated nameservers are Cloudflare's - records
edited in Porkbun's panel are never consulted. Verify the delegation first
(through DoH if the workstation runs MagicDNS):

    curl -s 'https://dns.google/resolve?name=stayz3ro.dev&type=NS'

Expected: Cloudflare nameservers (`felipe`/`melissa.ns.cloudflare.com`).

In the **Cloudflare** dashboard, add:

| Record | Name | Content | Proxy |
|---|---|---|---|
| A | `analytics` | Netcup VPS public IP | **DNS only** (grey cloud) - Caddy terminates TLS itself, and ACME needs the direct connection |

Then validate from two independent perspectives:

    dig +short analytics.stayz3ro.dev
    curl -s 'https://dns.google/resolve?name=analytics.stayz3ro.dev&type=A'

Expected: both return the VPS public IP.

---

## Step 7 - Enable the Caddy Route

Uncomment the `analytics.{$SITE_DOMAIN}` block in
`configs/caddy/Caddyfile` (staged there for exactly this step).

Validate with the same throwaway-container pattern as Phase 3:

    cd ../caddy
    docker run --rm -v "$PWD/Caddyfile:/etc/caddy/Caddyfile:ro" \
      -e SITE_DOMAIN -e ACME_EMAIL \
      caddy:2-alpine caddy validate --config /etc/caddy/Caddyfile

Expected: `Valid configuration`.

Reload the live proxy without downtime (the Caddyfile is bind-mounted
read-only into the container):

    docker exec caddy caddy reload --config /etc/caddy/Caddyfile

Caddy obtains the certificate for `analytics.stayz3ro.dev` on first request.
Because Step 5 already replaced the default credentials, CT-log scanners
find a claimed service.

---

## Step 8 - Validate HTTPS Externally

From the workstation (not the VPS):

    curl -I http://analytics.stayz3ro.dev
    curl -I https://analytics.stayz3ro.dev
    curl -Iv https://analytics.stayz3ro.dev 2>&1 | grep -E 'subject:|issuer:|SSL certificate verify'

Expected:

- `http://` returns `308` with `Location: https://analytics.stayz3ro.dev/`
- `https://` returns `200` (Umami login page)
- Certificate issuer is Let's Encrypt; verification succeeds

Open `https://analytics.stayz3ro.dev` in the browser and confirm the padlock
and the Umami login page, and that the changed credentials sign in.

---

## Step 9 - Confirm Backend and Database Ports Are Not Public

From the workstation:

    curl -sS -m 5 http://<VPS_PUBLIC_IP>:3000 ; echo "exit=$?"
    curl -sS -m 5 http://<VPS_PUBLIC_IP>:5432 ; echo "exit=$?"

Expected: connection refused or timeout (non-zero exit). Only 80 and 443
answer.

Optional, if `nmap` is available:

    nmap -Pn -p 22,80,443,3000,3001,5432 <VPS_PUBLIC_IP>

Expected: `80` and `443` open; everything else closed/filtered.

---

## Step 10 - Add an Uptime Kuma Monitor

In `https://status.stayz3ro.dev`, add a new monitor:

| Setting | Value |
|---|---|
| Monitor type | HTTP(s) |
| URL | `https://analytics.stayz3ro.dev` |

Expected: the monitor goes **Up**. The first app now watches the second.

---

## Step 11 - Wire the Blog Embed (Separate Repo)

Get the embed snippet from Umami's dashboard (website entry added in
Step 5):

    <script defer src="https://analytics.stayz3ro.dev/script.js"
            data-website-id="..."></script>

Add it to the Astro blog's `<head>` **in the blog's own repository** and
deploy it there - this repo does not touch the blog. Coordinate the change
explicitly with that project (parallel-repos lesson from Phase 3).

Verify end-to-end: load the blog, then confirm the visit appears in the
Umami dashboard.

---

## Step 12 - Capture Screenshots

Capture and redact:

| # | Evidence | Purpose |
|---|---|---|
| 01 | `docker compose ps` (umami + umami-db) | Stack running, no published ports |
| 02 | Umami login over the SSH tunnel | Admin claimed privately, pre-exposure |
| 03 | Changed credentials sign-in | Default `admin`/`umami` replaced |
| 04 | Cloudflare DNS `analytics` record | Record added in the live zone, DNS-only |
| 05 | `dig` + DoH resolution | Verified from two independent perspectives |
| 06 | `curl -I http://` -> 308 | HTTP redirects to HTTPS |
| 07 | `curl -Iv https://` cert chain | Valid Let's Encrypt certificate |
| 08 | Response headers | Security headers present |
| 09 | Browser padlock + Umami dashboard | Public HTTPS works, real service reachable |
| 10 | Backend port probes refused (3000, 5432) | App and database ports not public |
| 11 | Uptime Kuma monitor **Up** | New host monitored from day one |

Redact public IPv4/IPv6, Tailscale IPs, the admin username, website IDs, and
the ACME email before committing.

---

## Rollback

Disable the public route first, then stop the stack:

    # 1. comment the analytics block back out, then:
    docker exec caddy caddy reload --config /etc/caddy/Caddyfile
    # 2. stop the app:
    cd ../umami && docker compose down

The `umami_db_data` volume is kept unless `-v` is added - analytics data
survives rollback. Firewall, DNS, and SSH posture are unchanged by this
phase. The DNS record can be left in place or removed in Cloudflare.

---

## Phase Result

When all steps pass, `https://analytics.stayz3ro.dev` serves Umami publicly
with a valid certificate, the default admin login was replaced before the
hostname was discoverable, Postgres is unreachable from outside its own
internal network, the host is monitored in Uptime Kuma, and the VPS is
running its first stateful public service.
