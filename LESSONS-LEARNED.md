# Lessons Learned 🧠

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Phase 1](https://img.shields.io/badge/phase_1-complete-success)
![Phase 2](https://img.shields.io/badge/phase_2-complete-success)
![Next](https://img.shields.io/badge/next-Reverse%20Proxy%20%26%20HTTPS-blue)

This file documents operational lessons, troubleshooting notes, and infrastructure design decisions from the VPS Cloud Infrastructure Lab.

---

## Current Project Takeaway

The first two phases established the foundation for a production-style public VPS environment:

| Phase | Outcome |
|---|---|
| Phase 1 - VPS Baseline & Security Hardening | Built a secure Linux server baseline |
| Phase 2 - Domain DNS & Public Routing | Connected `stayz3ro.dev` and restricted SSH to Tailscale |

The project is now ready for:

**Phase 3 - Reverse Proxy & HTTPS**

---

# Phase 1 - VPS Baseline & Security Hardening

## Secure the Server Before Hosting Anything

The first priority with a public VPS is not application deployment.

The first priority is:

- Access control
- Patch management
- SSH hardening
- Firewall rules
- Brute-force protection
- Listening port validation
- Documentation

Before adding Docker apps, domains, reverse proxy rules, or dashboards, the server needs a secure baseline.

This phase established that foundation.

---

## SSH Hardening Requires a Safe Workflow

SSH changes can lock you out if applied incorrectly.

The safe workflow is:

1. Keep the existing SSH session open
2. Validate the SSH config
3. Reload SSH instead of blindly restarting
4. Open a second terminal
5. Test login from the second terminal
6. Only then close the original session

Useful validation command:

    sudo sshd -t

If there is no output, the SSH configuration syntax is valid.

---

## Disable Risky Access After Validating Safe Access

Disabling root login and password login is good practice, but only after confirming key-based access works.

The final SSH posture for Phase 1:

| Setting | Value |
|---|---|
| Root SSH login | Disabled |
| Password SSH login | Disabled |
| Public key authentication | Enabled |
| Non-root sudo user | Enabled |

This reduced the risk of brute-force access and removed direct root login from the public internet.

---

## Hostname Resolution Matters

After changing the hostname, the server should also have a matching local hosts entry.

Without that, sudo can show a warning like:

    sudo: unable to resolve host netcup-prod-01

The fix was to ensure the hostname was reflected in `/etc/hosts`.

This was a useful reminder that clean Linux administration includes both visible hostname configuration and local name resolution.

---

## Public Exposure Should Start Small

A new VPS should not expose application ports directly.

For the baseline phase, only these public services were expected:

| Port | Purpose |
|---|---|
| SSH | Administrative access |
| HTTP | Web traffic and certificate validation |
| HTTPS | Secure public services |

Ports for applications, databases, Portainer, monitoring dashboards, and internal tools should not be directly exposed.

Those services should eventually sit behind a reverse proxy, Tailscale, or private network access.

---

## UFW Provides a Simple Baseline Firewall

UFW gives a straightforward host-level firewall baseline.

The initial policy was:

| Direction | Policy |
|---|---|
| Incoming | Deny by default |
| Outgoing | Allow by default |

Allowed public traffic during Phase 1:

- SSH
- HTTP
- HTTPS

This created a small and understandable exposure model before the VPS hosted public workloads.

---

## Fail2Ban Adds Useful SSH Protection

Fail2Ban does not replace SSH key authentication or firewalling, but it adds another useful layer.

For Phase 1, Fail2Ban was configured to monitor SSH authentication attempts and temporarily ban repeated failures.

This is especially useful on a public VPS where automated SSH scanning is expected.

---

## Tailscale Is Useful for Private Administration

Tailscale gives the VPS a private administrative access path.

This is useful for future services that should not be public, such as:

- Portainer
- Internal dashboards
- Monitoring tools
- Admin-only apps
- Private service checks

The main design decision:

**Public services should use HTTPS through a reverse proxy. Admin services should stay private whenever possible.**

---

# Phase 2 - Domain DNS & Public Routing

## DNS Should Be Treated as Infrastructure

Phase 2 showed that DNS is not just a domain setup step. It is part of the infrastructure design.

The domain records define how users, services, and future applications will reach the VPS.

Configured records:

| Record | Purpose |
|---|---|
| `stayz3ro.dev` | Root domain |
| `www.stayz3ro.dev` | Web alias |
| `apps.stayz3ro.dev` | Future public apps |
| `status.stayz3ro.dev` | Future status page |
| `api.stayz3ro.dev` | Future API services |

The lesson:

**DNS should be planned before deploying the reverse proxy.**

---

## Remove Default Parking Records First

Porkbun default parking records needed to be removed before the domain could point cleanly to the Netcup VPS.

Removed records:

    ALIAS   stayz3ro.dev       pixie.porkbun.com
    CNAME   *.stayz3ro.dev     pixie.porkbun.com

Keeping wildcard or parking records would make future validation confusing.

The lesson:

**Clean DNS records reduce troubleshooting noise.**

---

## Validate DNS Locally and Publicly

DNS was validated from the local workstation and from public resolvers.

Useful validation commands:

    dig +short stayz3ro.dev
    dig +short www.stayz3ro.dev
    dig +short apps.stayz3ro.dev
    dig +short status.stayz3ro.dev
    dig +short api.stayz3ro.dev

Public resolver checks:

    dig @1.1.1.1 +short stayz3ro.dev
    dig @8.8.8.8 +short stayz3ro.dev

The lesson:

**A DNS record is not complete until resolution is verified from more than one perspective.**

---

## Public DNS Does Not Mean Public Administration

Connecting a domain to a public VPS does not mean administrative services should be public.

During Phase 2, SSH was moved from public exposure to Tailscale-only access.

Final access model:

| Access Type | Result |
|---|---|
| SSH to public VPS IP | Blocked |
| SSH to Tailscale IP | Allowed |
| HTTP | Public for future reverse proxy |
| HTTPS | Public for future reverse proxy |
| Direct app ports | Blocked |
| Admin dashboards | Not publicly exposed |

The lesson:

**Public service traffic and administrative access should be separate paths.**

---

## Tailscale-Only SSH Better Matches Enterprise Access Patterns

Restricting SSH to Tailscale created a more enterprise-style management plane.

The model is similar to:

    Admin workstation
      ↓
    VPN / private access layer
      ↓
    Server management interface

In this lab:

    Admin workstation
      ↓
    Tailscale
      ↓
    Netcup VPS
      ↓
    SSH

The lesson:

**Administrative access should go through a private management path whenever possible.**

---

## Firewall Rules Should Match Actual Listening Services

During Phase 2, SSH was confirmed to be listening on port `22`.

That made unused `2222` firewall rules unnecessary.

The final firewall posture should be simple and intentional:

| Rule | Purpose |
|---|---|
| `22/tcp on tailscale0` | Private SSH administration |
| `80/tcp` | Public HTTP for future reverse proxy |
| `443/tcp` | Public HTTPS for future reverse proxy |

The lesson:

**Firewall rules should be reviewed after each change so stale rules do not remain.**

---

## Screenshots Are Validation Evidence

Screenshots are not just decoration.

They prove that the implementation was completed and tested.

Useful validation evidence includes:

- DNS records
- Local DNS resolution
- Public resolver checks
- SSH listening state
- Tailscale SSH success
- Final UFW rules
- Public SSH blocked

This makes the project stronger as a portfolio artifact because it shows both configuration and verification.

---

## Redaction Is Part of Documentation Quality

Public infrastructure documentation should not leak sensitive information.

Redacted or excluded items include:

- Public IPv4 addresses
- IPv6 addresses
- Tailscale IPs
- Provider account details
- Email addresses
- Authentication links
- Tokens
- Private keys
- SSH host fingerprints
- Billing details

A clean repo should demonstrate infrastructure skills without exposing operational secrets.

---

## Main Takeaway

Phase 1 made the VPS safe to manage.

Phase 2 made the VPS reachable through a real domain while keeping administration private.

The important lesson:

**Public infrastructure should expose services intentionally, but management access should stay private.**
