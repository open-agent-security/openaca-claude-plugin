---
name: sync
description: Configure, check, or run explicit OpenACA Cloud sync for a Claude Code endpoint.
argument-hint: "[configure|status|endpoint] [optional project path]"
allowed-tools:
  - Bash
  - Read
---

# OpenACA Cloud Sync

Use this skill when the user asks to connect OpenACA to Cloud, check sync
status, upload endpoint state, or share a local Agent BOM/fleet view.

Cloud sync is opt-in. Confirm before running an upload command.

## Configure

When the user wants to configure a Cloud token, do NOT run the configure
command as a Bash tool call, and do NOT pass `--token <value>` on the CLI:
either one embeds the secret in the tool invocation, the process argument
list, the shell history, and the session transcript.

Instead, tell the user to run the configure command themselves in a private
terminal session, outside of Claude — **without** `--token`. The CLI prompts
for the token with input hidden, so the secret never lands in argv or shell
history:

```
uvx --isolated --from openaca openaca remote configure
```

Once the user confirms the command succeeded, proceed to `status` or
`sync` to verify the connection.

Do not repeat token values back to the user. Do not include token values
in summaries or logs.

## Status

Check local remote configuration:

```bash
uvx --isolated --from openaca openaca remote status
```

## Sync Endpoint State

Run the normal endpoint sync first:

```bash
uvx --isolated --from openaca openaca remote sync endpoint
```

Include project-local Claude configuration when requested:

```bash
uvx --isolated --from openaca openaca remote sync endpoint --project .
```

Optional external scanners must remain explicit. If the user asks for
SkillSpector-backed observations, name the extra scanner in the command:

```bash
uvx --isolated --from openaca openaca remote sync endpoint --scanner nvidia-skillspector
```

If `uvx` is unavailable but `openaca` is installed, use the same command
without the `uvx` prefix.

## Reporting

Summarize:

- whether the command was configure, status, or sync,
- whether a project path was included,
- whether an external scanner was requested,
- any endpoint ID or Cloud URL reported by the CLI,
- the exact command run, with secrets redacted.

## Safety

Do not run sync implicitly after inventory or scan. Do not upload full
skill, plugin, MCP, or endpoint state unless the user explicitly asks.
