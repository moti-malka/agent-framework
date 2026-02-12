"""
Challenge 02 — Build File Reading Tools
========================================
MCP gives you access to the repo, but your scanning agents will also
need custom tools to process file contents programmatically.

Your task: Create tools that read files from the repository via MCP
and return their contents in a format that's easy for agents to analyze.

Export:
    read_repo_file   — a tool that reads a single file's contents
    list_repo_files  — a tool that lists all files in the repository
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import _paths  # noqa: F401

import asyncio
import os
import nest_asyncio
nest_asyncio.apply()

from dotenv import load_dotenv
from agent_framework import tool, ChatAgent
from typing import Annotated
from pydantic import Field

from shared_models import GITHUB_REPO, create_mcp_client, create_chat_client

load_dotenv()

chat_client = create_chat_client()
chat_client_mcp = create_mcp_client()

# Import your MCP tool from challenge 01
from challenge_01_repo_access import github_mcp_tool


# ═════════════════════════════════════════════════════════════════════
# TODO: Create a tool that lists all files in the repository
#
# This tool should use an agent with the GitHub MCP tool to get a
# complete file listing. The output should be a clean list of
# relative file paths.
#
# Think about:
#   - How can an agent with MCP discover the repository tree?
#   - What format should the output be for downstream agents?
#
# Decorate with @tool and assign to: list_repo_files
# ═════════════════════════════════════════════════════════════════════

# list_repo_files = ...


# ═════════════════════════════════════════════════════════════════════
# TODO: Create a tool that reads a single file from the repository
#
# Given a relative file path (e.g., "app.py" or "utils/crypto.py"),
# this tool should return the full file contents as a string.
#
# Think about:
#   - How to use the MCP tool to fetch file contents
#   - What to return if the file doesn't exist
#   - Should the tool include the file path in its output for context?
#
# Decorate with @tool and assign to: read_repo_file
# ═════════════════════════════════════════════════════════════════════

# read_repo_file = ...


# ─── Test (DO NOT MODIFY) ────────────────────────────────────────────
async def test_challenge_02():
    print("📂 Testing file listing tool...")
    files_result = await list_repo_files()
    print(f"   Found files: {files_result[:500]}...")

    print("\n📄 Testing file reading tool...")
    content = await read_repo_file("app.py")
    print(f"   app.py length: {len(content)} characters")
    assert len(content) > 0, "File content should not be empty"

    print("\n✅ Challenge 02 complete — your file tools are working!")

if __name__ == "__main__":
    asyncio.run(test_challenge_02())
