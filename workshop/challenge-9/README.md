# Challenge 9: Observability Middleware 📡

**Duration:** 15 minutes

In production, you need visibility into what your scanning agents are doing: which files they're reading, which tools they're calling, how long each scan takes, and what errors occur. Middleware provides this audit trail.

## Learning Objectives

- Build middleware that wraps agent execution with logging
- Build middleware that wraps individual tool/function calls
- Understand the `AgentRunContext` and `FunctionInvocationContext` patterns

## Key Concepts

### Agent Framework Middleware

Middleware wraps execution at two levels:

```
┌─────────────────────────────────────────┐
│  agent_logging_middleware               │
│  ┌───────────────────────────────────┐  │
│  │  Agent Processing                 │  │
│  │  ┌─────────────────────────────┐  │  │
│  │  │ tool_logging_middleware     │  │  │
│  │  │  ┌───────────────────────┐  │  │  │
│  │  │  │ Tool Execution       │  │  │  │
│  │  │  └───────────────────────┘  │  │  │
│  │  └─────────────────────────────┘  │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

- **Agent middleware**: Wraps the entire agent run (start → finish)
- **Tool middleware**: Wraps each individual tool/function call

## Step-by-Step Instructions

### What You Need to Build

1. **`agent_logging_middleware`** — Logs agent start (with message count), times execution, logs completion (with duration)
2. **`tool_logging_middleware`** — Logs which tool is called, its arguments, and the result (truncated if long)

### Middleware Signatures

```python
async def agent_logging_middleware(
    context: AgentRunContext,
    next: Callable[[AgentRunContext], Awaitable[None]],
) -> None:
    # Log start, call next(context), log end

async def tool_logging_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    # Log tool name + args, call next(context), log result
```

### Exports

| Variable | Type | Description |
|----------|------|-------------|
| `agent_logging_middleware` | Middleware function | Logs agent execution lifecycle |
| `tool_logging_middleware` | Middleware function | Logs individual tool invocations |

## Testing

```bash
cd workshop/challenge-9
python challenge_09_middleware.py
```

**Expected output**: Detailed logs showing agent activation, tool calls with arguments, and execution timing.

## Resources

- **Challenge file**: [`challenge_09_middleware.py`](./challenge_09_middleware.py)
- **Agent Framework Docs**: [aka.ms/agent-framework](https://aka.ms/agent-framework)
