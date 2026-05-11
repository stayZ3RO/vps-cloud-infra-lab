# Phase 2 - Validation Evidence 📸

![Status](https://img.shields.io/badge/status-validated-brightgreen)
![DNS](https://img.shields.io/badge/dns-validated-blue)
![Domain](https://img.shields.io/badge/domain-stayz3ro.dev-purple)
![SSH](https://img.shields.io/badge/ssh-Tailscale%20Only-success)

## Purpose

This page documents validation evidence for Phase 2: Domain DNS & Public Routing.

The goal was to confirm that `stayz3ro.dev` resolves to the Netcup VPS and that administrative SSH access is restricted to the private Tailscale network.

---

## Validation Summary

| Area | Result |
|---|---|
| Root domain | Resolves to Netcup VPS |
| www record | Resolves through CNAME/root domain |
| apps subdomain | Resolves to Netcup VPS |
| status subdomain | Resolves to Netcup VPS |
| api subdomain | Resolves to Netcup VPS |
| Public resolvers | Cloudflare and Google DNS validated |
| Public SSH | Blocked |
| Tailscale SSH | Working |
| HTTP/HTTPS | Publicly allowed for future reverse proxy |
| Direct app ports | Not exposed |

---

## Completion Criteria

| Requirement | Status |
|---|---:|
| Porkbun parking records removed | ✅ Complete |
| Root domain A record configured | ✅ Complete |
| www record configured | ✅ Complete |
| apps subdomain configured | ✅ Complete |
| status subdomain configured | ✅ Complete |
| api subdomain configured | ✅ Complete |
| Local DNS resolution validated | ✅ Complete |
| Public resolver validation completed | ✅ Complete |
| SSH works over Tailscale | ✅ Complete |
| Public SSH is blocked | ✅ Complete |
| UFW confirms Tailscale-only SSH | ✅ Complete |
| DNS and security screenshots captured | ✅ Complete |

---

# Screenshot Evidence

## 01 - Porkbun DNS Records

Confirms DNS records were configured for the root domain and planned service subdomains.

![Porkbun DNS records](../../screenshots/phase-2-domain-dns-public-routing/01-porkbun-dns-records-redacted.png)

---

## 02 - Local DNS Resolution

Confirms local `dig +short` lookups resolve the domain and subdomains.

![DNS resolution](../../screenshots/phase-2-domain-dns-public-routing/02-dns-resolution-dig-short-redacted.png)

---

## 03 - Public Resolver Validation

Confirms public resolvers return the expected DNS records.

![Public resolver validation](../../screenshots/phase-2-domain-dns-public-routing/03-public-resolver-validation-redacted.png)

---

## 04 - UFW Before SSH Cleanup

Shows the firewall state before removing public SSH rules.

![UFW before cleanup](../../screenshots/phase-2-domain-dns-public-routing/04-ufw-before-tailscale-only-ssh-redacted.png)

---

## 05 - SSH Listening Port

Confirms the SSH service listening state before final validation.

![SSH listening port](../../screenshots/phase-2-domain-dns-public-routing/05-ssh-listening-port-redacted.png)

---

## 06 - Tailscale SSH Access Success

Confirms SSH works over the VPS Tailscale IP.

![Tailscale SSH success](../../screenshots/phase-2-domain-dns-public-routing/06-ssh-tailscale-access-success-redacted.png)

---

## 07 - Final UFW Tailscale-Only SSH

Confirms SSH is allowed only over the Tailscale interface while HTTP and HTTPS remain public.

![Final UFW state](../../screenshots/phase-2-domain-dns-public-routing/07-ufw-tailscale-only-ssh-redacted.png)

---

## 08 - Public SSH Blocked

Confirms SSH to the public VPS IP fails.

![Public SSH blocked](../../screenshots/phase-2-domain-dns-public-routing/08-public-ssh-blocked-redacted.png)

---

## Redaction Rules

The following values were redacted or excluded before committing screenshots:

| Sensitive Item | Handling |
|---|---|
| Public IPv4 address | Redacted |
| Tailscale IP | Redacted |
| IPv6 address | Redacted or excluded |
| Porkbun account details | Excluded |
| Email addresses | Redacted or excluded |
| API access details | Excluded |
| Billing details | Excluded |
| SSH host fingerprints | Redacted where visible |

---

## Validation Result

Phase 2 is validated.

The domain DNS foundation is ready, and administrative SSH is restricted to Tailscale.

The VPS is ready for the next phase:

**Phase 3 - Reverse Proxy & HTTPS**
