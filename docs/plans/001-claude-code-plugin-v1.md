# Claude Code Plugin V1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a public Claude Code plugin that gives users explicit OpenACA scan, Agent BOM, explanation, and triage workflows without embedding scanner logic.

**Architecture:** The plugin is a thin wrapper around the published `openaca` CLI. Claude Code skills provide the user-facing workflow; the main OpenACA repository remains the source of truth for scanning, advisory matching, posture rules, and Agent BOM schema. V1 has no hooks, monitors, MCP server, blocking behavior, or background execution.

**Tech Stack:** Claude Code plugin manifest, Claude Code skills, `uvx openaca`, Python 3 standard-library validation.

---

### Task 1: Create Plugin Metadata

**Files:**
- Create: `.claude-plugin/plugin.json`
- Create: `.claude-plugin/marketplace.json`
- Create: `README.md`
- Create: `LICENSE`
- Create: `.gitignore`

- [x] **Step 1: Add the plugin manifest**

Create `.claude-plugin/plugin.json` with the plugin name `openaca`, version `0.1.0`, Apache-2.0 license metadata, repository URL, homepage URL, and security/supply-chain keywords.

- [x] **Step 2: Add the custom marketplace catalog**

Create `.claude-plugin/marketplace.json` with one plugin entry named `openaca` whose source is the public GitHub repository `open-agent-security/openaca-claude-plugin`.

- [x] **Step 3: Add README installation and safety docs**

Document early install commands, required tools, available skills, and the V1 safety model: explicit invocation only, no hooks, no monitors, no MCP server, and no automatic settings changes.

- [x] **Step 4: Add license and ignores**

Add Apache-2.0 `LICENSE` and ignore `.DS_Store` plus local Claude files.

### Task 2: Add Explicit Workflow Skills

**Files:**
- Create: `skills/scan/SKILL.md`
- Create: `skills/bom/SKILL.md`
- Create: `skills/explain/SKILL.md`
- Create: `skills/triage/SKILL.md`

- [x] **Step 1: Add scan skill**

Create a `scan` skill that runs `uvx openaca scan endpoint -v`, `uvx openaca scan endpoint -v --project .`, or `uvx openaca scan repo --target .` depending on the user's requested scope.

- [x] **Step 2: Add Agent BOM skill**

Create a `bom` skill that runs `uvx openaca bom endpoint --output openaca-agent-bom.json`, `uvx openaca bom endpoint --project . --output openaca-agent-bom.json`, or `uvx openaca bom repo --target . --output openaca-agent-bom.json`.

- [x] **Step 3: Add explanation skill**

Create an `explain` skill that interprets OpenACA findings, Agent BOM entries, severity, confidence, and next steps without overstating evidence.

- [x] **Step 4: Add triage skill**

Create a `triage` skill that guides review after MCP, plugin, skill, hook, command, or settings changes, and asks before making modifications.

### Task 3: Add Scaffold Validation

**Files:**
- Create: `scripts/validate_plugin.py`

- [x] **Step 1: Validate metadata**

Read `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`; fail if either name is not `openaca`.

- [x] **Step 2: Validate skill set**

Fail unless exactly four skills exist: `scan`, `bom`, `explain`, and `triage`.

- [x] **Step 3: Guard V1 safety boundary**

Fail if the repository contains `hooks/`, `monitors/`, `.mcp.json`, or `bin/`.

- [x] **Step 4: Run validation**

Run:

```bash
python3 scripts/validate_plugin.py
```

Expected output:

```text
plugin scaffold ok
```

### Task 4: Validate With Claude Code

**Files:**
- No file changes expected.

- [x] **Step 1: Run Claude plugin validation if available**

Run:

```bash
claude plugin validate .
```

Expected: Claude Code accepts the plugin structure. If the local Claude
Code version does not support this command, record the unsupported
command output in the PR and rely on `scripts/validate_plugin.py`.

### Task 5: Publish Initial Repo State

**Files:**
- All files above.

- [x] **Step 1: Commit the initial plugin**

Run:

```bash
git add .
git commit -m "Add safe OpenACA Claude Code plugin wrapper"
```

- [x] **Step 2: Push main**

Run:

```bash
git push -u origin main
```
