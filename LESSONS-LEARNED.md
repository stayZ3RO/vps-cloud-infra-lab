# Lessons Learned

## Phase 1 - VPS Baseline & Security Hardening

### Secure the Server Before Hosting Services

Before deploying applications, the VPS needs a secure baseline: patched OS, non-root sudo user, SSH hardening, firewall rules, brute-force protection, and validation of listening ports.

### SSH Changes Require Careful Validation

SSH configuration should be validated before reloading the service.

Useful validation command:

    sudo sshd -t

A second terminal should be used to test login before closing the original SSH session.

### Hostname Resolution Matters

After setting the hostname, `/etc/hosts` should contain a matching local hostname entry to avoid sudo resolution warnings.

### Public Services Should Be Minimal

Only SSH, HTTP, and HTTPS should be exposed initially. Admin dashboards, databases, Docker ports, and monitoring tools should not be directly exposed to the public internet.

### Screenshots Need Redaction

Provider details, public IPs, private IPs, Tailscale details, emails, tokens, and billing information should be redacted before committing screenshots.
