#!/usr/bin/env python3
"""Build the distributable TicNote OpenClaw Skill archive."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
STAGE = DIST / "ticnote-openclaw"
VERSION_FILE = ROOT / "VERSION"


def read_version() -> str:
    if VERSION_FILE.exists():
        version = VERSION_FILE.read_text(encoding="utf-8").strip()
        if version:
            return version.removeprefix("v")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    for line in skill.splitlines():
        if line.startswith("version:"):
            version = line.split(":", 1)[1].strip()
            if version:
                return version.removeprefix("v")

    raise RuntimeError("Cannot determine Skill version from VERSION or SKILL.md")


def build() -> Path:
    version = read_version()
    archive = DIST / f"ticnote-openclaw-{version}.zip"

    if STAGE.exists():
        shutil.rmtree(STAGE)
    DIST.mkdir(parents=True, exist_ok=True)
    STAGE.mkdir(parents=True)

    for name in ("SKILL.md", "README.md", "README.en.md", "LICENSE"):
        source = ROOT / name
        if not source.exists():
            raise FileNotFoundError(source)
        shutil.copy2(source, STAGE / name)

    shutil.copytree(ROOT / "references", STAGE / "references")

    if archive.exists():
        archive.unlink()
    shutil.make_archive(str(archive.with_suffix("")), "zip", DIST, STAGE.name)
    shutil.rmtree(STAGE)

    print(archive)
    return archive


if __name__ == "__main__":
    try:
        build()
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
