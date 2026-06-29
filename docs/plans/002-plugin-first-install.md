# Plugin-First Installation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the Claude Code plugin the preferred low-friction OpenACA install path by adding fast inventory and explicit Cloud sync workflows.

**Architecture:** Keep the plugin as a thin Claude Code skill bundle over the published `openaca` CLI. Add two skills (`inventory`, `sync`), update existing skill copy so inventory is the fast first step and external scanners remain opt-in, and extend scaffold validation to enforce the new six-skill surface. Treat BOM diff and future scoped scans as OpenACA CLI primitives that the plugin calls once released, not logic embedded in this repository.

**Tech Stack:** Claude Code plugin manifest, Claude Code skills, `uvx --isolated --from openaca openaca`, Python 3 standard-library validation tests.

---

### Task 1: Add Validation Coverage For The Plugin-First Surface

**Files:**
- Create: `tests/test_plugin_contract.py`

- [x] **Step 1: Write failing contract tests**

Add standard-library `unittest` tests that assert the plugin has exactly the six expected skills and that the README documents plugin-first usage plus optional Cloud sync.

- [x] **Step 2: Run tests and confirm RED**

Run `python3 -m unittest discover -s tests -v`. Expected: fail because `inventory` and `sync` skills do not exist yet and README lacks the new positioning.

### Task 1.5: Align The Design Note

**Files:**
- Modify: `docs/specs/plugin-first-install.md`

- [x] **Step 1: Document the two-track delivery model**

Record that this plugin owns the Claude Code UX while OpenACA CLI owns primitives such as `openaca bom diff` and future scoped scans.

### Task 2: Add New Skills

**Files:**
- Create: `skills/inventory/SKILL.md`
- Create: `skills/sync/SKILL.md`
- Modify: `skills/scan/SKILL.md`
- Modify: `skills/triage/SKILL.md`

- [x] **Step 1: Add inventory skill**

Create a fast local inventory workflow that runs `openaca bom endpoint` or `openaca bom endpoint --project .` and explains that the BOM is local inventory, not a safety verdict.

- [x] **Step 2: Add sync skill**

Create an opt-in Cloud workflow around `openaca remote configure`, `openaca remote status`, and `openaca remote sync endpoint`, with explicit privacy and token-handling guidance.

- [x] **Step 3: Update scan and triage skills**

Make scan read as the deeper advisory/posture path and make triage prefer inventory first when the user only asks what changed.

### Task 3: Update Plugin Docs And Validator

**Files:**
- Modify: `README.md`
- Modify: `CLAUDE.md`
- Modify: `scripts/validate_plugin.py`

- [x] **Step 1: Reposition install docs**

Update README so the plugin is presented as the preferred developer install path, with MDM/managed rollout described as later organizational coverage rather than first-run setup.

- [x] **Step 2: Update validator**

Change `expected_skills` from four skills to six: `inventory`, `scan`, `bom`, `explain`, `triage`, and `sync`.

- [x] **Step 3: Update repo conventions**

Update `CLAUDE.md` so future skill additions remember the six-skill surface and the plugin-first safety boundary.

### Task 4: Verify And Publish

**Files:**
- All modified files.

- [x] **Step 1: Run tests**

Run `python3 -m unittest discover -s tests -v`; expected pass.

- [x] **Step 2: Run scaffold validation**

Run `python3 scripts/validate_plugin.py`; expected `plugin scaffold ok`.

- [x] **Step 3: Run Claude validation if available**

Run `claude plugin validate .`; expected plugin validation pass. If the local Claude CLI does not support it, record the unsupported output.

- [ ] **Step 4: Commit, push, and open a ready PR**

Commit one logical change, push the branch, and open a ready PR.
