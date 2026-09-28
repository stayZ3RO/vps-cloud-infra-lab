# Phase 5 - Monitoring & Alerts 🔔

![Status](https://img.shields.io/badge/status-packet%20ready-blue)
![Service](https://img.shields.io/badge/service-Uptime%20Kuma-orange)
![Scope](https://img.shields.io/badge/scope-public%20edge-purple)

## Phase Summary

Phase 5 makes the public edge observable. Uptime Kuma is already deployed on
`netcup-prod-01` and reachable at `https://status.stayz3ro.dev`, but it has no
monitors and no notification providers. This phase adds public-edge
availability, DNS, and certificate-expiry monitoring, with ntfy for actionable
push and Discord for history.

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
| ntfy provider configured and test received | ⏳ To run |
| Discord provider configured and test received | ⏳ To run |
| Public-edge monitors created | ⏳ To run |
| Certificate expiry warning enabled | ⏳ To run |
| Real DOWN and UP notification proven | ⏳ To run |
| Final wiring recorded without secrets | ⏳ To run |
| Offsite dead-man monitor designed | ⏳ Separate packet |

The packet was prepared from read-only checks only. The live changes are run
by the owner, one stage at a time, and are not made by this repo.
