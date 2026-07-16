#!/usr/bin/env python3
"""Build a clean public snapshot from the current tracked repository state."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path, PurePosixPath

PACKAGE_NAME = "selvalabs-agent-os"
EXCLUDED_EXACT = {
    "validation-report.txt",
}
EXCLUDED_PREFIXES = (
    ".git/",
    "dist/",
    "__pycache__/",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-dir", type=Path, default=Path("dist"))
    return parser.parse_args()


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        check=True,
        text=True,
        capture_output=True,
    )


def tracked_files(root: Path) -> list[PurePosixPath]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=root,
        check=True,
        capture_output=True,
    )
    paths: list[PurePosixPath] = []
    for raw in result.stdout.split(b"\0"):
        if not raw:
            continue
        relative = PurePosixPath(raw.decode("utf-8"))
        value = relative.as_posix()
        if value in EXCLUDED_EXACT or any(value.startswith(prefix) for prefix in EXCLUDED_PREFIXES):
            continue
        paths.append(relative)
    return sorted(paths, key=lambda item: item.as_posix())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_deterministic_zip(package_dir: Path, archive_path: Path) -> None:
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(package_dir.rglob("*"), key=lambda item: item.relative_to(package_dir).as_posix()):
            if not path.is_file():
                continue
            relative = PurePosixPath(PACKAGE_NAME) / PurePosixPath(path.relative_to(package_dir).as_posix())
            info = zipfile.ZipInfo(relative.as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())


def main() -> int:
    args = parse_args()
    root = args.root.expanduser().resolve()
    output_dir = args.output_dir.expanduser()
    if not output_dir.is_absolute():
        output_dir = (root / output_dir).resolve()

    validator = root / "scripts" / "validate_agent_os.py"
    if not validator.is_file():
        print(f"Missing validator: {validator}", file=sys.stderr)
        return 2

    validation = run([sys.executable, str(validator), str(root)], cwd=root)
    if validation.stdout:
        print(validation.stdout, end="")

    package_dir = output_dir / PACKAGE_NAME
    archive_path = output_dir / f"{PACKAGE_NAME}.zip"
    if package_dir.exists():
        shutil.rmtree(package_dir)
    if archive_path.exists():
        archive_path.unlink()
    package_dir.mkdir(parents=True)

    manifest_files: list[dict[str, object]] = []
    for relative in tracked_files(root):
        source = root / Path(relative.as_posix())
        if source.is_symlink():
            raise RuntimeError(f"Symlinks are not allowed in the public snapshot: {relative}")
        if not source.is_file():
            continue
        destination = package_dir / Path(relative.as_posix())
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        manifest_files.append(
            {
                "path": relative.as_posix(),
                "sha256": sha256(destination),
                "size_bytes": destination.stat().st_size,
            }
        )

    manifest = {
        "package": PACKAGE_NAME,
        "format": 1,
        "history_included": False,
        "issues_included": False,
        "pull_requests_included": False,
        "files": manifest_files,
    }
    manifest_path = package_dir / "RELEASE-MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if (package_dir / ".git").exists():
        raise RuntimeError("Public snapshot unexpectedly contains .git")

    write_deterministic_zip(package_dir, archive_path)
    print(f"Public snapshot directory: {package_dir}")
    print(f"Public snapshot archive: {archive_path}")
    print(f"Tracked files copied: {len(manifest_files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
