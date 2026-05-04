# Phase 1 - VPS Baseline & Security Hardening 🔐

## Objective

Prepare the Netcup VPS as a secure, production-ready Linux server before configuring domain DNS, reverse proxying, HTTPS, or public application hosting.

This phase establishes the baseline controls needed before exposing services to the public internet.

---

## Server Role

| Item | Value |
|---|---|
| Provider | Netcup |
| Hostname | `netcup-prod-01` |
| Role | Primary production/public services VPS |
| Operating System | Ubuntu Linux |
| Primary Admin User | Non-root sudo user |
| Public Domain | `stayz3ro.dev` planned |
| Private Access | Tailscale |

---

## Completed Tasks

### System Baseline

- Confirmed hostname configuration
- Confirmed operating system version
- Updated system packages
- Installed baseline administration tools
- Set system timezone
- Added swap for stability

### User and Access Management

- Created non-root sudo user
- Confirmed sudo group membership
- Confirmed sudo access
- Disabled root SSH login
- Disabled password-based SSH login
- Confirmed SSH key-based access

### SSH Hardening

- Confirmed SSH service is active
- Validated SSH configuration syntax
- Reloaded SSH safely
- Tested access from a second terminal session

### Firewall

- Enabled UFW
- Set default deny for incoming traffic
- Set default allow for outgoing traffic
- Allowed SSH
- Allowed HTTP
- Allowed HTTPS
- Verified firewall rules

### Intrusion Protection

- Installed Fail2Ban
- Enabled SSH jail
- Configured retry limits
- Verified Fail2Ban status

### Updates

- Enabled unattended upgrades
- Verified unattended upgrade service

### Container Runtime

- Installed Docker
- Installed Docker Compose
- Verified Docker functionality

### Private Administration

- Installed Tailscale
- Connected VPS to private tailnet
- Verified Tailscale status

### Filesystem Organization

Created the following VPS directory structure:

    /opt/stayz3ro
    ├── apps
    ├── backups
    ├── monitoring
    ├── proxy
    └── scripts

---

## Validation Evidence

| Evidence | Screenshot |
|---|---|
| Netcup VPS dashboard | `screenshots/01-netcup-vps-dashboard-redacted.png` |
| Hostname validation | `screenshots/02-hostnamectl.png` |
| OS version | `screenshots/03-os-version.png` |
| Sudo user validation | `screenshots/04-sudo-user-groups.png` |
| SSH service status | `screenshots/05-ssh-service-status.png` |
| SSH config validation | `screenshots/06-ssh-config-validation.png` |
| UFW firewall status | `screenshots/07-ufw-firewall-status.png` |
| Fail2Ban status | `screenshots/08-fail2ban-status.png` |
| Unattended upgrades | `screenshots/09-unattended-upgrades-status.png` |
| Swap and memory check | `screenshots/10-swap-memory-check.png` |
| Docker validation | `screenshots/11-docker-version.png` |
| Tailscale status | `screenshots/12-tailscale-status-redacted.png` |
| VPS folder structure | `screenshots/13-folder-structure.png` |
| Listening ports | `screenshots/14-listening-ports-redacted.png` |

---

## Commands Used for Validation

    hostnamectl
    cat /etc/os-release
    groups ash
    sudo whoami
    sudo systemctl status ssh --no-pager
    sudo sshd -t && echo "SSH config validation passed"
    sudo ufw status verbose
    sudo fail2ban-client status sshd
    systemctl status unattended-upgrades --no-pager
    free -h
    docker version
    docker compose version
    tailscale status
    tree /opt/stayz3ro
    sudo ss -tulpen | grep LISTEN

---

## Security Decisions

| Decision | Reason |
|---|---|
| Disabled root SSH login | Reduces risk from direct root brute-force attempts |
| Disabled password SSH login | Requires SSH key authentication |
| Enabled UFW | Limits exposed network services |
| Allowed only SSH, HTTP, HTTPS | Keeps the attack surface small |
| Enabled Fail2Ban | Adds brute-force protection for SSH |
| Used Tailscale | Provides private admin access without exposing dashboards |
| Avoided public Portainer exposure | Prevents exposing privileged container management to the internet |

---

## Redaction Rules

The following data is redacted from screenshots before being committed:

- Public IPv4 address
- IPv6 address
- Tailscale IPs
- Tailscale device identifiers where needed
- Netcup customer/account details
- Email addresses
- Authentication URLs
- API keys or tokens
- Billing details

---

## Phase 1 Completion Criteria

Phase 1 is complete because:

- Hostname resolves correctly with no sudo warning
- Non-root sudo user works
- SSH service is active
- SSH config validates successfully
- Root SSH login is disabled
- Password SSH login is disabled
- UFW is enabled
- Only SSH, HTTP, and HTTPS are allowed
- Fail2Ban is active for SSH
- Unattended upgrades are enabled
- Docker and Docker Compose work
- Tailscale is installed and connected
- `/opt/stayz3ro` folder structure exists
- Listening ports are understood and documented

---

## Next Phase

Next: **Phase 2 - Domain DNS & Public Routing**

The next phase will connect the `stayz3ro.dev` domain to the VPS and establish public DNS records before deploying the reverse proxy and HTTPS certificates.
