---
name: inventory
description: Generate fast local OpenACA inventory from Claude Code endpoint or project configuration without running advisory lookups.
argument-hint: "[endpoint|project] [optional output path]"
allowed-tools:
  - Bash
  - Read
---

# OpenACA Inventory

Use this skill when the user asks what Claude Code plugins, MCP servers,
skills, hooks, commands, packages, or agent components are installed or
wired together, and they do not explicitly need vulnerability or posture
findings.

## Fast Local Inventory

Generate an endpoint Agent BOM:

```bash
uvx --isolated --from openaca openaca bom endpoint --output openaca-agent-bom.json
```

Include project-local Claude configuration when the user is working in a
project and wants that layered into the endpoint view:

```bash
uvx --isolated --from openaca openaca bom endpoint --project . --output openaca-agent-bom.json
```

If `uvx` is unavailable but `openaca` is installed, use the same command
without the `uvx` prefix.

## Optional Change Review

If the user has a previous BOM and the installed OpenACA CLI supports
`bom diff`, compare snapshots before recommending a deeper scan:

```bash
uvx --isolated --from openaca openaca bom diff --before openaca-agent-bom.previous.json --after openaca-agent-bom.json
```

`bom diff` is local and does not run advisory lookups. It reports added,
removed, and changed component occurrences plus composition-edge changes.

## Reporting

Summarize inventory as composition, not safety:

- active plugins and direct components,
- MCP servers, skills, hooks, and commands observed,
- notable new or removed components when a diff is available,
- where the BOM was written,
- the exact command run.

If the user wants advisories or posture findings, suggest `/openaca:scan`.

## Safety

Do not upload or paste the full BOM unless the user asks. BOMs can include
local paths, URLs, component names, and source provenance.
