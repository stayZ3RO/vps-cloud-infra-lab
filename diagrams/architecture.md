# VPS Cloud Infra — Architecture Overview

A single consolidated view of the current state. The phase diagrams
([phase 1](phase-1-vps-baseline-security.md),
[phase 2](phase-2-domain-dns-public-routing.md)) carry the detail.

```mermaid
flowchart TD
    USER["Internet user"]
    DNS["Porkbun DNS — stayz3ro.dev<br/>A / CNAME records → VPS public IP"]
    UFW["UFW firewall<br/>80 / 443 public · SSH = Tailscale only"]
    VPS["Netcup VPS 1000 G12 — Debian · netcup-prod-01<br/>SSH keys only · fail2ban · unattended-upgrades"]
    DOCKER["Docker + Docker Compose<br/>/opt/stayz3ro"]
    SVCS["containerized services"]
    ADMIN["admin workstation"]

    USER --> DNS --> UFW --> VPS --> DOCKER --> SVCS
    ADMIN -.->|Tailscale| VPS
    USER -. "public SSH: blocked" .-x VPS

    CF["Cloudflare — DNS · proxy / CDN · TLS"]:::planned
    PROXY["reverse proxy + HTTPS<br/>domain-based routing"]:::planned
    CF -. planned .- DNS
    PROXY -. planned .- DOCKER

    classDef ext fill:#334155,stroke:#94a3b8,color:#f1f5f9
    classDef edge fill:#075985,stroke:#38bdf8,color:#e0f2fe
    classDef host fill:#92400e,stroke:#fbbf24,color:#fef3c7
    classDef svc fill:#166534,stroke:#4ade80,color:#dcfce7
    classDef planned fill:#1e1b4b,stroke:#818cf8,color:#e0e7ff,stroke-dasharray:4 3
    class USER,ADMIN ext
    class DNS,UFW edge
    class VPS host
    class DOCKER,SVCS svc
```

**Current:** `stayz3ro.dev` DNS is on **Porkbun**, records point straight at
the VPS public IP; UFW exposes only 80/443, SSH is Tailscale-only, public
SSH is blocked.
**Planned (dashed):** move DNS to Cloudflare (proxy/CDN/TLS) and add a
reverse proxy for HTTPS and domain-based service routing — the portfolio
domain `chrisalorenzo.com` already runs the Cloudflare model.
