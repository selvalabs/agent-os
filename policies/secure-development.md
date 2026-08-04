# Secure development controls

These controls are generic and apply to every agentic change. The consuming project records the chosen implementation in `docs/agent/SECURITY.md`.

## Required invariants

1. **Authorization scope:** every write path identifies its tenant, project, account or resource scope and rejects requests outside that scope. A global integration credential is never sufficient by itself.
2. **Fail-closed configuration:** credentials, signing keys, allowlists and ingress protections have no insecure defaults. Missing required values stop startup or deployment.
3. **Abuse resistance:** externally reachable ingestion, authentication and expensive operations have bounded body size, rate/concurrency limits and observable rejection behavior. When more than one application replica can serve traffic, limiter state must be shared through a distributed backend; process-local counters are not sufficient.
4. **Ingress boundary:** internal services are not published directly when a TLS/authenticated proxy is the intended boundary. Exposed ports must be documented and tested.
5. **Secret hygiene:** examples use short fictional placeholders; real values come from a secret manager or environment injection and never appear in logs, issues or documentation.

## Development rule

For each applicable invariant, the issue must name the control, the regression test and the validation command. A security-sensitive change is not ready for merge until the original abuse case no longer reproduces.

## Evidence expectations

- authorization: negative cross-scope test plus legitimate positive test;
- configuration: startup/compose validation with missing values;
- abuse resistance: deterministic limit test with expected `429`/rejection;
- ingress: port/config inspection and authenticated route check;
- secrets: repository scan and diff review.

The framework does not prescribe a cloud, proxy, database or rate-limit backend. Projects must document those choices locally.
