# Phase 4 - Validation Evidence 📸

![Status](https://img.shields.io/badge/status-pending%20execution-yellow)
![App](https://img.shields.io/badge/app-Umami-success)
![Proxy](https://img.shields.io/badge/proxy-behind%20Caddy-success)
![Domain](https://img.shields.io/badge/domain-analytics.stayz3ro.dev-purple)

## Purpose

This page documents validation evidence for Phase 4: Docker App Deployment
(Umami at `analytics.stayz3ro.dev`).

The goal is to confirm that the app is publicly reachable over HTTPS with a
valid certificate, that the default admin credentials were replaced before
public exposure, that no backend or database port answers publicly, that the
host is monitored, and that real analytics events flow from the blog.

> This phase is scaffolded but not yet executed. The tables below are the
> checklist to fill in during the run described in
> [step-by-step.md](step-by-step.md).

---

## Validation Summary

| Area | Expected Result | Status |
|---|---|---|
| `umami` container | Running, no published ports, on the `web` + internal networks | ⏳ Pending |
| `umami-db` container | Running, internal-only network, not reachable from `web` | ⏳ Pending |
| Admin credentials | Changed from defaults over an SSH tunnel **before** DNS/route/cert existed | ⏳ Pending |
| DNS record | `analytics.stayz3ro.dev` A record in the Cloudflare zone, DNS-only, resolves from two perspectives | ⏳ Pending |
| Certificate | Issued by Let's Encrypt for `analytics.stayz3ro.dev` | ⏳ Pending |
| HTTP -> HTTPS | `http://analytics.stayz3ro.dev` returns 308 to HTTPS | ⏳ Pending |
| HTTPS | `https://analytics.stayz3ro.dev` returns 200, valid chain, Umami login | ⏳ Pending |
| Security headers | HSTS, nosniff, DENY, Referrer-Policy present | ⏳ Pending |
| Backend ports | 3000 (app) and 5432 (Postgres) not reachable on the public IP | ⏳ Pending |
| Uptime Kuma monitor | New monitor for `https://analytics.stayz3ro.dev` is **Up** | ⏳ Pending |
| Analytics events | Blog embed sends visits visible in the Umami dashboard | ⏳ Pending |

---

## Completion Criteria

| Requirement | Status |
|---|---:|
| App chosen and justified against candidates | ✅ Complete (Umami - see [overview.md](overview.md)) |
| Compose service layout committed | ✅ Complete |
| `.env.example` committed; real `.env` gitignored | ✅ Complete |
| DNS record added in the live zone and validated | ⏳ Pending |
| Caddy route enabled and validated | ⏳ Pending |
| App deployed and reachable externally over HTTPS | ⏳ Pending |
| Admin account secured over a private path before exposure | ⏳ Pending |
| Backend/database ports confirmed not publicly reachable | ⏳ Pending |
| New hostname added as an Uptime Kuma monitor | ⏳ Pending |
| Redacted screenshots captured | ⏳ Pending |

---

# Screenshot Evidence

_Screenshots will be embedded here after execution._

## 01 - Stack Running, No Published Ports

## 02 - Admin Claimed Over SSH Tunnel

## 03 - Changed Credentials Sign-In

## 04 - Cloudflare DNS Record

## 05 - DNS Resolution (dig + DoH)

## 06 - HTTP 308 Redirect

## 07 - Valid Certificate Chain

## 08 - Security Headers

## 09 - Browser Padlock, Umami Dashboard

## 10 - Backend Ports Not Public

## 11 - Uptime Kuma Monitor Up

---

## Redaction Rules

| Sensitive Item | Handling |
|---|---|
| Public IPv4 address | Redacted |
| Public IPv6 address | Redacted or excluded |
| Tailscale IP | Redacted |
| Umami admin username | Redacted |
| Website IDs (`data-website-id`) | Redacted |
| ACME / account email | Redacted |
| SSH host fingerprints | Redacted where visible |
| Provider account data | Excluded |

---

## Validation Result

_To be completed after the Phase 4 run._
