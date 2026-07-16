# Implementation status — version 0.1

## Included

- Agent OS architecture and context hierarchy;
- reusable policies and skills;
- repository templates with `START-HERE.md` and `AGENTS.md`;
- compatibility guidance for agent-specific instruction files;
- non-destructive repository bootstrap with `--dry-run`;
- structural, secret and public-context validation;
- CI workflows;
- example manifests and schemas;
- generic Notion Brain implementation guidance;
- Markdown Library memory model and write-back workflow;
- clean public snapshot builder with file manifest.

## Deliberately not automated

The framework does not automatically:

- write into a user's Notion workspace;
- create or rename GitHub repositories;
- modify production services;
- change database schemas;
- deploy to servers;
- grant agent permissions;
- synchronize private and public repositories bidirectionally.

These operations require explicit authorization, environment-specific configuration, review and appropriate credentials.

## Recommended adoption path

1. read `START-HERE.md`;
2. validate the framework;
3. bootstrap a fictitious repository with `--dry-run`;
4. adapt placeholders to the target project;
5. test one controlled repository before broader adoption;
6. create a separate knowledge Brain only when its ownership and source rules are clear;
7. add enforcement and production access gradually.

## Public distribution

Use `scripts/build_public_snapshot.py` and `docs/release/PUBLIC-RELEASE.md` to create a clean distribution. Do not publish a private development repository by changing its visibility when its history contains internal context.
