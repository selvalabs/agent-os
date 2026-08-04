# Secure Development Controls Design

## Goal
Turn recurring security findings into reusable, public-safe controls that are applied during agentic development rather than discovered only after deployment.

## Public boundary
The public Agent OS contains generic controls, fictional examples, and validation logic only. It must not contain private domains, infrastructure addresses, workspace IDs, credentials, or project-specific operational values.

## Components
- `policies/secure-development.md`: generic invariants for authorization, secrets, abuse resistance, and ingress exposure.
- `schemas/security-controls.yaml`: machine-readable control inventory with required evidence.
- `templates/repository/docs/agent/SECURITY.md`: project-level security worksheet.
- `.github` templates: issue and PR prompts that require security evidence.
- `scripts/validate_security_controls.py`: deterministic validation of the inventory and public-safe template files.

## Workflow
An agent records applicable controls in the issue, adds a regression test for each security-sensitive behavior, runs the validator and project checks, then includes evidence in the PR. The bootstrap copies the worksheet and templates into new repositories.

## Non-goals
This layer does not prescribe a specific cloud, proxy, database, rate-limit backend, or secret manager. Those belong in the Selva-specific adapter or the consuming project.

## Acceptance criteria
- New bootstrapped repositories receive the security worksheet and GitHub prompts.
- The control inventory is valid and contains the four baseline invariants.
- Public sanitization checks reject private operational material.
- Existing Agent OS validation and dry-run bootstrap checks remain green.
