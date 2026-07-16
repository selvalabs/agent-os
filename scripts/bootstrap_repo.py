#!/usr/bin/env python3
"""Bootstrap agent documentation into a repository without overwriting by default."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

PLACEHOLDERS = {
    "{{PROJECT_NAME}}": None,
    "{{REPO_SLUG}}": None,
    "{{INSTALL_COMMAND}}": "TODO: definir instalação",
    "{{TEST_COMMAND}}": "TODO: definir testes",
    "{{LINT_COMMAND}}": "TODO: definir lint",
    "{{BUILD_COMMAND}}": "TODO: definir build",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--repo-slug", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true", help="Sobrescreve arquivos existentes; use somente após revisão.")
    parser.add_argument("--allow-non-git", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = args.target.expanduser().resolve()
    template = Path(__file__).resolve().parents[1] / "templates" / "repository"

    if not target.exists() or not target.is_dir():
        print(f"Erro: diretório alvo inexistente: {target}", file=sys.stderr)
        return 2
    if not args.allow_non_git and not (target / ".git").exists():
        print("Erro: o alvo não parece ser um repositório Git. Use --allow-non-git conscientemente.", file=sys.stderr)
        return 2

    replacements = dict(PLACEHOLDERS)
    replacements["{{PROJECT_NAME}}"] = args.project_name
    replacements["{{REPO_SLUG}}"] = args.repo_slug

    planned: list[tuple[Path, str]] = []
    collisions: list[Path] = []

    for source in sorted(template.rglob("*")):
        if not source.is_file():
            continue
        relative = source.relative_to(template)
        destination = target / relative
        if destination.exists() and not args.force:
            collisions.append(relative)
            continue
        text = source.read_text(encoding="utf-8")
        for old, new in replacements.items():
            if new is not None:
                text = text.replace(old, new)
        planned.append((destination, text))

    print(f"Alvo: {target}")
    for destination, _ in planned:
        print(f"CRIAR: {destination.relative_to(target)}")
    for relative in collisions:
        print(f"PRESERVAR: {relative}")

    if args.dry_run:
        print("Dry-run: nenhuma alteração feita.")
        return 0

    for destination, text in planned:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, encoding="utf-8")

    print(f"Concluído: {len(planned)} arquivo(s) criado(s); {len(collisions)} preservado(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
