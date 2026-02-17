"""
Challenge 06 — Structured Vulnerability Output
===============================================
Free-text scan results are useful but hard to compare and aggregate.
Using response_format, you can force an agent to produce structured
output that matches a Pydantic model.

Your task: Create an agent that scans for secrets (like Challenge 05)
but outputs a structured VulnerabilityList AND reports findings to memory.

⚠️ IMPORTANT: The agent should BOTH:
  1. Call report_vulnerability for each finding (stored in memory)
  2. Produce structured output via response_format (for display/logging)

Export:
    structured_scanner  — an agent that returns structured Vulnerability findings
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import _paths  # noqa: F401

import asyncio
import os
import nest_asyncio
nest_asyncio.apply()

from dotenv import load_dotenv
from agent_framework import Agent

from shared_models import GITHUB_REPO, Vulnerability, VulnerabilityList, create_mcp_client, create_chat_client

load_dotenv()

chat_client = create_chat_client()
chat_client_mcp = create_mcp_client()

# Import tools from previous challenges
from challenge_01_repo_access import github_mcp_tool
from challenge_02_file_tools import read_repo_file, list_repo_files
from challenge_03_memory import scan_memory, report_vulnerability, mark_file_scanned
from challenge_04_middleware import agent_logging_middleware, tool_logging_middleware


# ═════════════════════════════════════════════════════════════════════
# TODO: Create a structured_scanner agent
#
# This agent should do the same work as the secrets scanner from
# Challenge 05, but ALSO produce structured output matching the
# VulnerabilityList model.
#
# Think about:
#   - How do you make an agent return structured JSON output?
#     (Hint: use the response_format parameter)
#   - The agent needs the same file reading tools AND memory tools
#   - Instructions should guide the agent to:
#     1. Call report_vulnerability for each finding (→ memory)
#     2. Produce a final VulnerabilityList JSON response
#   - Use context_providers=[scan_memory]
#   - Use middleware=[agent_logging_middleware, tool_logging_middleware]
#
# Assign to: structured_scanner
# ═════════════════════════════════════════════════════════════════════

structured_scanner = None  # Replace with your implementation


# ─── Test (DO NOT MODIFY) ────────────────────────────────────────────
async def test_challenge_06():
    assert structured_scanner is not None, "structured_scanner is not set"

    scan_memory.reset()

    print("📊 Running structured scanner...")
    result = await structured_scanner.run(
        f"Scan the repository {GITHUB_REPO} for hardcoded secrets. "
        f"Call report_vulnerability for each finding. "
        f"Return structured vulnerability findings."
    )

    # Parse the structured output
    findings = VulnerabilityList.model_validate_json(result.text)

    print(f"\n📊 Structured output: {len(findings.vulnerabilities)} vulnerabilities")
    for v in findings.vulnerabilities[:5]:
        print(f"   {v.file}:{v.start_line}-{v.end_line} — {v.description[:60]}")

    print(f"\n🧠 Memory: {len(scan_memory.vulnerabilities)} vulnerabilities")
    print(f"📂 Files covered: {scan_memory.files_covered}")

    assert len(findings.vulnerabilities) > 0, "Should find at least one vulnerability"
    print("\n✅ Challenge 06 complete — structured output working!")

if __name__ == "__main__":
    asyncio.run(test_challenge_06())
