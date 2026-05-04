# Phase 1 - Validation Evidence

## Purpose

This page documents the validation evidence for Phase 1: VPS Baseline & Security Hardening.

The goal is to prove that the VPS was not only configured, but also verified through command output and screenshots.

---

## Completion Criteria

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
- /opt/stayz3ro folder structure exists
- Listening ports are understood and documented

---

## Screenshot Evidence

### 02 - Hostname Validation

Confirms the VPS hostname is configured cleanly.

![Hostname validation](../../screenshots/phase-1-vps-baseline-security/02-hostnamectl.png)

---

### 03 - OS Version

Documents the Ubuntu Linux version used for the VPS baseline.

![OS version](../../screenshots/phase-1-vps-baseline-security/03-os-version.png)

---

### 05 - SSH Service Status

Confirms the SSH service is active and running.

![SSH service status](../../screenshots/phase-1-vps-baseline-security/05-ssh-service-status.png)

---

### 06 - SSH Config Validation

Confirms the SSH configuration syntax passed validation.

![SSH config validation](../../screenshots/phase-1-vps-baseline-security/06-ssh-config-validation.png)

---

### 07 - UFW Firewall Status

Confirms UFW is enabled and only the intended baseline ports are allowed.

![UFW firewall status](../../screenshots/phase-1-vps-baseline-security/07-ufw-firewall-status.png)

---

### 08 - Fail2Ban Status

Confirms Fail2Ban is active for SSH protection.

![Fail2Ban status](../../screenshots/phase-1-vps-baseline-security/08-fail2ban-status.png)

---

### 09 - Unattended Upgrades

Confirms unattended upgrades are enabled for automatic security updates.

![Unattended upgrades](../../screenshots/phase-1-vps-baseline-security/09-unattended-upgrades-status.png)

---

### 10 - Swap and Memory Check

Confirms system memory and swap status after baseline configuration.

![Swap and memory check](../../screenshots/phase-1-vps-baseline-security/10-swap-memory-check.png)

---

### 11 - Docker Validation

Confirms Docker and Docker Compose are installed and available.

![Docker validation](../../screenshots/phase-1-vps-baseline-security/11-docker-version.png)

---

### 12 - Tailscale Status

Confirms the VPS is connected to Tailscale for private administrative access.

![Tailscale status](../../screenshots/phase-1-vps-baseline-security/12-tailscale-status-redacted.png)

---

### 13 - VPS Folder Structure

Confirms the /opt/stayz3ro folder structure was created for future services.

![VPS folder structure](../../screenshots/phase-1-vps-baseline-security/13-folder-structure.png)

---

### 14 - Listening Ports

Confirms listening services were reviewed before public app deployment.

![Listening ports](../../screenshots/phase-1-vps-baseline-security/14-listening-ports-redacted.png)

---

## Optional Evidence Not Included

The following evidence can be added later if needed:

| Evidence | Reason |
|---|---|
| Netcup VPS dashboard | Omitted to avoid exposing provider/account details |
| Sudo user group screenshot | Verified during setup but not included in this screenshot set |

---

## Redaction Rules

The following information was redacted or excluded before committing screenshots:

- Public IPv4 address
- IPv6 address
- Tailscale IPs
- Tailscale device identifiers where needed
- Netcup customer/account details
- Email addresses
- Authentication URLs
- API keys or tokens
- Billing details
- SSH keys
- Private credentials

---

## Validation Summary

This phase confirms the VPS has a secure baseline before public application hosting begins.

The server is ready for the next phase:

**Phase 2 - Domain DNS & Public Routing**
