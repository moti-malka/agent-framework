# Challenge 3: Shared Memory & Vulnerability Tracking 🧠

**Duration:** 20 minutes

Before building scanner agents, you need a **shared memory system** that tracks which files have been scanned and what vulnerabilities were found. This memory is shared across ALL scanner agents (Challenges 4–8) and is the source of truth for the final scoring.

## Learning Objectives

- Build a `ContextProvider` for shared state across agents
- Create `@tool` functions for recording findings
- Understand how context providers inject state into agent conversations

## Architecture

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│   Secrets    │   │  Code Vuln   │   │    Infra     │
│   Scanner    │   │   Scanner    │   │   Scanner    │
└──────┬───────┘   └──────┬───────┘   └──────┬───────┘
       │                  │                  │
       └──────────────────┼──────────────────┘
                          ▼
                 ┌────────────────┐
                 │  ScanMemory    │
                 │  (shared)      │
                 │                │
                 │ files_covered  │
                 │ vulnerabilities│
                 └────────────────┘
```

## Key Concepts

### ContextProvider

A `ContextProvider` has two hooks:
- **`invoking()`** — Called BEFORE an agent runs. Returns a `Context` telling the agent what's already been scanned.
- **`invoked()`** — Called AFTER an agent runs. Parses structured vulnerability JSON from the response as a backup.

### Why This Matters

The final workflow (Challenge 10) scores results based on what's **in memory** — not the agent's text output. Every scanner must call `report_vulnerability()` and `mark_file_scanned()` to register findings.

## Step-by-Step Instructions

### What You Need to Build

1. **`ScanMemory`** — A `ContextProvider` class with:
   - `files_covered: set[str]` — which files have been analyzed
   - `vulnerabilities: list[dict]` — findings with keys: `file`, `start_line`, `end_line`, `description`, `scanner`
   - `reset()` — clears all state
   - `_add_vuln()` — adds a vulnerability (deduplicates by file + line range)
   - `invoking()` / `invoked()` hooks

2. **`report_vulnerability`** — A `@tool` that records a single finding to memory
3. **`mark_file_scanned`** — A `@tool` that marks a file as analyzed

### Exports

| Variable | Type | Description |
|----------|------|-------------|
| `scan_memory` | `ScanMemory` | Shared ContextProvider instance |
| `report_vulnerability` | `@tool` function | Records a vulnerability to memory |
| `mark_file_scanned` | `@tool` function | Marks a file as scanned |

## Testing

```bash
cd workshop/challenge-3
python challenge_03_memory.py
```

**Expected output**: Vulnerabilities are recorded and deduplicated correctly.

## Resources

- **Challenge file**: [`challenge_03_memory.py`](./challenge_03_memory.py)
- **Agent Framework Context Providers**: [aka.ms/agent-framework](https://aka.ms/agent-framework)
