# Phase 1 - Step-by-Step Guide

## Objective

Configure the Netcup VPS as a secure baseline Linux server before domain DNS, reverse proxy, HTTPS, or application hosting.

---

## Step 1 - System Baseline

Commands used:

    sudo apt update
    sudo apt upgrade -y
    sudo apt install -y curl wget git nano htop ufw fail2ban unzip ca-certificates gnupg lsb-release tree

Validation:

    cat /etc/os-release
    hostnamectl

---

## Step 2 - Hostname Configuration

Hostname used:

    netcup-prod-01

Validation:

    hostname
    hostnamectl
    cat /etc/hosts

---

## Step 3 - Non-Root Sudo User

Validation:

    groups ash
    sudo whoami

Expected result:

    root

---

## Step 4 - SSH Hardening

Configured SSH with:

    PermitRootLogin no
    PasswordAuthentication no
    PubkeyAuthentication yes

Validation:

    sudo systemctl status ssh --no-pager
    sudo sshd -t && echo "SSH config validation passed"

SSH was reloaded safely after validation:

    sudo systemctl reload ssh

---

## Step 5 - Firewall Configuration

UFW baseline:

    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    sudo ufw allow OpenSSH
    sudo ufw allow 80/tcp
    sudo ufw allow 443/tcp
    sudo ufw enable

Validation:

    sudo ufw status verbose

---

## Step 6 - Fail2Ban

Fail2Ban was enabled for SSH brute-force protection.

Validation:

    sudo fail2ban-client status sshd

---

## Step 7 - Unattended Upgrades

Automatic security updates were enabled.

Validation:

    systemctl status unattended-upgrades --no-pager

---

## Step 8 - Swap

Swap was configured for stability on a small VPS.

Validation:

    free -h

---

## Step 9 - Docker

Docker and Docker Compose were installed.

Validation:

    docker version
    docker compose version

---

## Step 10 - Tailscale

Tailscale was installed for private administrative access.

Validation:

    tailscale status

---

## Step 11 - VPS Folder Structure

Created:

    /opt/stayz3ro
    ├── apps
    ├── backups
    ├── monitoring
    ├── proxy
    └── scripts

Validation:

    tree /opt/stayz3ro

---

## Step 12 - Listening Ports

Reviewed listening services with:

    sudo ss -tulpen | grep LISTEN

Only expected services should be listening before deploying public apps.
