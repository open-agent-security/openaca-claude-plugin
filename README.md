# OpenACA Claude Code Plugin

OpenACA adds explicit Claude Code workflows for agent supply-chain
security. It helps Claude run the open `openaca` scanner, generate Agent
BOMs, and explain findings for Claude Code plugins, skills, MCP servers,
hooks, commands, and runtime components.

This plugin is a thin wrapper around the published OpenACA CLI. It does
not contain scanner logic, hooks, background monitors, or an MCP server.

## Install

During early testing, install directly from this repository:

```text
/plugin marketplace add open-agent-security/openaca-claude-plugin
/plugin install openaca@openaca
/reload-plugins
```

The skills are then available as namespaced Claude Code commands:

```text
/openaca:scan
/openaca:bom
/openaca:explain
/openaca:triage
```

## Requirements

- Claude Code with plugin support.
- `uvx` available on PATH, or the `openaca` CLI already installed.

The plugin examples use `uvx --prerelease allow --from openaca` so
beta testers get the latest published OpenACA pre-release without
managing a separate installation.

## What The Plugin Provides

- `/openaca:scan`: run an OpenACA endpoint or repository scan.
- `/openaca:bom`: generate an Agent BOM for the current endpoint or repo.
- `/openaca:explain`: explain OpenACA findings and next steps.
- `/openaca:triage`: guide a focused review after agent configuration
  changes.

## Safety Model

OpenACA V1 plugin behavior is explicit-invocation only. It does not:

- install hooks,
- run background monitors,
- block tool usage,
- modify Claude Code settings automatically,
- upload local configuration to OpenACA services.

The underlying `openaca` CLI may query configured public vulnerability
federation sources such as OSV.dev as part of normal scanning.

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
