---
name: triage
description: Guide agent supply-chain triage after Claude Code MCP, plugin, skill, hook, command, or settings changes.
argument-hint: "[what changed]"
allowed-tools:
  - Bash
  - Read
---

# OpenACA Triage

Use this skill when the user has added or changed MCP servers, plugins,
skills, hooks, commands, `.claude/settings.json`, or other agent runtime
configuration and wants a security-oriented review.

## Triage Flow

1. Identify the changed scope: endpoint config, project config, repo
   files, or a stored Agent BOM.
2. Run the narrowest useful scan:

```bash
uvx openaca scan endpoint -v --project .
```

3. If the user only wants inventory, generate a BOM instead:

```bash
uvx openaca bom endpoint --project . --output openaca-agent-bom.json
```

4. Summarize new or relevant components:
   plugins, MCP servers, skills, hooks, commands, and direct components.
5. Separate evidence classes:
   advisory matches, posture findings, and composition inventory.
6. Recommend next steps only where evidence supports them.

If `uvx` is unavailable but `openaca` is installed, use the same command
without the `uvx` prefix.

## Safety

Ask before making changes. Do not disable components, edit settings, or
remove files without explicit user approval.
