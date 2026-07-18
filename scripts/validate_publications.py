#!/usr/bin/env python3
"""Reject public content that is not explicitly approved."""

from __future__ import annotations

import re
import sys
from pathlib import Path

CONTENT_ROOT = Path("content")
PUBLIC_SECTIONS = ("articles", "talks", "podcast")


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    parts = text.split("---", 2)
    return parts[1] if len(parts) == 3 else ""


def value(block: str, key: str) -> str | None:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*([^#\n]*)", block)
    if not match:
        return None
    return match.group(1).strip().strip('"\'').lower()


def main() -> int:
    errors: list[str] = []

    for section in PUBLIC_SECTIONS:
        directory = CONTENT_ROOT / section
        if not directory.exists():
            continue

        for path in sorted(directory.rglob("*.md")):
            if path.name == "_index.md":
                continue

            block = frontmatter(path.read_text(encoding="utf-8"))
            draft = value(block, "draft")
            status = value(block, "status")
            approval = value(block, "approvalStatus")

            if draft == "false" and (status != "approved" or approval != "approved"):
                errors.append(
                    f"{path}: draft=false requires params.status=approved "
                    "and params.approvalStatus=approved"
                )

    if errors:
        print("Publication approval validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Publication approval validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
