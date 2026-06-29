# Plugin-First Installation Spec

## Goal

Make the Claude Code plugin the preferred OpenACA installation path for
developer-led adoption, while keeping the plugin safe, explicit, and thin over
the published `openaca` CLI.

## Positioning

The plugin is the low-friction entry point for developers who want to inspect
their own coding-agent stack from inside Claude Code. MDM remains the
mandatory-coverage path for organizations that need enforced rollout, but it is
not the first experience.

The plugin should answer three developer questions:

1. What agent components are installed here?
2. Which components or findings deserve review?
3. How do I optionally share this endpoint state with OpenACA Cloud?

## User Workflows

## Two-Track Delivery

Plugin-first adoption needs two layers to evolve together:

- **Plugin UX track:** improve the Claude Code plugin as the preferred
  developer install path. This repository owns the skill surface,
  documentation, and safety boundary.
- **OpenACA CLI primitive track:** add local CLI operations that make the
  plugin useful without making every interaction run a full scan. The first
  primitive is `openaca bom diff`, which compares two local Agent BOMs and
  answers "what changed?" without advisory lookups.

The plugin remains a thin wrapper. It should call released CLI primitives as
they become available instead of embedding scanner or diff logic.

### Fast Local Inventory

Users need a fast, low-risk first command that does not feel like a stuck
scanner. The plugin should expose a dedicated inventory workflow that generates
an Agent BOM for the current endpoint or current project. This is the plugin's
default first recommendation for "what is installed?" questions.

The inventory workflow produces local artifacts only. It does not upload data
and does not claim that an inventory-only result is a vulnerability assessment.
When a previous BOM exists and the installed OpenACA CLI supports it, the
workflow may suggest `openaca bom diff --before <old> --after <new>` to show
component and composition changes before a deeper scan.

### Advisory And Posture Scan

Users still need the existing scan workflow for advisory and posture evidence.
The scan skill should clearly describe it as a deeper check than inventory.
It may query public vulnerability sources through the CLI and may take longer
than inventory.

Optional external scanners such as NVIDIA SkillSpector must remain explicit.
The plugin should not run them by default.

### Triage After Changes

When a user changes a plugin, MCP server, skill, hook, command, or settings
file, the plugin should guide a narrow review:

1. Identify what changed.
2. Run local inventory first when the user only needs component visibility.
3. Run scan when the user wants advisory or posture evidence.
4. Explain findings without overstating safety.

### Cloud Sync

Cloud upload should be opt-in and explicit. The plugin should expose a sync
workflow around the existing `openaca remote configure`, `openaca remote
status`, and `openaca remote sync endpoint` commands.

The sync workflow must:

- explain that upload crosses a local-to-cloud boundary,
- tell users not to paste tokens into public/shared sessions,
- avoid printing token values in summaries,
- recommend a normal sync without SkillSpector first,
- make SkillSpector sync an explicit opt-in.

## Non-Goals

This iteration does not add:

- background monitoring,
- automatic hooks,
- blocking or enforcement,
- an MCP server,
- embedded scanner logic,
- automatic Cloud upload,
- endpoint coverage guarantees.

Path-scoped scans such as "scan only this skill" or "scan this plugin" are
also deferred to the OpenACA CLI. They need selector semantics over BOM
occurrence keys and composition graph identities; the plugin should not invent
that logic locally.

## Plugin Surface

The plugin should provide six skills:

- `/openaca:inventory` - fast local Agent BOM/inventory workflow.
- `/openaca:scan` - deeper advisory/posture scan workflow.
- `/openaca:bom` - explicit Agent BOM generation/export workflow.
- `/openaca:explain` - explanation of findings and BOM entries.
- `/openaca:triage` - guided review after agent configuration changes.
- `/openaca:sync` - opt-in Cloud configuration/status/sync workflow.

`inventory` and `bom` overlap intentionally: `inventory` is the user-friendly
first-run workflow, while `bom` remains the artifact-focused export command.

## Safety

The plugin remains explicit-invocation only. It must not ship ambient execution
surfaces or mutate Claude Code settings. The local validator should continue to
fail if forbidden ambient paths are introduced.
