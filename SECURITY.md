# Security Policy

## Supported scope

The current public release line receives documentation, template, bootstrap and validation fixes on the default branch.

## Reporting a vulnerability

Do not publish credentials, private workspace URLs, private repository references, personal data or exploit details in a public issue.

Report suspected vulnerabilities privately to the repository maintainer through GitHub's private vulnerability reporting feature when it is enabled. If that feature is unavailable, use the private contact channel listed on the maintainer's GitHub profile.

Include:

- affected file, script or workflow;
- reproducible impact;
- minimum steps needed to verify the issue;
- whether private context or credentials may have been exposed;
- suggested mitigation, when available.

## Public-content boundary

This project is a generic framework. Contributions must not contain:

- real Notion page or database URLs;
- concrete private workspace IDs;
- client, project or internal agent names;
- local user paths;
- tokens, keys, passwords, cookies or secrets;
- copied private issues, pull requests or conversation logs.

Run before submitting changes:

```bash
python scripts/validate_agent_os.py .
```

## Operational safety

External services begin in read-only mode. Production, destructive changes, migrations and permission changes require explicit human approval, preflight checks, rollback planning and verification.
