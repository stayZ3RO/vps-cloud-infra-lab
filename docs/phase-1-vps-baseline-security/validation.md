# Phase 1 - Validation Evidence

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
- `/opt/stayz3ro` folder structure exists
- Listening ports are understood and documented

---

## Screenshot Evidence

### 02 - Hostname Validation

![Hostname validation](../../screenshots/phase-1-vps-baseline-security/02-hostnamectl.png)

---

### 03 - OS Version

![OS version](../../screenshots/phase-1-vps-baseline-security/03-os-version.png)

---

### 05 - SSH Service Status

![SSH service status](../../screenshots/phase-1-vps-baseline-security/05-ssh-service-status.png)

---

### 06 - SSH Config Validation

![SSH config validation](../../screenshots/phase-1-vps-baseline-security/06-ssh-config-validation.png)

---

### 07 - UFW Firewall Status

![UFW firewall status](../../screenshots/phase-1-vps-baseline-security/07-ufw-firewall-status.png)

---

### 08 - Fail2Ban Status

![Fail2Ban status](../../screenshots/phase-1-vps-baseline-security/08-fail2ban-status.png)

---

### 09 - Unattended Upgrades

![Unattended upgrades](../../screenshots/phase-1-vps-baseline-security/09-unattended-upgrades-status.png)

---

### 10 - Swap and Memory Check

![Swap and memory check](../../screenshots/phase-1-vps-baseline-security/10-swap-memory-check.png)

---

### 11 - Docker Validation

![Docker validation](../../screenshots/phase-1-vps-baseline-security/11-docker-version.png)

---

### 12 - Tailscale Status

![Tailscale status](../../screenshots/phase-1-vps-baseline-security/12-tailscale-status-redacted.png)

---

### 13 - VPS Folder Structure

![VPS folder structure](../../screenshots/phase-1-vps-baseline-security/13-folder-structure.png)

---

### 14 - Listening Ports

![Listening ports](../../screenshots/phase-1-vps-baseline-security/14-listening-ports-redacted.png)

---

## Optional Evidence Not Included

The following evidence was either omitted or can be added later:

- Netcup VPS dashboard screenshot
- Sudo user group validation screenshot

The Netcup dashboard contains provider/account details and should only be included if fully redacted.

---

## Redaction Rules

The following information was redacted before committing screenshots:

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

## Validation Summary

This phase confirms the VPS has a secure baseline before public application hosting begins.

The server is ready for the next phase: **Domain DNS & Public Routing**.
