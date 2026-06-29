# OpenACA Claude Code Plugin

## What this repo is

OpenACA Claude Code Plugin adds explicit Claude Code workflows for
agent supply-chain security — running the open `openaca` scanner,
generating Agent BOMs, and explaining findings for Claude Code
plugins, skills, MCP servers, hooks, commands, and runtime components.
The plugin is a thin wrapper around the published OpenACA CLI; it
ships no scanner logic, hooks, background monitors, or MCP server.

## Common commands

```bash
bash scripts/install-hooks.sh         # one-time, install pre-push gate
python3 scripts/validate_plugin.py    # validate the plugin scaffold
claude plugin validate .              # full plugin validation (if Claude Code CLI installed)
```

## Architecture

This is a Claude Code plugin, not a Python application. The shipped
surface is:

- `.claude-plugin/plugin.json` + `marketplace.json` — manifest +
  marketplace listing.
- `skills/{inventory,scan,bom,explain,triage,sync}/SKILL.md` — the six
  namespaced commands users invoke (`/openaca:inventory` etc.).
- `scripts/validate_plugin.py` — local scaffold validator (also
  invoked by the pre-push hook and CI).

V1 is explicit-invocation only: no ambient hooks, no background
monitors, no `.mcp.json`, no `bin/`. `validate_plugin.py` enforces
that by failing if any of those paths appear.

The plugin is the preferred developer install path for Claude Code users.
Keep it thin over the published OpenACA CLI: plugin skills may guide users
to CLI primitives such as `bom endpoint`, `bom diff`, `scan endpoint`, and
`remote sync endpoint`, but must not embed scanner, diff, or upload logic.

## Repo conventions

- Skills follow Claude Code's `skills/<name>/SKILL.md` layout.
  Adding or removing a skill means updating `expected_skills` in
  `scripts/validate_plugin.py` and the README command list.
- All JSON in `.claude-plugin/` and `skills/` must parse — the
  pre-push hook and CI both run a syntax check.
- The plugin must not auto-install hooks or modify Claude Code
  settings; that's the V1 safety model documented in README.md.
