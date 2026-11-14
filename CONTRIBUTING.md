# Contributing

Keep this repository useful as a shareable guide and an actionable deployment handoff.

## Edit the source

1. Update `vllm-windows11-deployment-runbook.html` for changes to the complete guide or embedded agent brief.
2. Regenerate the Markdown handoff with `python3 tools/sync_agent_handoff.py`.
3. Update `README.md` if the scope, workflow, or repository structure changes.

Keep the HTML self-contained. Readers should be able to download one file and use it without a build step or network connection. External source links and deployment downloads can still require the network.

## Review technical changes

- Prefer official documentation and model cards. Check that examples apply to the selected GPU architecture, OS, and stable runtime version.
- Label the command's execution environment. Preserve correct shell syntax and HTML escaping.
- Separate planning figures and hypothetical layouts from measurements on the actual server.
- Preserve private inference bindings and the distinction between the local pilot and the business access layer.
- Record limitations and unresolved acceptance targets without claiming an untested deployment is ready.

## Check before publishing

```bash
python3 tools/sync_agent_handoff.py --check
git diff --check
git diff --cached --check
```

For HTML changes, open the file locally at desktop and narrow widths. Check section navigation, command copying, checklist controls, and print preview. For command changes, perform syntax checks without running installation, driver, model-download, or host-configuration operations on an unrelated machine.

Review the exact staged files and diff for credentials, private prompts/documents, server identifiers, model weights, caches, or logs. Ignore patterns are an aid rather than proof that a commit contains no sensitive data.

No project license has been selected. License changes require the owner's instruction; referenced tools and models retain their own terms.
