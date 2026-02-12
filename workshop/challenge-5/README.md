# Challenge 5: Structured Vulnerability Output 📊

**Duration:** 15 minutes

Free-text scan results are useful but hard to compare and aggregate. Using `response_format`, you can force an agent to produce structured JSON output that matches a Pydantic model — making findings machine-readable.

## Learning Objectives

- Use `response_format` to enforce structured agent output
- Combine structured output with memory-based tracking
- Understand the `Vulnerability` and `VulnerabilityList` Pydantic models

## Key Concept: Dual Output

Your agent should produce output through **two channels**:

```
Agent Scan
  ├── Channel 1: report_vulnerability()  → stored in ScanMemory
  └── Channel 2: response_format=VulnerabilityList  → structured JSON output
```

Both are important:
- **Memory** is used for scoring in Challenge 10
- **Structured output** is used for display, logging, and downstream processing

## Step-by-Step Instructions

### What You Need to Build

A `structured_scanner` agent that:
- Scans for secrets (same domain as Challenge 4)
- Calls `report_vulnerability()` for each finding (→ memory)
- Produces a final `VulnerabilityList` JSON response via `response_format`
- Uses `context_provider=scan_memory`

### Think About

- How do you set `response_format` on a `ChatAgent`?
- Should the instructions tell the agent to produce JSON in a specific shape?
- How does this differ from Challenge 4's free-text scanner?

### Exports

| Variable | Type | Description |
|----------|------|-------------|
| `structured_scanner` | `ChatAgent` | Agent with structured `VulnerabilityList` output |

## Testing

```bash
cd workshop/challenge-5
python challenge_05_structured_output.py
```

**Expected output**: Parseable `VulnerabilityList` JSON with vulnerability file paths, line numbers, and descriptions.

## Resources

- **Challenge file**: [`challenges/challenge_05_structured_output.py`](../challenges/challenge_05_structured_output.py)
- **Pydantic Models**: Defined in [`challenges/shared_models.py`](../challenges/shared_models.py)
