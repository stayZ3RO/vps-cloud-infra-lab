# Docker Configs 🐳

This folder will store sanitized Docker and Docker Compose examples used throughout the VPS Cloud Infrastructure Lab.

No production secrets, private keys, live environment files, API tokens, or database credentials should be committed.

---

## Current State

Docker and Docker Compose were installed during Phase 1.

No production Docker Compose stacks are stored in this folder yet.

---

## Planned Future Configs

This folder may eventually include examples for:

| Config | Purpose |
|---|---|
| reverse-proxy.compose.example.yml | Reverse proxy stack |
| app-template.compose.example.yml | Standard app deployment template |
| monitoring-agent.compose.example.yml | Lightweight monitoring agent |
| backup-job.compose.example.yml | Backup container or scheduled job |
| .env.example | Safe environment variable template |

---

## Docker Security Notes

Future Docker configs should follow these rules:

- Do not expose app ports directly unless required
- Route public services through the reverse proxy
- Keep databases on internal Docker networks
- Use named volumes intentionally
- Avoid committing real .env files
- Use .env.example for documentation
- Keep admin tools private through Tailscale where possible

---

## Validation Commands

Useful Docker validation commands:

    docker version
    docker compose version
    docker ps
    docker network ls
    docker volume ls

---

## Planned Deployment Pattern

Future services should generally follow this pattern:

    /opt/stayz3ro
    ├── proxy
    │   └── reverse proxy stack
    ├── apps
    │   └── public or private apps
    ├── monitoring
    │   └── service checks and agents
    ├── backups
    │   └── backup scripts and targets
    └── scripts
        └── maintenance automation
