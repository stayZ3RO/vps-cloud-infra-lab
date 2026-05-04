# Lessons Learned

This file documents the operational lessons, troubleshooting notes, and infrastructure decisions made during the VPS Cloud Infrastructure Lab.

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

The final SSH posture for this phase:

| Setting | Value |
|---|---|
| Root SSH login | Disabled |
| Password SSH login | Disabled |
| Public key authentication | Enabled |
| Non-root sudo user | Enabled |

This reduces the risk of brute-force access and removes direct root login from the public internet.

---

## Hostname Resolution Matters

After changing the hostname, the server should also have a matching local hosts entry.

Without that, sudo can show a warning like:

    sudo: unable to resolve host netcup-prod-01

The fix was to ensure the hostname was reflected in /etc/hosts.

This was a useful reminder that clean Linux administration includes both visible hostname configuration and local name resolution.

---

## Public Exposure Should Start Small

A new VPS should not expose application ports directly.

For the baseline phase, only these public services are expected:

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

The initial policy is:

| Direction | Policy |
|---|---|
| Incoming | Deny by default |
| Outgoing | Allow by default |

Allowed public traffic:

- SSH
- HTTP
- HTTPS

This creates a small and understandable exposure model before the VPS hosts public workloads.

---

## Fail2Ban Adds Useful SSH Protection

Fail2Ban does not replace SSH key authentication or firewalling, but it adds another useful layer.

For this phase, Fail2Ban was configured to monitor SSH authentication attempts and temporarily ban repeated failures.

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

The main design decision: public services should use HTTPS through a reverse proxy, while admin services should stay private whenever possible.

---

## Screenshots Are Validation Evidence

Screenshots are not just decoration.

They prove that the implementation was completed and tested.

Useful validation evidence includes:

- Hostname validation
- OS version
- SSH service status
- SSH config validation
- UFW firewall rules
- Fail2Ban status
- Unattended upgrades
- Docker version
- Tailscale status
- Folder structure
- Listening ports

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
- Billing details

A clean repo should demonstrate infrastructure skills without exposing operational secrets.

---

## Main Takeaway

Phase 1 did not deploy a public app yet, but it established the foundation required to safely host one.

The important lesson:

**Public infrastructure should be hardened before it is useful.**
