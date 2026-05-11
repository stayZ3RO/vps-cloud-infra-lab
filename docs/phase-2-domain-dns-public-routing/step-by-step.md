# Phase 2 - Step-by-Step Guide 🛠️

![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Scope](https://img.shields.io/badge/scope-DNS%20%2B%20Public%20Routing-blue)
![SSH](https://img.shields.io/badge/ssh-Tailscale%20Only-success)

## Purpose

This guide documents the Phase 2 implementation flow for DNS routing and Tailscale-only SSH access.

---

## Implementation Flow

| Step | Task | Status |
|---|---|---:|
| 1 | Remove Porkbun parking records | ✅ Complete |
| 2 | Add root domain A record | ✅ Complete |
| 3 | Add www CNAME record | ✅ Complete |
| 4 | Add planned service subdomains | ✅ Complete |
| 5 | Validate local DNS resolution | ✅ Complete |
| 6 | Validate public DNS resolvers | ✅ Complete |
| 7 | Confirm SSH listening state | ✅ Complete |
| 8 | Confirm Tailscale SSH works | ✅ Complete |
| 9 | Remove public SSH rules | ✅ Complete |
| 10 | Validate public SSH is blocked | ✅ Complete |
| 11 | Capture redacted screenshots | ✅ Complete |

---

## Step 1 - Remove Default Porkbun Parking Records

The default Porkbun parking records were removed.

Removed records:

    ALIAS   stayz3ro.dev       pixie.porkbun.com
    CNAME   *.stayz3ro.dev     pixie.porkbun.com

Why this matters:

- Prevents the domain from pointing to Porkbun parking
- Removes wildcard behavior that could mask future subdomain testing
- Creates a clean DNS foundation

---

## Step 2 - Add Root Domain Record

The root domain was pointed to the Netcup VPS.

Record:

| Type | Host | Purpose |
|---|---|---|
| A | @ | Root domain to Netcup VPS |

---

## Step 3 - Add WWW Record

The `www` subdomain was configured as a CNAME to the root domain.

Record:

| Type | Host | Value |
|---|---|---|
| CNAME | www | stayz3ro.dev |

---

## Step 4 - Add Planned Service Subdomains

The following service subdomains were added for future use:

| Type | Host | Purpose |
|---|---|---|
| A | apps | Future public app entry point |
| A | status | Future status page |
| A | api | Future API services |

---

## Step 5 - Validate Local DNS Resolution

Local DNS resolution was validated with `dig`.

Commands:

    dig +short stayz3ro.dev
    dig +short www.stayz3ro.dev
    dig +short apps.stayz3ro.dev
    dig +short status.stayz3ro.dev
    dig +short api.stayz3ro.dev

Expected result:

- Root domain resolves to Netcup VPS
- `www` resolves through the root domain
- Planned subdomains resolve to Netcup VPS

---

## Step 6 - Validate Public Resolvers

Public resolver validation was performed using Cloudflare and Google DNS.

Commands:

    dig @1.1.1.1 +short stayz3ro.dev
    dig @8.8.8.8 +short stayz3ro.dev
    dig @1.1.1.1 +short apps.stayz3ro.dev
    dig @8.8.8.8 +short apps.stayz3ro.dev

Why this matters:

- Confirms DNS records are visible outside the local network
- Validates public propagation
- Confirms the domain is ready for reverse proxy and HTTPS

---

## Step 7 - Confirm SSH Listening State

SSH listening state was reviewed.

Command:

    sudo ss -tulpen | grep ssh

Result:

- SSH is listening on port 22
- SSH service is available for private Tailscale access

---

## Step 8 - Confirm Tailscale SSH Works

SSH access over Tailscale was tested from the admin workstation.

Command:

    ssh ash@TAILSCALE_VPS_IP

Expected result:

    Login succeeds

---

## Step 9 - Remove Public SSH Rules

Public SSH firewall rules were removed from UFW.

The final access model allows SSH only on the Tailscale interface while keeping HTTP and HTTPS public.

Expected final firewall posture:

| Rule | Purpose |
|---|---|
| 22/tcp on tailscale0 | Private SSH administration |
| 80/tcp | Public HTTP for future reverse proxy |
| 443/tcp | Public HTTPS for future reverse proxy |

---

## Step 10 - Validate Public SSH Is Blocked

Public SSH access was tested from the admin workstation.

Command:

    ssh -o ConnectTimeout=5 ash@PUBLIC_VPS_IP

Expected result:

    Connection timed out

This confirms public SSH is blocked.

---

## Step 11 - Capture Screenshots

Screenshots were captured and redacted for:

| Screenshot | Purpose |
|---|---|
| DNS records | Confirms Porkbun configuration |
| Local DNS resolution | Confirms domain/subdomain lookups |
| Public resolver validation | Confirms public propagation |
| UFW before cleanup | Shows public SSH before hardening |
| SSH listening port | Confirms SSH service state |
| Tailscale SSH success | Confirms private admin access |
| Final UFW state | Confirms Tailscale-only SSH |
| Public SSH blocked | Confirms public SSH is no longer reachable |

---

## Phase Result

Phase 2 completed the public DNS foundation and improved the VPS management plane.

The domain is ready for reverse proxy and HTTPS setup, while SSH administration is restricted to Tailscale.
