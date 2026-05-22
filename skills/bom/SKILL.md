---
name: bom
description: Generate an OpenACA Agent BOM when the user asks for a bill of materials, Agent BOM, inventory export, or structured list of agent components.
argument-hint: "[endpoint|repo] [optional output path]"
allowed-tools:
  - Bash
  - Read
---

# OpenACA Agent BOM

Use this skill when the user asks for an Agent BOM, a structured
inventory, a CycloneDX export, or a reusable snapshot of agent
composition.

## Generate A BOM

- For the current Claude Code endpoint:

```bash
uvx openaca bom endpoint -v --output openaca-agent-bom.json
```

- To include project-local configuration:

```bash
uvx openaca bom endpoint -v --project /path/to/project --output openaca-agent-bom.json
```

- For a repository target:

```bash
uvx openaca bom repo -v --target /path/to/repo --output openaca-agent-bom.json
```

If `uvx` is unavailable but `openaca` is installed, use the same command
without the `uvx` prefix.

## Explain The Artifact

Describe the Agent BOM as composition data: what components exist, how
they are related, and where they were observed. Keep findings separate:
scan results and advisories reference BOM components, but the BOM itself
is inventory.

When useful, suggest scanning the stored BOM with the current corpus:

```bash
uvx openaca scan bom -v --input openaca-agent-bom.json
```

## Safety

Do not paste the full BOM into chat unless the user asks. BOMs can
contain local paths, URLs, component names, and source provenance. Prefer
a concise summary and leave the file in the workspace.
