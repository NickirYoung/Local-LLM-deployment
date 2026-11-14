# Deployment agent handoff

Use this brief alongside the [complete HTML runbook](./vllm-windows11-deployment-runbook.html).

> Generated from the runbook's `code-agent` element. To change the brief, edit the HTML and run `python3 tools/sync_agent_handoff.py`.

Use this attached HTML runbook as the deployment specification for my local business LLM server. Read all sections, including troubleshooting and acceptance, before making changes.

Objective
Get a reproducible vLLM pilot running on my existing Windows 11 server, validate all available GPUs, compare sensible model layouts, and leave working startup, recovery, security boundaries, and deployment evidence. Continue through the authorized setup and testing; report precise external blockers instead of stopping at a plan.

Reported hardware (verify, do not assume detected)

- 2 x AMD EPYC 9684X, 96 cores / 192 threads each
- 24 x 64 GB DDR5-4800 system RAM
- 8 x NVIDIA GeForce RTX 4090, 24 GB each
- Windows 11; exact edition/build, motherboard, GPU topology, storage, and business workload are unknown

Execution approach

1. Start with read-only inventory. Record Windows edition/build, BIOS, CPU/core/thread counts, usable RAM, storage, NVIDIA driver, WSL version/distributions, GPUs, occupied ports, and existing workloads. Do not expose secrets in logs.
2. Verify the live upstream requirements for vLLM, Python, CUDA/driver compatibility, WSL, and the selected model. Use official sources linked in this document. Select a stable compatible release, record exact versions, and use its matching documentation. Do not silently adopt nightly builds or an unofficial Windows fork.
3. Use Ubuntu 24.04 in WSL2 as the initial Windows route. Reuse a suitable existing distribution or create a dedicated one. Preserve Windows, existing files, and unrelated services. Back up and merge configuration changes; do not overwrite .wslconfig or wsl.conf wholesale. Check active WSL work before restarting it.
4. Install the NVIDIA driver on Windows; do not install a Linux display driver inside WSL. Use a clean Python environment and Linux-native paths on adequately sized NVMe storage.
5. Validate GPU computation individually, then multi-GPU communication progressively. Start with one GPU and Qwen3-8B, then test groups of 2, 4, and 8 where available. Separate hardware/driver failures from model-memory failures.
6. Establish a pinned Qwen3.8-27B BF16 text-only baseline on four GPUs if the current stable release supports it. Compare PP4/TP1 with TP4/PP1. Trial two independent four-GPU instances if resources permit. Use a compatible, verified smaller model while resolving newer-model support rather than changing the host OS.
7. Evaluate the documented INT4 candidate in a separate configuration, starting with one or two GPUs and conservative limits. Preserve the BF16 baseline. Compare business quality, latency, memory, and concurrency. Do not assume the largest model is best.
8. Keep inference endpoints bound to loopback during the pilot. Prepare the business access layer with HTTPS, identity, per-user limits, endpoint allowlisting, and audit policy. Reuse existing approved infrastructure when possible. Keep a completed local pilot available while missing identity/domain/certificate choices are resolved. Do not expose raw vLLM publicly.
9. Configure systemd and Windows startup under the actual WSL-owning Windows account. Test readiness after a cold reboot with no interactive login, session closure, worker failure, and restart. Coordinate disruptive reboots with the owner and active work.
10. Test the actual business workload and document a concurrency/context/output envelope. Use synthetic benchmarks only as capacity probes. If the workload is still unknown, label the result a provisional pilot and list the missing acceptance targets.
11. Record model repository plus commit, software versions, launch configuration, service definitions, environment/driver facts, benchmark JSON, thermal/error observations, backup and rollback instructions. Keep credentials in private local files, not the report.
12. Verify whether this specific deployment fits the applicable model and GeForce software terms. Record any unresolved licensing question rather than making a legal determination.
13. If multi-GPU WSL is persistently unreliable, capture a minimal reproduction and recommend a native-Linux validation path. Do not reinstall Windows, repartition disks, purchase infrastructure, change business data access, or migrate the host OS without the owner's explicit authorization.

Required outputs

- Read-only inventory report and an implementation decision log.
- Working authenticated local API with verified model/version pins.
- Validated launcher(s), startup units/tasks, health checks, and recovery notes.
- Comparison of applicable GPU layouts with measured latency, throughput, memory, and errors.
- A business-readiness checklist with each item marked passed, failed, pending, or not applicable.
- A deployment manifest with exact versions and model commits; no secrets.
- A final account of what runs now, how to start/stop/update/roll back, where evidence is stored, and anything that still needs owner or integrator action.

Use normal judgment for reversible work within the owner's authorization. Ask concise questions only for information, access, or approvals that materially block the next action. Do useful independent work while awaiting answers. Never label untested commands, unmeasured throughput, or an unverified reboot path as validated.
