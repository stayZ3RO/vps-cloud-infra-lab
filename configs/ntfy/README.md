# ntfy (self-hosted push notifications)

Private ntfy instance for alert delivery, published at
`https://ntfy.chrisalorenzo.com` through the existing Caddy.

| File | Purpose |
|---|---|
| `docker-compose.yml` | ntfy service, pinned image, persistent volumes, `web` network, no published ports |
| `server.yml` | Private-instance settings: `deny-all`, behind Caddy, no web app, cache and attachment limits |

Users, access rules, and tokens are created with the ntfy CLI inside the
container and live only in the `ntfy_lib` volume. Never commit them.

Setup, validation, and rollback:
[`docs/phase-5-monitoring-and-alerts/ntfy-self-hosted-execution-packet.md`](../../docs/phase-5-monitoring-and-alerts/ntfy-self-hosted-execution-packet.md).
