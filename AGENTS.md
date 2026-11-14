# Instructions for repository agents

## Scope

This repository contains a deployment runbook and documentation-maintenance tooling. Editing this repository is different from executing the deployment on a Windows server. Do not run server installation, driver, firewall, reboot, or model-download commands on the machine hosting the checkout unless the user has actually requested deployment there.

For an authorized deployment task, read `AGENT_HANDOFF.md` and the complete HTML runbook before starting. Apply the user's existing authorization and instructions; do not manufacture additional approval steps for ordinary reversible work.

## Canonical files

- `vllm-windows11-deployment-runbook.html` is the complete guide and canonical source for the embedded deployment brief.
- `AGENT_HANDOFF.md` is generated from the HTML element with ID `code-agent`. Update the HTML first, then run `python3 tools/sync_agent_handoff.py`.
- `README.md` is the repository entry point. Keep its scope and status consistent with the guide.

## Editing requirements

- Preserve the runbook's single-file, offline-readable form. Do not introduce external fonts, scripts, styles, or required runtime dependencies.
- Keep PowerShell, Bash, Python, and configuration examples clearly labeled. Escape code correctly inside HTML so copied text remains valid.
- Maintain existing section IDs, internal navigation, copy targets, and responsive/print layouts, or update all dependent references together.
- Verify changing technical claims against primary documentation. Record model/runtime compatibility and distinguish estimates from measurements.
- Never imply that a server deployment, benchmark, or reboot/recovery test passed without actual evidence from that server.
- Keep API keys, tokens, private data, model weights, logs, and local deployment evidence out of commits. Do not print credentials during diagnostics.
- Do not add or change the repository's license without the owner's instruction.
- Keep the project lightweight. A build system, hosted service, package installation, or model download is not required to maintain the HTML or the synchronization helper.

## Verification

Run `python3 tools/sync_agent_handoff.py --check` after changes. When editing HTML or embedded commands, verify the affected internal links/copy targets, browser rendering, and command syntax as appropriate. Do not execute the deployment examples as a documentation test.

Before committing, inspect the staged diff and confirm that only the intended documentation/tooling files are included. Preserve existing remote history and never force-push without explicit authorization.
