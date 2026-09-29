# Phase 5 - Monitoring & Alerts 🔔

![Status](https://img.shields.io/badge/status-packet%20ready-blue)
![Service](https://img.shields.io/badge/service-Uptime%20Kuma-orange)
![Scope](https://img.shields.io/badge/scope-public%20edge-purple)

## Phase Summary

Phase 5 makes the public edge observable. Uptime Kuma is deployed on
`netcup-prod-01` and reachable at `https://status.stayz3ro.dev`. As of
2026-09-28 it monitors the public sites, the HTTPS edge, and public DNS for
`stayz3ro.dev` and `chrisalorenzo.com`, with certificate-expiry notices, and
sends alerts to a dedicated Discord provider and to a self-hosted ntfy server
on the same VPS (`ntfy.chrisalorenzo.com`).

The design rule for the phase is narrow: monitor only what is public, from
outside the LAN. Nothing in this phase monitors a private or admin endpoint,
and nothing opens a path from the VPS into the home LAN.

---

## What This Phase Demonstrates

| Area | Demonstrated Skill |
|---|---|
| External monitoring | Availability checks from a separate failure domain than the services |
| Alert design | Severity expressed through provider choice, retries, and resend intervals |
| Secret handling | Provider credentials entered only in the service UI, never in Git |
| Failure-domain reasoning | Separating external public-edge alerts from internal infrastructure alerts |
| Validation | A real, reversible DOWN/UP test instead of trusting a test button |

---

## Documentation

| Page | Description |
|---|---|
| [Alert Wiring Execution Packet](alert-wiring-execution-packet.md) | Ready-to-run steps for providers, monitors, testing, and rollback |

---

## Scope

In scope:

- ntfy and Discord notification providers in Uptime Kuma
- HTTP(s), TCP port, and DNS monitors for public hostnames
- TLS certificate expiry warning on the public HTTP monitors
- a reversible DOWN/UP notification test
- a written record of the final wiring, without secrets

Out of scope:

- any private, admin, or LAN endpoint monitor
- an inbound path from the VPS into the LAN
- heartbeat (Push) monitors and the Caddy access-log prerequisite
- changes to the LAN-side monitoring and alerting stack
- a public status page and an independent offsite dead-man monitor

---

## Completion Criteria

| Requirement | Status |
|---|---:|
| Execution packet written and reviewed read-only | ✅ Complete |
| ntfy provider configured and test received | ✅ Complete |
| Discord provider configured and test received | ✅ Complete |
| Public-edge monitors created | ✅ Complete |
| Certificate expiry warning enabled | ✅ Complete |
| Real DOWN and UP notification proven | ✅ Complete |
| Final wiring recorded without secrets | ✅ Complete |
| Offsite dead-man monitor designed | ⏳ Separate packet |

The live wiring was done on 2026-09-28 and is recorded in the packet and
`CURRENT-STATUS.md`.
