# Local LLM deployment

A practical runbook for evaluating and deploying a local business LLM with **vLLM on Windows 11 through Ubuntu in WSL2**.

The complete guide is a single HTML file that works offline. It includes a deployment-agent brief, copyable commands, model and GPU layout comparisons, startup/recovery configuration, troubleshooting, acceptance checks, and primary-source links.

**Status:** documentation and deployment examples. The guide's HTML, copy controls, and embedded Bash/Python syntax have been checked; the actual server deployment and performance have not been verified. Review the current upstream requirements before executing the examples.

## Open the guide

Download [the HTML runbook](./vllm-windows11-deployment-runbook.html) using GitHub's **Download raw file** control, then open the downloaded file in a browser. GitHub's file view displays the source rather than the rendered guide. Share the HTML file directly; it has no external fonts, scripts, or styles.

Alternatively, clone the repository and open the guide from Windows PowerShell:

```powershell
git clone https://github.com/NickirYoung/Local-LLM-deployment.git
cd Local-LLM-deployment
Start-Process .\vllm-windows11-deployment-runbook.html
```

The guide also has **Copy agent handoff** and **Print / Save PDF** controls. Its checklist state stays in the reader's browser and does not travel with the file.

## Give it to a deployment agent

Provide both files to the agent that can access the intended Windows server:

- [AGENT_HANDOFF.md](./AGENT_HANDOFF.md) — the deployment brief in plain Markdown.
- [vllm-windows11-deployment-runbook.html](./vllm-windows11-deployment-runbook.html) — the full specification, commands, references, and acceptance criteria.

Suggested opening instruction:

> Read AGENT_HANDOFF.md and the complete HTML runbook. Inventory the intended server first, then carry out the authorized setup and validation. Preserve existing data and services, record evidence, and distinguish a working local pilot from a business-ready deployment.

[AGENTS.md](./AGENTS.md) gives coding agents instructions for maintaining this repository. It is separate from the deployment handoff.

## Target hardware

| Component | Reported configuration |
| --- | --- |
| Operating system | Windows 11; edition and build still need verification |
| CPU | 2 × AMD EPYC 9684X; 192 cores / 384 threads total |
| System RAM | 24 × 64 GB DDR5-4800; 1,536 GB nominal |
| GPU | 8 × NVIDIA GeForce RTX 4090; 24 GB per card |
| Aggregate GPU memory | 192 GB across eight distinct GPU memories |
| Motherboard, chassis, storage, power | To be inventoried and validated |

This is a reported configuration, not an observed inventory. The guide addresses the 4090's interconnect limitations, Windows edition limits, PCIe/NUMA layout, model-memory budgeting, and power/cooling requirements with linked references.

## Deployment sequence

1. **Inventory and assess:** verify the OS edition, detected hardware, storage, physical integration, driver, and existing workloads.
2. **Establish the foundation:** configure WSL2/Ubuntu and an isolated Python environment, then prove computation on each GPU.
3. **Validate inference:** start a one-GPU smoke test and progress through the required multi-GPU groups.
4. **Compare model layouts:** pin a compatible model/runtime, compare pipeline and tensor parallelism, and evaluate independent replicas and quantized candidates.
5. **Prepare business access:** add the application, identity, HTTPS, route restrictions, and permission-aware retrieval where required.
6. **Verify operation:** test unattended startup, recovery, quality, capacity, sustained behavior, and rollback before recording business readiness.

The initial examples use Qwen3-8B for the smoke test and Qwen3.8-27B for a larger evaluation. These are documented candidates, not guaranteed quality or capacity recommendations. Check the model cards and compatible stable vLLM release at execution time.

## Repository layout

```text
.
├── README.md
├── AGENTS.md                              # Instructions for repository-editing agents
├── AGENT_HANDOFF.md                       # Generated deployment brief
├── CONTRIBUTING.md
├── .gitattributes
├── .gitignore
├── tools/
│   └── sync_agent_handoff.py              # Standard-library documentation helper
└── vllm-windows11-deployment-runbook.html  # Canonical complete runbook
```

## Maintain the documentation

The HTML is the canonical source for the complete guide and embedded deployment brief. After editing that brief, regenerate its Markdown copy:

```bash
python3 tools/sync_agent_handoff.py
```

Check that the two copies agree:

```bash
python3 tools/sync_agent_handoff.py --check
```

The helper needs only Python's standard library and does not execute deployment commands, contact the network, or install anything. Open the HTML in a browser to review layout, copy controls, links, and print styles. See [CONTRIBUTING.md](./CONTRIBUTING.md) for the review checklist.

## Credentials and local artifacts

Keep API keys, tokens, environment files, model weights, private prompts, document corpora, and server evidence out of the repository. The ignore rules cover common local artifacts, but inspect every staged change before publishing. The example `vllm.env` belongs on the deployment server and must not be committed.

## Sources and licensing

The runbook includes a [primary-source reference section](./vllm-windows11-deployment-runbook.html#sources). Its preparation date is **14 November 2026**; retain the documentation matching the versions actually deployed.

No project-wide open-source license has been selected for this repository. Referenced software, models, and drivers retain their own licenses and terms. This repository does not bundle model weights, vLLM, or NVIDIA drivers.
