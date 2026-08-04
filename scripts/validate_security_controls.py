#!/usr/bin/env python3
"""Validate the public security-control inventory and consumer templates."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_CONTROL_IDS = {
    "AUTH-SCOPE-001",
    "CONFIG-FAIL-CLOSED-001",
    "ABUSE-LIMIT-001",
    "INGRESS-BOUNDARY-001",
    "SECRET-HYGIENE-001",
}
PUBLIC_FORBIDDEN = re.compile(
    r"(?:https?://(?:app\.)?notion\.com/p/[0-9a-f]{32}|(?:BEGIN .*PRIVATE KEY)|\b(?:password|token|secret|api[_-]?key)\s*[:=]\s*[A-Za-z0-9+/]{20,})",
    re.IGNORECASE,
)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    inventory = root / "schemas" / "security-controls.yaml"
    policy = root / "policies" / "secure-development.md"
    template = root / "templates" / "repository" / "docs" / "agent" / "SECURITY.md"
    errors: list[str] = []
    if not inventory.is_file():
        errors.append("missing schemas/security-controls.yaml")
    else:
        text = inventory.read_text(encoding="utf-8")
        found = {line.strip()[len("- id:"):].strip() for line in text.splitlines() if line.strip().startswith("- id:")}
        missing = REQUIRED_CONTROL_IDS - found
        if missing:
            errors.append(f"missing control ids: {sorted(missing)}")
    for path in (policy, template):
        if not path.is_file():
            errors.append(f"missing {path.relative_to(root)}")
            continue
        text = path.read_text(encoding="utf-8")
        if PUBLIC_FORBIDDEN.search(text):
            errors.append(f"private or secret-like content in {path.relative_to(root)}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Security controls valid: five baseline controls and public-content checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
