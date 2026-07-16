# Contributing

## Before starting

1. Read `START-HERE.md`.
2. Search existing issues.
3. Open or relate an issue for meaningful changes.
4. Use a dedicated branch.
5. Keep the change small, reviewable and reversible.

## Public examples only

This repository teaches users to create their own agentic repositories and knowledge brain. Examples must be fictitious and reusable.

Use neutral values such as:

- `Projeto Exemplo`;
- `Produto Alpha`;
- `Agente de Código`;
- `example-org/example-repo`;
- `https://example.com`.

Never copy private workspace content into an issue, commit, pull request, test fixture or screenshot. Read `docs/governance/PUBLIC-SANITIZATION.md` before publishing examples.

## Validation

Run:

```bash
python scripts/validate_agent_os.py .
```

When changing repository templates, also test the bootstrap:

```bash
mkdir -p /tmp/agent-os-example
git -C /tmp/agent-os-example init
python scripts/bootstrap_repo.py \
  --target /tmp/agent-os-example \
  --project-name "Projeto Exemplo" \
  --repo-slug "projeto-exemplo" \
  --dry-run
```

## Pull requests

Describe:

- the problem;
- what changed;
- why the approach is safe;
- validation performed;
- user or agent impact;
- any limitations or follow-up work.

Do not mark a pull request ready while validation is failing.
