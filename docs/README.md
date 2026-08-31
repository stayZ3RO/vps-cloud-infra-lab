# Documentation Hub 📚

This folder contains the phase-based documentation for the VPS Cloud Infrastructure Lab.

Each phase is organized like a small infrastructure case study:

- What was built
- Why it matters
- How it was implemented
- How it was validated
- What screenshots or evidence support the work
- What comes next

---

## Phase Index

| Phase | Status | Documentation |
|---|---:|---|
| Phase 1 - VPS Baseline & Security Hardening | ✅ Complete | [View Phase 1](phase-1-vps-baseline-security/) |
| Phase 2 - Domain DNS & Public Routing | ✅ Complete | [View Phase 2](phase-2-domain-dns-public-routing/) |
| Phase 3 - Reverse Proxy & HTTPS | ✅ Complete | [View Phase 3](phase-3-reverse-proxy-https/) |
| Phase 4 - Docker App Deployment | 🚧 In Progress | [View Phase 4](phase-4-docker-app-deployment/) |
| Phase 5 - Monitoring & Alerts | ⏳ Planned | Coming soon |
| Phase 6 - Backups & Disaster Recovery | ⏳ Planned | Coming soon |
| Phase 7 - Secondary VPS / Staging | ⏳ Planned | Coming soon |
| Phase 8 - AI Agent / Homelab Ops Bot | ⏳ Planned | Coming soon |

---

## Current Focus

The current phase is:

**Phase 4 - Docker App Deployment**

App selected: **Umami** (privacy-first web analytics) at
`analytics.stayz3ro.dev`. Scoping, compose stack, and runbook are staged;
deployment is pending. See
[phase-4-docker-app-deployment/](phase-4-docker-app-deployment/).

---

## Documentation Style

Each completed phase should include:

| File | Purpose |
|---|---|
| `README.md` | Phase landing page |
| `overview.md` | Case-study style summary |
| `step-by-step.md` | Implementation guide |
| `validation.md` | Evidence, screenshots, and verification |
| Diagram file | Architecture or flow documentation |
| Screenshot folder | Redacted proof of implementation |

---

## Related Project Files

| File | Purpose |
|---|---|
| [Current Status](../CURRENT-STATUS.md) | Current state of the project |
| [Roadmap](../ROADMAP.md) | Planned buildout |
| [Lessons Learned](../LESSONS-LEARNED.md) | Operational notes and takeaways |
| [Changelog](../CHANGELOG.md) | Major documentation and infrastructure updates |
