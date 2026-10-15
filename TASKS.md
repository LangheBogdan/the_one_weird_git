# Task checklist

- [x] Inspect the workspace and read the Effect article.
- [x] Confirm the deliverable: task-based catalog, agent instructions, on-demand downloads.
- [x] Verify official sources for web, backend, database, API, mobile, and game tools.
- [x] Write a task-based catalog with minimal selections and optional alternatives.
- [x] Write agent instructions and a version-pinned reference download workflow.
- [x] Check links, consistency, and the final workspace contents.
- [x] Explain the core selection rules in `docs/core-ideas.html`.
- [x] Define the approval trigger: `docs/implementation-plan.md` frontmatter, rules in `docs/approval-trigger.md`.
- [ ] Write the skill that reads the trigger and adds the required references.

## Scope

Create reference documentation only. Do not clone repositories, install dependencies, initialize Git, or change anything outside this workspace.

## Verification

- All local Markdown links resolve; code fences are balanced; Bash examples pass syntax checking.
- Official repository pages and documentation were consulted on 2026-10-01. Source-reading limitations for Phaser and Babylon.js are recorded in `docs/mobile-game-sources.md`.
- Git subtree syntax was checked against official documentation and local help. Download/import commands were not executed.
- No `references/` or `repos/` directory exists; the selection log records zero downloads.
- On 2026-10-06 `git rev-parse HEAD` shows `36bff09c1376788436c4474cc6e71ccf6773dc55` on `main`, and `git status --short` was empty. The 2026-10-01 note that this folder was not a Git repository is out of date. `references/` and `repos/` still do not exist. No clone or `git subtree add` was run.
