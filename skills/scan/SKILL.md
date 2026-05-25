---
name: scan
description: Run OpenACA scans from Claude Code when the user asks to scan agent components, check Claude Code configuration, inspect MCP servers/plugins/skills/hooks, or assess agent supply-chain risk.
argument-hint: "[endpoint|repo] [optional path]"
allowed-tools:
  - Bash
  - Read
---

# OpenACA Scan

Use this skill when the user asks to run OpenACA, scan the current
Claude Code endpoint, scan a repository, check MCP servers, inspect
installed plugins or skills, or review agent supply-chain exposure.

## Choose The Scan Target

`--include-posture` is included by default in the commands below so
scanner-side hygiene findings (mutable install refs, insecure
transport, missing remote auth) surface alongside advisory matches.
Posture findings never affect `--fail-on` exit codes. Drop the flag
for an advisory-only scan.

- For the user's active Claude Code setup, run an endpoint scan:

```bash
uvx openaca@latest scan endpoint -v --include-posture
```

- If the user names a project path or asks to include project-local
  agent configuration, pass `--project`:

```bash
uvx openaca@latest scan endpoint --project /path/to/project -v --include-posture
```

- For a repository-only scan, run repo scan with the repo path as target:

```bash
uvx openaca@latest scan repo --target /path/to/repo -v --include-posture
```

If `uvx` is unavailable but `openaca` is installed, use the same command
without the `uvx` prefix.

## Reporting

Summarize:

- number of active plugins and total components scanned,
- MCP servers, skills, hooks, commands, and plugins observed,
- findings by severity,
- whether project-local configuration was included,
- the exact command run.

Do not claim "safe" when there are no findings. Say:

> No findings means no matching OpenACA advisory and no enabled
> posture finding in the scanned scope. It is not a claim that the
> component is safe.

## Safety

Do not edit settings, remove plugins, disable MCP servers, or install
updates unless the user explicitly asks. Treat scan output as evidence
for discussion and triage.
