# Challenge 10: Orchestrated Security Workflow 🎯

**Duration:** 30 minutes

You've built all the components. Now wire them together into a **complete, orchestrated security scanning workflow** that coordinates all four scanner agents to produce a comprehensive security report.

## Learning Objectives

- Choose and implement a workflow orchestration pattern
- Coordinate multiple specialized agents into a unified pipeline
- Produce a scored JSON security report

## Architecture

```
                    ┌─────────────────┐
                    │  Workflow        │
                    │  Manager         │
                    └────────┬────────┘
           ┌─────────┬──────┴──────┬─────────┐
           ▼         ▼             ▼         ▼
    ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
    │ Secrets  │ │ Code     │ │ Infra    │ │ Auth/    │
    │ Scanner  │ │ Vuln     │ │ Scanner  │ │ Crypto   │
    │          │ │ Scanner  │ │          │ │ Scanner  │
    └──────┬───┘ └──────┬───┘ └──────┬───┘ └──────┬───┘
           └─────────┬──────┴──────┬─────────┘
                     ▼
              ┌──────────────┐
              │  ScanMemory  │
              │  (shared)    │
              └──────────────┘
                     ▼
              ┌──────────────┐
              │  JSON Report │
              └──────────────┘
```

## Orchestration Patterns

Choose one of these Agent Framework workflow builders:

| Pattern | Builder | Best For |
|---------|---------|----------|
| **Magentic** | `MagenticBuilder` | Manager dynamically delegates to specialist agents |
| **Group Chat** | `GroupChatBuilder` | Agents collaborate and cross-check findings |
| **Handoff** | `HandoffBuilder` | Agents pass control to each other in a chain |
| **Concurrent** | `ConcurrentBuilder` | All agents run in parallel simultaneously |

## Step-by-Step Instructions

### What You Need to Build

1. **`TASK_PROMPT`** — Main scanning task description for the workflow
2. **`FINAL_ANSWER_PROMPT`** — Instructions for how the manager wraps up
3. **`security_workflow`** — The complete orchestrated workflow

### How the Report Works

The test function uses `build_workflow_report()` (already provided) to convert
`scan_memory` into a typed `WorkflowReport` Pydantic model matching
[`expected_workflow_output.json`](../expected_workflow_output.json):

```python
WorkflowReport(
    workshop_id="agent-framework-security-scan",
    timestamp="...",
    repository="galshohat/vulnerable-app",
    scan_summary=ScanSummary(total_vulnerabilities=..., files_scanned=..., scanners_used=[...]),
    vulnerabilities=[Vulnerability(file=..., start_line=..., end_line=..., description=...), ...],
    files_covered=["app.py", "auth.py", ...],
    scanner_breakdown={"SecretsScanner": ScannerFindings(findings=11, files=[...]), ...},
)
```

The report is serialised with `report.model_dump()` and saved to
`workshop/challenge_10_output.json`.

### Think About

- Which orchestration pattern fits best for independent scanners?
- How should the manager ensure ALL 4 scanners are activated?
- What should `FINAL_ANSWER_PROMPT` tell the manager to produce?
- How do you prevent the manager from stalling?

### Exports

| Variable | Type | Description |
|----------|------|-------------|
| `TASK_PROMPT` | `str` | Main scanning task description |
| `FINAL_ANSWER_PROMPT` | `str` | Instructions for final report |
| `security_workflow` | Workflow | Complete orchestrated workflow |

## Testing & Scoring

```bash
cd workshop/challenge-10
python challenge_10_workflow.py
```

The test automatically saves results to `workshop/challenge_10_output.json`.

### Achievement Tiers

| Tier | Percentage | Badge | Description |
|------|------------|-------|-------------|
| **Diamond** | 90%+ | 💎 | Security expert! Near-perfect detection |
| **Gold** | 75-89% | 🥇 | Excellent! Found most vulnerabilities |
| **Silver** | 50-74% | 🥈 | Good job! Covered major security issues |
| **Bronze** | 25-49% | 🥉 | Nice start! Keep scanning more files |

### Tips for Higher Scores

1. **Scan ALL files** — don't skip subdirectories (`deploy/`, `utils/`, `api/`, `.github/`)
2. **Use ALL 4 scanners** — each covers different vulnerability types
3. **Report line ranges accurately** — include context, not just single lines
4. **Ensure scanners call `report_vulnerability()`** — memory is what gets scored

## Resources

- **Challenge file**: [`challenge_10_workflow.py`](./challenge_10_workflow.py)
- **Expected output format**: [`expected_workflow_output.json`](../expected_workflow_output.json)
- **Security Guide**: [`SECURITY_GUIDE.md`](../SECURITY_GUIDE.md)
