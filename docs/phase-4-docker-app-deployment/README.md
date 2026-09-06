# Phase 4 - Docker App Deployment 🐳

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![Phase](https://img.shields.io/badge/phase-4-blue)
![App](https://img.shields.io/badge/app-Umami-success)
![Proxy](https://img.shields.io/badge/proxy-behind%20Caddy-success)
![Scope](https://img.shields.io/badge/scope-app%20selection-purple)

## Phase Summary

Phase 4 deploys the first application container behind the Phase 3 Caddy
reverse proxy, on a public subdomain, with no backend port published to the
host. Uptime Kuma (`status.stayz3ro.dev`) proved the proxy pattern; this phase
proves the repeatable app-onboarding pattern: compose service, env template,
Caddy route, DNS record, validation, evidence.

**App selected (2026-08-30): Umami**, privacy-first web analytics, at
`analytics.stayz3ro.dev`, real visitor analytics for the blog and portfolio,
and the VPS's first stateful service (Umami + PostgreSQL). Candidate
comparison and rationale: [overview.md](overview.md).

---

## What This Phase Will Demonstrate

| Area | Demonstrated Skill |
|---|---|
| App deployment | Multi-container app (service + database) via Docker Compose |
| Exposure control | App joined to the internal `web` network; only Caddy on 80/443 |
| Configuration management | `.env.example` committed, real `.env` gitignored on the VPS |
| DNS operations | New subdomain record in the **live** zone (Cloudflare, not Porkbun) |
| Security sequencing | Admin account claimed over a private tunnel before public exposure |
| Service integration | New hostname added as an Uptime Kuma monitor |
| Evidence discipline | Redacted deployment screenshots |

---

## Candidate Apps (Shortlist)

**Decision (2026-08-30): Umami (A) selected; subdomain `analytics.stayz3ro.dev`.**

The shortlist record:

| # | App | Subdomain | One-line case |
|---|---|---|---|
| A ✅ | **Umami** - privacy-first web analytics | `analytics.stayz3ro.dev` | Real visitor stats for the blog and portfolio; first stateful service |
| B | **Shlink** - self-hosted URL shortener | `apps.` + `api.stayz3ro.dev` | Branded short links + a real public REST API, using both staged routes |
| C | **Vikunja** - task/project tracker | `tasks.stayz3ro.dev` or Tailscale-only | Closes a pending cross-repo tooling decision; auth/exposure tradeoff exercise |

Full comparison, tradeoffs, and recommendation:
[overview.md](overview.md).

---

## Documentation

| Page | Description | Status |
|---|---|---|
| [Overview](overview.md) | Scoping record: candidates, comparison, decision | ✅ Complete |
| [Step-by-Step Guide](step-by-step.md) | Implementation runbook (Umami stack, tunnel claim, DNS, Caddy route, validation) | ✅ Written, pending execution |
| [Validation Evidence](validation.md) | Checklist and screenshot evidence | ⏳ Pending execution |
| [Architecture Diagram](../../diagrams/phase-4-docker-app-deployment.md) | App + database network layout behind Caddy | ✅ Complete |
| [Umami Config](../../configs/umami/) | Compose stack, `.env.example`, README | ✅ Complete |

---

## Completion Criteria

| Requirement | Status |
|---|---:|
| App chosen and justified against candidates | ✅ Complete (Umami) |
| Compose service layout committed (app + database, `web` network, no published ports) | ✅ Complete |
| `.env.example` committed; real `.env` gitignored | ✅ Complete |
| DNS record added in the live zone and validated | ⏳ Pending |
| Caddy route enabled and validated (`caddy validate` + reload) | ⏳ Pending |
| App deployed and reachable externally over HTTPS | ⏳ Pending |
| Admin account secured over a private path before exposure | ⏳ Pending |
| Backend/database ports confirmed not publicly reachable | ⏳ Pending |
| New hostname added as an Uptime Kuma monitor | ⏳ Pending |
| Redacted screenshots captured | ⏳ Pending |

---

## Evidence

Redacted validation screenshots will be stored in a new
`screenshots/phase-4-docker-app-deployment/` folder, following the standing
redaction rules. See [screenshots/](../../screenshots/) for the existing
evidence layout.

---

## Before This Phase Deploys

The Phase 3 screenshot checklist
([screenshots/phase-3-reverse-proxy-https/README.md](../../screenshots/phase-3-reverse-proxy-https/README.md),
9 items) is still unfilled. The Phase 3 stack is live right now. Capture that
evidence **before** Phase 4 changes anything about the running deployment.

---

## Next Phase

Next: **Phase 5 - Monitoring & Alerts**

The app deployed here becomes a real monitored workload, and its traffic/state
gives Phase 5 something meaningful to watch.
