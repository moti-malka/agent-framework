"""
Challenge 09 — Observability Middleware
=======================================
In production, you need visibility into what your scanning agents
are doing: which files they're reading, which tools they're calling,
how long each scan takes, and what errors occur.

Your task: Build middleware that logs agent execution and tool calls,
providing an audit trail of the entire scanning process.

Export:
    agent_logging_middleware    — middleware that logs agent runs
    tool_logging_middleware     — middleware that logs tool invocations
"""

import asyncio
import os
import time
import nest_asyncio
nest_asyncio.apply()

from dotenv import load_dotenv
from agent_framework import (
    AgentRunContext, FunctionInvocationContext,
    ChatAgent
)
from typing import Callable, Awaitable

from shared_models import GITHUB_REPO, create_mcp_client, create_chat_client

load_dotenv()

chat_client = create_chat_client()
chat_client_mcp = create_mcp_client()

# Import tools from previous challenges
from challenge_02_file_tools import read_repo_file, list_repo_files


# ═════════════════════════════════════════════════════════════════════
# TODO: Create agent_logging_middleware
#
# This middleware wraps the entire agent execution. It should:
#   - Log when an agent starts processing (with message count)
#   - Time how long the agent takes
#   - Log when the agent finishes (with duration)
#
# Middleware signature:
#   async def agent_logging_middleware(
#       context: AgentRunContext,
#       next: Callable[[AgentRunContext], Awaitable[None]],
#   ) -> None:
#
# Think about:
#   - What information is available on AgentRunContext?
#   - How do you pass control to the actual agent? (call next)
#   - Where do you measure start/end time?
#
# Assign to: agent_logging_middleware
# ═════════════════════════════════════════════════════════════════════

agent_logging_middleware = None  # Replace with your implementation


# ═════════════════════════════════════════════════════════════════════
# TODO: Create tool_logging_middleware
#
# This middleware wraps individual tool/function calls. It should:
#   - Log which tool is being called and with what arguments
#   - Log the tool's result (truncated if long)
#
# Middleware signature:
#   async def tool_logging_middleware(
#       context: FunctionInvocationContext,
#       next: Callable[[FunctionInvocationContext], Awaitable[None]],
#   ) -> None:
#
# Think about:
#   - What properties does FunctionInvocationContext have?
#   - How do you get the function name and arguments?
#   - How do you get the result after calling next()?
#
# Assign to: tool_logging_middleware
# ═════════════════════════════════════════════════════════════════════

tool_logging_middleware = None  # Replace with your implementation


# ─── Test (DO NOT MODIFY) ────────────────────────────────────────────
async def test_challenge_09():
    assert agent_logging_middleware is not None, "agent_logging_middleware is not set"
    assert tool_logging_middleware is not None, "tool_logging_middleware is not set"

    # Create a test agent with both middleware
    test_agent = chat_client.as_agent(
        name="MiddlewareTestAgent",
        instructions="You are a test agent. Use the provided tools to read files.",
        tools=[read_repo_file, list_repo_files],
        middleware=[agent_logging_middleware, tool_logging_middleware]
    )

    print("🔧 Testing middleware with a scan operation...\n")
    result = await test_agent.run(
        f"List the files in {GITHUB_REPO} and then read the contents of app.py"
    )
    print(f"\n📝 Agent response: {result.text[:200]}...")
    print("\n✅ Challenge 09 complete — observability middleware working!")

if __name__ == "__main__":
    asyncio.run(test_challenge_09())
