# Phase 1 - Step-by-Step Guide

## Objective

Configure the Netcup VPS as a secure baseline Linux server before domain DNS, reverse proxy, HTTPS, or application hosting.

This guide documents the implementation flow used for Phase 1.

---

## Step 1 - Confirm Server Access

Initial administrative access was established over SSH.

The VPS was accessed first with provider credentials, then moved toward a safer non-root administrative model.

Validation goal:

- Confirm SSH access works
- Confirm the server is reachable
- Confirm commands can be run as an administrator

---

## Step 2 - Update the Operating System

The system package index and installed packages were updated.

Commands used:

    sudo apt update
    sudo apt upgrade -y

Baseline tools were installed:

    sudo apt install -y curl wget git nano htop ufw fail2ban unzip ca-certificates gnupg lsb-release tree

Why this matters:

- Ensures the VPS starts from a patched baseline
- Adds tools needed for administration, validation, and documentation
- Prepares the system for Docker, security tooling, and future services

---

## Step 3 - Configure Hostname

Hostname used:

    netcup-prod-01

Validation commands:

    hostname
    hostnamectl

The local hosts file was also checked to prevent sudo hostname resolution warnings.

Validation command:

    cat /etc/hosts

Expected result:

- Hostname displays correctly
- Sudo commands run without hostname resolution warnings

---

## Step 4 - Confirm Non-Root Sudo User

A non-root administrative user was configured for daily management.

Validation commands:

    groups ash
    sudo whoami

Expected sudo result:

    root

Why this matters:

- Avoids daily administration as root
- Supports disabling direct root SSH login
- Creates a safer operational model

---

## Step 5 - Harden SSH

SSH was configured for key-based access and reduced risk.

Target SSH settings:

    PermitRootLogin no
    PasswordAuthentication no
    PubkeyAuthentication yes

Validation commands:

    sudo systemctl status ssh --no-pager
    sudo sshd -t

For screenshot clarity:

    sudo sshd -t && echo "SSH config validation passed"

SSH was reloaded after validation:

    sudo systemctl reload ssh

Operational safety note:

A second terminal session was used to confirm SSH login still worked before closing the original session.

---

## Step 6 - Configure UFW Firewall

UFW was enabled with a minimal public exposure model.

Commands used:

    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    sudo ufw allow OpenSSH
    sudo ufw allow 80/tcp
    sudo ufw allow 443/tcp
    sudo ufw enable

Validation command:

    sudo ufw status verbose

Expected public exposure:

| Port | Purpose |
|---|---|
| SSH | Administrative access |
| HTTP | Web traffic and certificate validation |
| HTTPS | Secure public services |

---

## Step 7 - Enable Fail2Ban

Fail2Ban was installed and configured for SSH brute-force protection.

Example SSH jail configuration:

    [sshd]
    enabled = true
    port = ssh
    maxretry = 5
    bantime = 1h
    findtime = 10m

Service commands:

    sudo systemctl restart fail2ban
    sudo systemctl enable fail2ban

Validation commands:

    sudo fail2ban-client status
    sudo fail2ban-client status sshd

Why this matters:

- Public VPS servers receive automated SSH login attempts
- Fail2Ban adds an additional defensive layer
- Repeated failed authentication attempts can be temporarily banned

---

## Step 8 - Enable Unattended Security Updates

Unattended upgrades were enabled for automatic security patching.

Commands used:

    sudo apt install -y unattended-upgrades
    sudo dpkg-reconfigure --priority=low unattended-upgrades

Validation command:

    systemctl status unattended-upgrades --no-pager

Why this matters:

- Helps keep security updates applied
- Reduces risk from unpatched packages
- Supports a more production-minded baseline

---

## Step 9 - Configure Timezone

Timezone was set to Eastern time.

Command used:

    sudo timedatectl set-timezone America/New_York

Validation command:

    timedatectl

---

## Step 10 - Add Swap

Swap was added to improve stability on a small VPS.

Validation command before and after:

    free -h

Example swap creation commands:

    sudo fallocate -l 2G /swapfile
    sudo chmod 600 /swapfile
    sudo mkswap /swapfile
    sudo swapon /swapfile

Persistence entry:

    echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

Why this matters:

- Helps reduce risk of process crashes under memory pressure
- Provides a small safety buffer for lightweight services
- Useful for smaller VPS plans

---

## Step 11 - Install Docker and Docker Compose

Docker was installed as the container runtime for future services.

Install command:

    curl -fsSL https://get.docker.com | sudo sh

The admin user was added to the Docker group:

    sudo usermod -aG docker ash

Group membership was refreshed:

    newgrp docker

Validation commands:

    docker version
    docker compose version
    docker run hello-world

Why this matters:

- Prepares the VPS for containerized application hosting
- Supports future reverse proxy, apps, monitoring, and automation services
- Keeps deployment workflows repeatable through Docker Compose

---

## Step 12 - Install Tailscale

Tailscale was installed for private administrative access.

Install command:

    curl -fsSL https://tailscale.com/install.sh | sh

Authentication command:

    sudo tailscale up

Validation command:

    tailscale status

Why this matters:

- Supports private access to admin tools
- Reduces need to expose dashboards publicly
- Provides a secure management path for future internal services

---

## Step 13 - Create VPS Folder Structure

A clean service layout was created under /opt/stayz3ro.

Commands used:

    sudo mkdir -p /opt/stayz3ro/{proxy,apps,monitoring,backups,scripts}
    sudo chown -R ash:ash /opt/stayz3ro

Validation command:

    tree /opt/stayz3ro

Expected structure:

    /opt/stayz3ro
    ├── apps
    ├── backups
    ├── monitoring
    ├── proxy
    └── scripts

Why this matters:

- Keeps future services organized
- Separates apps, proxy, monitoring, backups, and scripts
- Makes the VPS easier to maintain and document

---

## Step 14 - Review Listening Ports

Listening services were reviewed before deploying public apps.

Validation command:

    sudo ss -tulpen | grep LISTEN

Why this matters:

- Confirms what services are listening
- Helps identify accidental exposure
- Creates a clean baseline before reverse proxy and app deployment

---

## Phase 1 Result

At the end of this phase, the VPS has a hardened and validated baseline.

The server is ready for:

- Domain DNS configuration
- Reverse proxy deployment
- HTTPS setup
- Docker application hosting
- Monitoring and backup planning
