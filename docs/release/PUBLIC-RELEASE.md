# Public release from a clean snapshot

## Security boundary

A private development repository may contain sensitive context in commits, branches, issues, pull requests, comments or deleted files. Sanitizing only the latest files does not sanitize its history.

Do not publish a private development repository by changing its visibility.

## Required flow

```text
private development repository
→ validate current tracked files
→ build clean snapshot
→ inspect generated manifest and ZIP
→ create a new empty public repository
→ initialize new history from the snapshot
→ run validation and bootstrap tests again
→ configure CI and branch protection
→ publish
```

## Build the snapshot

```bash
python scripts/validate_agent_os.py .
python scripts/build_public_snapshot.py --output-dir dist
```

Generated files:

```text
dist/
├── selvalabs-agent-os/
│   └── RELEASE-MANIFEST.json
└── selvalabs-agent-os.zip
```

The package contains tracked files only. It does not contain `.git`, issues, pull requests, branches or private discussions.

## Manual inspection

Before publication:

1. extract the ZIP into a temporary directory;
2. verify `RELEASE-MANIFEST.json`;
3. search for names, URLs, IDs, local paths and private brands;
4. run `python scripts/validate_agent_os.py .` inside the extracted directory;
5. run the bootstrap against a fictitious repository;
6. confirm `LICENSE`, `SECURITY.md` and `CONTRIBUTING.md` are present;
7. review screenshots and binary assets separately, when they exist.

## Initialize public history

From the extracted snapshot:

```bash
rm -rf .git
git init -b main
git add .
git commit -m "feat: publish SelvaLabs Agent OS"
git remote add origin <PUBLIC_REPOSITORY_URL>
git push -u origin main
```

Use an empty public repository. Do not import private issues, pull requests, releases, discussions, branches or tags.

## Repository settings

Recommended initial settings:

- public visibility only after the snapshot review;
- default branch `main`;
- require pull requests for changes;
- require successful Actions checks;
- block force pushes and branch deletion;
- enable private vulnerability reporting;
- add topics such as `agentic-engineering`, `ai-agents`, `developer-tools`, `notion`, `github-actions`, `python` and `governance`;
- add a social preview without private screenshots.

## Ongoing publication

Treat the private repository as the development source and the public repository as a reviewed distribution.

Future public updates should use a deliberate release process with:

1. private issue and branch;
2. implementation and validation;
3. sanitized snapshot;
4. diff against the public repository;
5. public pull request containing only releasable changes.
