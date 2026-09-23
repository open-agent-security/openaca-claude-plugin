# OpenACA Claude Code Plugin

## What this repo is

OpenACA Claude Code Plugin adds explicit Claude Code workflows for
agent supply-chain security — running the open `openaca` scanner,
generating Agent BOMs, and explaining findings for Claude Code
plugins, skills, MCP servers, hooks, commands, and runtime components.
The plugin is a thin wrapper around the published OpenACA CLI; it
ships no scanner logic, hooks, background monitors, or MCP server.

## Common commands

```bash
bash scripts/install-hooks.sh         # one-time, install pre-push gate
python3 scripts/validate_plugin.py    # validate the plugin scaffold
claude plugin validate .              # full plugin validation (if Claude Code CLI installed)
```

## Architecture

This is a Claude Code plugin, not a Python application. The shipped
surface is:

- `.claude-plugin/plugin.json` + `marketplace.json` — manifest +
  marketplace listing.
- `skills/{inventory,scan,bom,explain,triage,sync}/SKILL.md` — the six
  namespaced commands users invoke (`/openaca:inventory` etc.).
- `scripts/validate_plugin.py` — local scaffold validator (also
  invoked by the pre-push hook and CI).

V1 is explicit-invocation only: no ambient hooks, no background
monitors, no `.mcp.json`, no `bin/`. `validate_plugin.py` enforces
that by failing if any of those paths appear.

The plugin is the preferred developer install path for Claude Code users.
Keep it thin over the published OpenACA CLI: plugin skills may guide users
to CLI primitives such as `bom endpoint`, `bom diff`, `scan endpoint`, and
`remote sync endpoint`, but must not embed scanner, diff, or upload logic.

## Repo conventions

- Skills follow Claude Code's `skills/<name>/SKILL.md` layout.
  Adding or removing a skill means updating `expected_skills` in
  `scripts/validate_plugin.py` and the README command list.
- All JSON in `.claude-plugin/` and `skills/` must parse — the
  pre-push hook and CI both run a syntax check.
- The plugin must not auto-install hooks or modify Claude Code
  settings; that's the V1 safety model documented in README.md.

## Code Review Rules

### Reviewer

- Review the full PR against its base branch. Report all qualifying
  findings together; do not deliberately reserve findings for later rounds.
- Report concrete, actionable defects with supported failure scenarios.
  Respect explicit scope decisions and accepted tradeoffs. Do not present
  speculative hardening or optional improvements as correctness defects.
- Calibrate priority by impact and urgency:
  - P0: critical, broadly applicable failure requiring immediate action.
  - P1: serious defect that should be fixed before this change lands.
  - P2: normal-priority defect eligible for automatic fixing.
  - P3: low-priority suggestion.
  Do not inflate priority to make a finding eligible for automatic fixing.
- On subsequent reviews, verify earlier fixes and inspect their effects on
  callers and dependencies. Older code within the PR remains reviewable.
- When review history supports it, identify a finding as:
  - Regression: introduced since the previous reviewed head.
  - Late discovery: present at a previously reviewed head but not reported.
  - Unresolved: a previously reported defect remains.
  If the history is unavailable or ambiguous, say so rather than guessing.
- Deduplicate by underlying defect and remedy, not by title. Refer to an
  existing thread for an unresolved defect instead of opening another one.

### Automated Fix Rules

- Automatically address actionable CI failures and verified P0, P1,
  and P2 findings, whether raised by an automated reviewer or a human.
- P3 findings require explicit human approval before fixing. Maintain one
  updated summary with links to their threads. Do not mark them resolved
  merely because they are deferred.
- Validate each finding against the current head and relevant contracts.
  If its reasoning or priority is wrong, explain why rather than applying
  it solely because a reviewer requested it. Surface unresolved disputes
  for human judgment.
- Fix the underlying invariant across relevant call sites. Test the
  failure class rather than only the reported example.
- Preserve accepted fixes and regression tests when reviewing a rebased PR or
  when replacing or simplifying its implementation. Remove a test only when
  the behavior it protects is intentionally changed or removed, and explain
  that decision.
- Batch related fixes into one tested update before requesting re-review.
  Avoid duplicate review requests for the same head.
- An automated fixer pushes ordinary commits to the existing PR branch and
  runs every required gate. It does not bypass gates, merge, rebase, or
  force-push, or change workflows, permissions, credentials, or branch
  protection. Report an environment failure or required rebase as a blocker.
- After pushing fixes, wait for CI and a completed review of the current
  head. Silence, an older review, or a running review is not clearance.
- Stop and ask for human input when the same failure repeats without progress.
- Stop the automatic fix cycle when CI passes, the current head has been
  reviewed, and no actionable P0/P1/P2 findings remain. A reviewer
  thumbs-up is not required.
- If only P3 findings remain, report:
  "Automatic fixes complete for <SHA>; CI passed. P3 suggestions await
  author approval."
  Do not claim the PR has no findings or has been approved.
- Count automated fix rounds since the most recent human-authored corrective
  commit, and stop when the count reaches seven. A round is a fix pushed as a
  new head for review; failed local validation does not count. A human-authored
  commit is corrective when it materially addresses the reported blockers; it
  resets the count to zero whether it arrives before or after the cap. Merging,
  rebasing, or otherwise synchronizing the branch does not reset the count. If
  PR and session history are insufficient to determine the count, stop and ask
  the author rather than guessing.
- At the cap, remain subscribed but make no edits. Put a message in the PR:
  "Review cap limit reached. @<author> Please take a step back to review the
  design and push a corrective commit to reset the review cap." In the same
  comment, explain why review has not converged and suggest concrete
  simplifications or spec/ADR changes. Resume only after the reset defined
  above.

