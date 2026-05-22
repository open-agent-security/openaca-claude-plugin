#!/usr/bin/env python3
"""Validate the OpenACA Claude Code plugin scaffold."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_JSON = ROOT / ".claude-plugin" / "plugin.json"
MARKETPLACE_JSON = ROOT / ".claude-plugin" / "marketplace.json"


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        fail(f"missing {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def main() -> int:
    manifest = load_json(PLUGIN_JSON)
    marketplace = load_json(MARKETPLACE_JSON)

    if manifest.get("name") != "openaca":
        fail(".claude-plugin/plugin.json name must be openaca")

    if marketplace.get("name") != "openaca":
        fail(".claude-plugin/marketplace.json name must be openaca")

    skills_dir = ROOT / "skills"
    expected_skills = {"scan", "bom", "explain", "triage"}
    observed_skills = {
        child.name
        for child in skills_dir.iterdir()
        if child.is_dir() and (child / "SKILL.md").is_file()
    }
    if observed_skills != expected_skills:
        fail(f"expected skills {sorted(expected_skills)}, found {sorted(observed_skills)}")

    forbidden_paths = [
        ROOT / "hooks",
        ROOT / "monitors",
        ROOT / ".mcp.json",
        ROOT / "bin",
    ]
    present = [path.name for path in forbidden_paths if path.exists()]
    if present:
        fail(f"V1 plugin must not ship ambient execution surfaces: {', '.join(present)}")

    plugins = marketplace.get("plugins", [])
    if len(plugins) != 1 or plugins[0].get("name") != "openaca":
        fail("marketplace must list exactly one openaca plugin")

    print("plugin scaffold ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
