---
name: agentic-mailboxes
description: Use when creating, operating, troubleshooting, or extending an agent email mailbox with Cloudflare Email Routing, HTTPS ingress, PostgreSQL queues, Telegram delivery, approval workflows, or Brevo outbound sending.
---

# Agentic Mailboxes

Use this as an agent- and project-neutral pattern. Replace every value in `<ANGLE_BRACKETS>` with the target project's configuration. Never copy another agent's credentials, sessions, network, database, domain, or Telegram destination.

## Inbound architecture

```text
SMTP → Cloudflare Email Routing → Worker → HTTPS gateway → private queue/database → notifier/channel
```

The mailbox domain and technical HTTPS hostname are independent. Prefer a one-level technical hostname such as `email-api.<zone>`; deep hostnames can exceed a provider's default certificate coverage. Keep databases and gateways private, and expose only the intended HTTPS endpoint through the tunnel.

Validate inbound data in this order: timestamp, HMAC over the exact request bytes, JSON shape, MIME size/base64, recipient allowlist, MIME parsing, raw storage, message/thread upsert, and queue insertion. Use idempotent inserts and `ON CONFLICT DO NOTHING` where partial indexes make a conflict target unsafe.

Consume queue jobs with `FOR UPDATE SKIP LOCKED`, bounded retries, dead-letter state, and explicit downstream chat/topic identifiers. Preserve the complete body and attachments metadata. Do not infer a destination from the latest channel message.

## Outbound architecture

```text
draft/template → approval policy → jobs.queue → private provider worker → provider webhook → delivery state
```

Keep provider credentials in a secret broker or read-only secret mount. The agent-facing API must not receive the provider key. Authenticate the sender/domain before testing. For Brevo, use a REST API key with `POST https://api.brevo.com/v3/smtp/email`; an SMTP relay key is not interchangeable with an API key.

Support three explicit modes:

1. **Approved template** — render an active, versioned template and send automatically; notify the channel.
2. **Suggested reply** — show the complete proposed reply and send only after explicit human confirmation.
3. **Channel-created message** — allow edits, show the final preview, and send only after explicit confirmation.

Store approval nonce hash, chat ID, optional topic/thread ID, user ID, action, and expiry. Bind and consume them transactionally; enqueue at most one send job. Never infer approval from a later message. Validate variables exactly, reject unapproved senders, preserve UTF-8, and keep idempotency keys.

## Telegram presentation contract

Keep outbound confirmation and inbound notification distinct.

```text
✅ E-mail enviado

Para: <recipient>
Assunto: <subject>
Status: <provider status>

Mensagem:
<complete body>

ID técnico: <short id>
```

```text
📩 Novo e-mail

De: <parsed MIME From>
Para: <recipients>
Assunto: <subject>
Recebido: <local date/time>

Mensagem:
<current body>

──── Histórico citado ────
<quoted history, if present>

ID técnico: <short id>
```

Use the parsed MIME `sender`/`From` as the visible sender. Never display SMTP `envelope_from`/`Return-Path` as `De`; bounce addresses are technical metadata. Prefer `text_body`, convert `html_body` to safe plain text as fallback, and only then show `(sem corpo textual)`. Split replies at attribution lines such as `On ... wrote:` or `Em ... escreveu:` without deleting the quoted content. Show attachment count when nonzero and escape/sanitize content for the channel format.

## Provider webhook

Authenticate the webhook, validate shape, deduplicate by event hash/provider event key, and do not log payloads or bodies. Map sent, delivered, deferred, soft bounce, hard bounce, blocked, complaint, and error events to message/draft states. Queue completion means provider acceptance, not inbox delivery.

## Deployment and diagnostics

Before production changes: read the target project's runbook, perform preflight, create a private database/config backup, apply only scoped services/migrations, retain a rollback path, and run health plus synthetic MIME/provider/channel smoke tests. Record backup path, container/service status, restart counts, validation results, and next pending step in the target handoff.

Diagnose the first failing boundary: MX/SMTP → routing → TLS → Worker signature → gateway validation → parser/storage → queue → notifier/channel → provider/webhook. Keep all secrets, raw MIME, message bodies, personal recipients, and private IDs out of Git, prompts, logs, and handoffs.
