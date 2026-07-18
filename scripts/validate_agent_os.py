#!/usr/bin/env python3
"""Validate the Agent OS structure using only the Python standard library."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import unicodedata
from pathlib import Path

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"(?i)\b(?:api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{20,}"),
]

PUBLIC_PRIVACY_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("URL de página privada do Notion", re.compile(r"https://app\.notion\.com/p/[0-9a-f]{32}(?:\?[^\s)]*)?", re.IGNORECASE)),
    ("URL do Notion com identificador concreto", re.compile(r"https://(?:www\.)?notion\.so/[^\s)]*[0-9a-f]{32}(?:\?[^\s)]*)?", re.IGNORECASE)),
    ("identificador concreto de data source do Notion", re.compile(r"collection://[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}", re.IGNORECASE)),
    ("caminho local de usuário no Windows", re.compile(r"[A-Za-z]:\\Users\\(?!Example(?:\\|$))[^\\\s]+\\", re.IGNORECASE)),
    ("caminho local de usuário Unix", re.compile(r"/(?:home|Users)/(?!example(?:/|$))[^/\s]+/", re.IGNORECASE)),
    ("link para outro repositório SelvaLabs não liberado no framework", re.compile(r"https://github\.com/selvalabs/(?!selvalabs-agent-os(?:/|\b)|agent-os(?:/|\b))[A-Za-z0-9_.-]+", re.IGNORECASE)),
]

PRIVATE_PHRASE_HASHES = {
    "788eb2efc52660fe41472319f0d2c623be6540c956921b3632fcc934bf1be10d", "a18c05dcf81fe8461573c6afbe2becd85e4b2abae5f8fb99db29dd960e2d418d",
    "505a273570ca56047c4eb3f420da358ba958ffb2d2b7ad3c3c816f15f4451be4", "f0d9991c5e47e0d26a350c1618bd3154cd0f9f2461d3df671a753c393fe7a6a7",
    "08375490156ef328bb0e4266407d43dd49434dd823b2af71553bf89f360f5fd5", "5b4245d59aec80a3042c6f57af5eba73b6d4572c7597cd0d72be34ea7b51ccc7",
    "1426db568ced337fabba208afbb0200ccf0cea99622300134148caa1b4fbe283", "32c4d6efbac5730ce47b612e644d4d961d7b70caa3eddf51c7be0528de633481",
    "216e6fbc15d2ad97f4910ef225412f40f797c8ba6eef1c3dd9b52304cfb22a63", "dacf9ba53d3038ae8b8c4ec724c48b919f4f4e5897189d33e6bba0874e079bfc",
    "1172b79eec1555c69ba6088631f7fe1061982ae746d232879d41b945eac57b66", "3e61f3d72584db6d7385b8ec05842f864f89294452a32ad82760c6b8e5efaa6e",
}

PUBLIC_TEXT_ROOTS = {"README.md", "START-HERE.md", "AGENTS.md", "SECURITY.md", "CONTRIBUTING.md", "docs", "templates", "policies", "skills", "compatibility", "scripts", ".github"}

FORBIDDEN_MEMORY_ARCHITECTURE_PHRASES = {
    "view da biblioteca filtrada pelo projeto",
    "view da biblioteca de markdowns deste projeto",
    "biblioteca de markdowns do projeto",
    "toda página de projeto deve incluir uma view vinculada da biblioteca",
    "páginas de projeto com views filtradas da biblioteca",
    "as áreas 01 a 05 devem usar views vinculadas da mesma biblioteca",
}

REQUIRED_MEMORY_BOUNDARIES = {
    "README.md": "biblioteca de markdowns não é um catálogo de projetos",
    "docs/notion/START-HERE.md": "não é o lugar onde os projetos são registrados",
    "docs/notion/MARKDOWN-LIBRARY-MEMORY.md": "a biblioteca não registra projetos",
    "templates/repository/START-HERE.md": "não cadastre o projeto na biblioteca de markdowns",
}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def is_public_text_path(path: Path, root: Path) -> bool:
    return path.relative_to(root).parts[0] in PUBLIC_TEXT_ROOTS


def normalized_text(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    normalized = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    normalized = normalized.lower()
    return re.sub(r"[^a-z0-9]+", " ", normalized).strip()


def contains_private_phrase_fingerprint(text: str) -> bool:
    tokens = normalized_text(text).split()
    for size in range(1, min(8, len(tokens)) + 1):
        for start in range(0, len(tokens) - size + 1):
            phrase = " ".join(tokens[start:start + size])
            if hashlib.sha256(phrase.encode("utf-8")).hexdigest() in PRIVATE_PHRASE_HASHES:
                return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", type=Path)
    root = parser.parse_args().root.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    required = [
        "START-HERE.md", "AGENTS.md", "LICENSE", "SECURITY.md", "CONTRIBUTING.md",
        "docs/architecture/SPEC-AGENT-OS.md", "docs/governance/SECURITY-MODEL.md",
        "docs/governance/PUBLIC-SANITIZATION.md", "docs/release/PUBLIC-RELEASE.md",
        "docs/notion/START-HERE.md", "docs/notion/NOTION-BRAIN-ARCHITECTURE.md",
        "docs/notion/MARKDOWN-LIBRARY-MEMORY.md", "docs/notion/DATABASE-SCHEMAS.md",
        "scripts/build_public_snapshot.py", ".github/workflows/build-public-snapshot.yml",
        "templates/repository/START-HERE.md", "templates/repository/AGENTS.md", "templates/repository/CLAUDE.md",
    ]
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f"Arquivo obrigatório ausente: {relative}")

    agents = root / "AGENTS.md"
    if agents.exists() and len(agents.read_text(encoding="utf-8").splitlines()) > 200:
        warnings.append("AGENTS.md tem mais de 200 linhas; considere reduzir.")

    skill_root = root / "skills"
    if not skill_root.is_dir():
        errors.append("Diretório skills ausente.")
    else:
        names: set[str] = set()
        for skill_dir in sorted(p for p in skill_root.iterdir() if p.is_dir()):
            skill_file = skill_dir / "SKILL.md"
            if not skill_file.exists():
                errors.append(f"Skill sem SKILL.md: {skill_dir.name}")
                continue
            meta = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
            if not meta.get("name") or not meta.get("description"):
                errors.append(f"Frontmatter incompleto em {skill_file.relative_to(root)}")
            if meta.get("name") != skill_dir.name:
                errors.append(f"Nome da skill diverge do diretório: {skill_dir.name} != {meta.get('name')}")
            if meta.get("name") in names:
                errors.append(f"Nome de skill duplicado: {meta.get('name')}")
            names.add(meta.get("name", ""))

    scan_extensions = {".md", ".yaml", ".yml", ".json", ".py"}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in scan_extensions or ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"Possível segredo em {path.relative_to(root)}")
        if is_public_text_path(path, root):
            for label, pattern in PUBLIC_PRIVACY_PATTERNS:
                if pattern.search(text):
                    errors.append(f"Possível contexto privado ({label}) em {path.relative_to(root)}")
            if contains_private_phrase_fingerprint(text):
                errors.append(f"Possível marcador privado conhecido em {path.relative_to(root)}")
            if path.suffix.lower() == ".md":
                normalized = normalized_text(text)
                for phrase in FORBIDDEN_MEMORY_ARCHITECTURE_PHRASES:
                    if normalized_text(phrase) in normalized:
                        errors.append(f"Arquitetura mistura projeto e Biblioteca em {path.relative_to(root)}: {phrase}")

    for relative, required_phrase in REQUIRED_MEMORY_BOUNDARIES.items():
        path = root / relative
        if path.exists():
            normalized = normalized_text(path.read_text(encoding="utf-8", errors="replace"))
            if normalized_text(required_phrase) not in normalized:
                errors.append(f"Limite entre Projetos e Biblioteca ausente em {relative}")

    readme = root / "README.md"
    if readme.exists():
        readme_text = readme.read_text(encoding="utf-8")
        if "PUBLIC-SANITIZATION.md" not in readme_text:
            errors.append("README.md deve apontar para docs/governance/PUBLIC-SANITIZATION.md")
        if "histórico novo" not in readme_text and "histórico limpo" not in readme_text:
            warnings.append("README.md deveria explicar que a publicação pública usa histórico novo ou limpo.")

    for message in warnings:
        print(f"AVISO: {message}")
    for message in errors:
        print(f"ERRO: {message}", file=sys.stderr)
    if errors:
        print(f"Falhou com {len(errors)} erro(s).", file=sys.stderr)
        return 1
    print(f"Validação concluída: {len(warnings)} aviso(s), nenhum erro.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
