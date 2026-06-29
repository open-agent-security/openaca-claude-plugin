# OpenACA Claude Code Plugin

OpenACA adds explicit Claude Code workflows for agent supply-chain
security. It helps Claude run the open `openaca` scanner, generate Agent
BOMs, and explain findings for Claude Code plugins, skills, MCP servers,
hooks, commands, and runtime components.

This plugin is the preferred developer install path for local OpenACA
workflows in Claude Code. It is a thin wrapper around the published
OpenACA CLI and does not contain scanner logic, hooks, background
monitors, or an MCP server. MDM or other managed deployment remains the
right path when an organization needs mandatory coverage across a fleet.

## Install

During early testing, install directly from this repository:

```text
/plugin marketplace add open-agent-security/openaca-claude-plugin
/plugin install openaca@openaca
/reload-plugins
```

The skills are then available as namespaced Claude Code commands:

```text
/openaca:inventory
/openaca:scan
/openaca:bom
/openaca:explain
/openaca:triage
/openaca:sync
```

## Requirements

- Claude Code with plugin support.
- `uvx` available on PATH, or the `openaca` CLI already installed.

The plugin examples use `uvx --isolated --from openaca` so the latest
published OpenACA runs on demand without managing a separate installation.

## What The Plugin Provides

- `/openaca:inventory`: generate a fast local Agent BOM inventory without
  advisory lookups.
- `/openaca:scan`: run a deeper OpenACA endpoint or repository scan for
  advisory and posture findings.
- `/openaca:bom`: generate an Agent BOM for the current endpoint or repo.
- `/openaca:explain`: explain OpenACA findings and next steps.
- `/openaca:triage`: guide a focused review after agent configuration
  changes.
- `/openaca:sync`: configure, check, or explicitly upload endpoint state
  to OpenACA Cloud.

## Safety Model

OpenACA V1 plugin behavior is explicit-invocation only. It does not:

- install hooks,
- run background monitors,
- block tool usage,
- modify Claude Code settings automatically,
- automatically upload local configuration to OpenACA services.

The underlying `openaca` CLI may query configured public vulnerability
federation sources such as OSV.dev as part of normal scanning.
`/openaca:inventory` and `openaca bom diff` are local inventory/change
workflows; `/openaca:sync` is the explicit Cloud upload boundary.

## Development

Validate plugin structure:

```bash
python3 scripts/validate_plugin.py
```

If Claude Code is installed, also run:

```bash
claude plugin validate .
```

The marketplace pins the plugin source by git SHA. The plugin manifest
intentionally omits `version` so Claude Code uses the source SHA for
update detection. When plugin payload files change on `main`, the
`bump-marketplace-sha` workflow opens a PR to update the pinned SHA.
