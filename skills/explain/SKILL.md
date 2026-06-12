---
name: explain
description: Explain OpenACA findings, Agent BOM entries, scan output, severity, confidence, source provenance, and suggested next steps.
argument-hint: "[finding text, advisory id, or BOM component]"
allowed-tools:
  - Bash
  - Read
---

# Explain OpenACA Output

Use this skill when the user asks what an OpenACA finding means, why a
component was reported, how severe an issue is, or what to do next.

## Explanation Shape

For each finding, explain:

- the affected component and component type,
- the observed source or scan context,
- whether the evidence is an advisory match or posture finding,
- severity and confidence,
- why it matters for agent behavior,
- practical remediation or verification steps.

For Agent BOM entries, explain inventory and composition only. Do not
turn a BOM entry into a vulnerability unless scan output or an advisory
match supports that conclusion.

## Useful Commands

If the user provides a BOM and wants current advisory matching:

```bash
uvx --isolated --from openaca openaca scan bom --input openaca-agent-bom.json -v
```

`scan bom` returns advisory matches only. Posture findings need live
configuration (autoapprove lists, remote-auth, endpoint overrides)
that isn't preserved in the BOM — if the user asks about hygiene
findings on a BOM, point them at `scan endpoint --include-posture`
or `scan repo --include-posture` instead.

If the user wants a fresh endpoint scan (include posture so the
explanation can cover hygiene findings, not just advisory matches):

```bash
uvx --isolated --from openaca openaca scan endpoint -v --project . --include-posture
```

If `uvx` is unavailable but `openaca` is installed, use the same command
without the `uvx` prefix.

## Language

Be precise about evidence. "No findings" means no enabled OpenACA rule
matched in the scanned scope; it does not prove a component is safe.
Avoid overstating posture findings as confirmed compromise.
