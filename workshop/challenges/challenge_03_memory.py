"""
Challenge 03 — Scan Memory & Vulnerability Tracking
=====================================================
Before building scanner agents, you need a shared memory system that
tracks which files have been scanned and what vulnerabilities were found.

This memory will be shared across ALL scanner agents (Challenges 04–08).
The final workflow (Challenge 10) scores your results based on what
the memory contains — NOT the workflow's text output.

Your task:
  1. Build a ScanMemory ContextProvider that tracks files_covered and
     vulnerabilities found.
  2. Create @tool functions for agents to record their findings.

Export:
    scan_memory           — a ScanMemory ContextProvider instance
    report_vulnerability  — a @tool that records a vulnerability in memory
    mark_file_scanned     — a @tool that marks a file as analyzed
"""

import asyncio
import os
import json
import nest_asyncio
nest_asyncio.apply()

from dotenv import load_dotenv
from agent_framework import (
    ChatAgent, ChatMessage, ContextProvider, Context, tool
)
from collections.abc import MutableSequence, Sequence
from typing import Any, Annotated
from pydantic import Field

from shared_models import GITHUB_REPO, create_mcp_client, create_chat_client

load_dotenv()

chat_client = create_chat_client()

# Import file tools from Challenge 02
from challenge_02_file_tools import read_repo_file, list_repo_files


# ═════════════════════════════════════════════════════════════════════
# TODO 1: Create a ScanMemory ContextProvider
#
# This ContextProvider tracks scan progress across multiple agents:
#   - files_covered (set of str): which files have been analyzed
#   - vulnerabilities (list of dict): findings so far, each dict has
#     keys "file" (str), "start_line" (int), "end_line" (int), "description" (str)
#
# Required attributes:
#   self.files_covered: set[str]
#   self.vulnerabilities: list[dict]
#
# Required methods:
#   reset()  — clears files_covered and vulnerabilities
#   _add_vuln(file, start_line, end_line, description, scanner="unknown") — adds a vulnerability to memory
#     but only if the same (file, start_line, end_line) combo isn't already recorded
#     For single-line vulnerabilities, start_line == end_line.
#     Each vulnerability dict should have keys: "file", "start_line", "end_line", "description", "scanner"
#
# ContextProvider hooks:
#   invoking(messages, **kwargs) -> Context
#     Called BEFORE an agent runs. Return a Context with instructions
#     telling the agent what files are already covered and how many
#     vulnerabilities were found so far, so agents can avoid duplicate work.
#
#   invoked(request_messages, response_messages, **kwargs) -> None
#     Called AFTER an agent runs. Try to parse any structured vulnerability
#     JSON from the agent's response and add new findings to memory.
#     This is a backup for agents using response_format — they may
#     produce structured output without calling report_vulnerability.
#
# Assign the class to: ScanMemory
# Create a module-level instance: scan_memory = ScanMemory()
# ═════════════════════════════════════════════════════════════════════

# class ScanMemory(ContextProvider):
#     ...

scan_memory = None  # Replace with your implementation


# ═════════════════════════════════════════════════════════════════════
# TODO 2: Create a report_vulnerability tool
#
# A @tool-decorated function that records a single vulnerability in
# scan_memory. Scanner agents will call this for EACH finding.
#
# Parameters (use Annotated[type, Field(description=...)] ):
#   - file (str): relative file path where the vulnerability was found
#   - start_line (int): first line number of the vulnerability
#   - end_line (int): last line number (same as start_line for single-line issues)
#   - description (str): short description of the vulnerability
#   - scanner (str, optional): name of the scanner that found this (default="unknown")
#     Examples: "SecretsScanner", "CodeVulnScanner", "InfraScanner", "AuthCryptoScanner"
#
# The tool should:
#   - Call scan_memory._add_vuln(file, start_line, end_line, description, scanner)
#   - Also add the file to scan_memory.files_covered
#   - Return a confirmation string
#
# Assign to: report_vulnerability
# ═════════════════════════════════════════════════════════════════════

# @tool(...)
# def report_vulnerability(...):
#     ...


# ═════════════════════════════════════════════════════════════════════
# TODO 3: Create a mark_file_scanned tool
#
# A @tool-decorated function that marks a file as analyzed in memory.
# Agents should call this after reading a file, even if they found
# no vulnerabilities (so we track coverage).
#
# Parameters (use Annotated[type, Field(description=...)] ):
#   - file_path (str): relative file path that was analyzed
#
# Assign to: mark_file_scanned
# ═════════════════════════════════════════════════════════════════════

# @tool(...)
# def mark_file_scanned(...):
#     ...


# ─── Test (DO NOT MODIFY) ────────────────────────────────────────────
async def test_challenge_03():
    assert scan_memory is not None, "scan_memory is not set"
    assert report_vulnerability is not None, "report_vulnerability is not set"
    assert mark_file_scanned is not None, "mark_file_scanned is not set"

    # Reset memory
    scan_memory.reset()

    # Create a test agent that uses memory + tools
    test_agent = ChatAgent(
        chat_client=chat_client,
        name="MemoryTestAgent",
        instructions=(
            "You are a security scanner. Read the specified file and find "
            "hardcoded secrets. For EACH secret found, call report_vulnerability "
            "with the file path, line number, and a short description. "
            "After analyzing the file, call mark_file_scanned with the file path."
        ),
        tools=[read_repo_file, report_vulnerability, mark_file_scanned],
        context_provider=scan_memory,
    )

    print("🧠 Testing memory by scanning config.py...")
    result = await test_agent.run(
        f"Read config.py from {GITHUB_REPO} and report all hardcoded secrets. "
        f"Call report_vulnerability for each finding. "
        f"Call mark_file_scanned when done."
    )

    print(f"\n📊 Results:")
    print(f"   🧠 Vulnerabilities in memory: {len(scan_memory.vulnerabilities)}")
    print(f"   📂 Files covered: {scan_memory.files_covered}")

    assert len(scan_memory.vulnerabilities) > 0, \
        "Memory should have vulnerabilities after scanning"
    assert len(scan_memory.files_covered) > 0, \
        "Memory should track files covered"

    for v in scan_memory.vulnerabilities[:5]:
        print(f"   📌 {v['file']}:{v['start_line']}-{v['end_line']} — {v['description'][:60]}")

    print("\n✅ Challenge 03 complete — memory tracking is working!")


if __name__ == "__main__":
    asyncio.run(test_challenge_03())
