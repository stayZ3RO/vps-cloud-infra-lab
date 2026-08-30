# Phase 3 - Validation Evidence 📸

![Status](https://img.shields.io/badge/status-pending%20execution-yellow)
![Proxy](https://img.shields.io/badge/proxy-Caddy-blue)
![TLS](https://img.shields.io/badge/tls-Let's%20Encrypt-success)
![Domain](https://img.shields.io/badge/domain-stayz3ro.dev-purple)

## Purpose

This page will document validation evidence for Phase 3: Reverse Proxy &
HTTPS.

The goal is to confirm that `https://stayz3ro.dev` is publicly reachable with
a valid certificate, that HTTP redirects to HTTPS, that `www` redirects to the
apex, that security headers and structured logging are in place, and that no
backend ports are exposed publicly.

> This phase is scaffolded but not yet executed. The tables below are the
> checklist to fill in during the run described in
> [step-by-step.md](step-by-step.md).

---

## Validation Summary

| Area | Expected Result | Status |
|---|---|---|
| Caddy container | Running, ports 80/443/443-udp published | ⏳ Pending |
| Uptime Kuma container | Running, reachable only via Caddy on the `web` network | ⏳ Pending |
| Certificate | Issued by Let's Encrypt for `status.stayz3ro.dev` | ⏳ Pending |
| HTTP -> HTTPS | `http://status.stayz3ro.dev` returns 308 to HTTPS | ⏳ Pending |
| HTTPS | `https://status.stayz3ro.dev` returns 200, valid chain, Uptime Kuma UI | ⏳ Pending |
| Security headers | HSTS, nosniff, DENY, Referrer-Policy present | ⏳ Pending |
| Server header | Not advertised | ⏳ Pending |
| Access log | JSON entries in `configs/caddy/logs/access.log` | ⏳ Pending |
| Backend ports | 3000 / 8000 not reachable on the public IP | ⏳ Pending |

---

## Completion Criteria

| Requirement | Status |
|---|---:|
| Reverse proxy chosen and justified | ✅ Complete |
| Caddy stack committed | ✅ Complete |
| Uptime Kuma service defined in compose | ✅ Complete |
| Stack deployed on the VPS | ⏳ Pending |
| Certificate issued for `status.stayz3ro.dev` | ⏳ Pending |
| HTTP redirects to HTTPS | ⏳ Pending |
| External HTTPS validated (curl + browser) | ⏳ Pending |
| Security headers verified | ⏳ Pending |
| JSON access log confirmed | ⏳ Pending |
| Backend ports confirmed private | ⏳ Pending |
| Redacted screenshots captured | ⏳ Pending |

---

# Screenshot Evidence

_Screenshots will be embedded here after execution._

## 01 - Container Running

## 02 - Certificate Issuance (compose logs)

## 03 - HTTP 308 Redirect

## 04 - Valid Certificate Chain

## 05 - Browser Padlock, Uptime Kuma Loaded

## 07 - Security Headers

## 08 - JSON Access Log

## 09 - Backend Ports Not Public

---

## Redaction Rules

| Sensitive Item | Handling |
|---|---|
| Public IPv4 address | Redacted |
| Public IPv6 address | Redacted or excluded |
| Tailscale IP | Redacted |
| ACME / account email | Redacted |
| SSH host fingerprints | Redacted where visible |
| Provider account data | Excluded |

---

## Validation Result

_To be completed after the Phase 3 run._
