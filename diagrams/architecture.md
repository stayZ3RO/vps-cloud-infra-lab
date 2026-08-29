# VPS Cloud Infra — Architecture Overview

One consolidated view of the target architecture. The phase diagrams
([phase 1](phase-1-vps-baseline-security.md),
[phase 2](phase-2-domain-dns-public-routing.md),
[phase 3](phase-3-reverse-proxy-https.md)) carry the detail.

```mermaid
flowchart TD
    USER["Internet user"]
    CF["Cloudflare — authoritative DNS for stayz3ro.dev"]
    PAGES["Cloudflare Pages — Astro blog<br/>stayz3ro.dev (apex) + www"]
    CADDY["Caddy on the VPS<br/>terminates TLS (Let's Encrypt) · routes by hostname<br/>only 80/443 public · JSON access logs"]
    VPS["Netcup VPS 1000 G12 — Debian · netcup-prod-01<br/>SSH keys only · UFW · fail2ban · unattended-upgrades"]
    SVCS["public services at subdomains<br/>e.g. status.stayz3ro.dev"]
    ADMIN["admin workstation"]

    USER --> CF
    CF -->|apex + www| PAGES
    CF -->|"service subdomains"| CADDY
    CADDY --> VPS --> SVCS
    ADMIN -.->|Tailscale| VPS
    USER -. "public SSH: blocked" .-x VPS

    classDef ext fill:#334155,stroke:#94a3b8,color:#f1f5f9
    classDef edge fill:#075985,stroke:#38bdf8,color:#e0f2fe
    classDef host fill:#92400e,stroke:#fbbf24,color:#fef3c7
    classDef svc fill:#166534,stroke:#4ade80,color:#dcfce7
    class USER,ADMIN ext
    class CF,PAGES,CADDY edge
    class VPS host
    class SVCS svc
```

**`stayz3ro.dev` DNS is Cloudflare-authoritative** (Porkbun registrar only).
The **apex + `www` serve the Astro blog** from Cloudflare Pages. **Service
subdomains** (e.g. `status.stayz3ro.dev`) resolve to the VPS, where **Caddy**
terminates TLS and routes by hostname — exactly the ports 80/443 are public,
everything else is Tailscale-only. Backend app containers stay on an internal
Docker network and are never published directly.
