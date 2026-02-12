"""
Challenge 04 — Secrets Scanner Agent
=====================================
Hardcoded secrets are one of the most common and dangerous vulnerabilities.
API keys, passwords, and tokens committed to source code can be exploited
by anyone with access to the repository.

Your task: Build an agent that scans files for hardcoded secrets and
credentials, reporting each finding to the shared scan memory.

⚠️ IMPORTANT: Your agent MUST call report_vulnerability for every
finding and mark_file_scanned after analyzing each file. The final
workflow scores results from memory — not from agent text output.

Export:
    secrets_scanner  — an agent that detects hardcoded secrets
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import _paths  # noqa: F401

import asyncio
import os
import nest_asyncio
nest_asyncio.apply()

from dotenv import load_dotenv
from agent_framework import ChatAgent

from shared_models import GITHUB_REPO, create_mcp_client, create_chat_client

load_dotenv()

chat_client = create_chat_client()
chat_client_mcp = create_mcp_client()

# Import tools from previous challenges
from challenge_01_repo_access import github_mcp_tool
from challenge_02_file_tools import read_repo_file, list_repo_files
from challenge_03_memory import scan_memory, report_vulnerability, mark_file_scanned


# ═════════════════════════════════════════════════════════════════════
# TODO: Create a secrets_scanner agent
#
# This agent should:
#   - Read source code files from the repository
#   - Identify hardcoded secrets, API keys, passwords, tokens, and
#     credentials embedded in the code
#   - Call report_vulnerability for EACH finding
#   - Call mark_file_scanned after analyzing each file
#
# Think about:
#   - What tools does this agent need? (file tools + memory tools)
#   - What instructions would guide it to recognize different types
#     of secrets? (API keys, database passwords, encryption keys, etc.)
#   - Which files are most likely to contain secrets?
#   - The agent needs context_provider=scan_memory to see previous findings
#
# NOTE: Every secret is self-contained in its own file — no cross-file
# correlation is needed. Each file has secrets directly visible as
# string literals or variable assignments.
#
# Assign to: secrets_scanner
# ═════════════════════════════════════════════════════════════════════

secrets_scanner = None  # Replace with your implementation


# ─── Test (DO NOT MODIFY) ────────────────────────────────────────────
async def test_challenge_04():
    assert secrets_scanner is not None, "secrets_scanner is not set"

    scan_memory.reset()

    print("🔑 Running secrets scanner...")
    result = await secrets_scanner.run(
        f"Scan the repository {GITHUB_REPO} for hardcoded secrets, "
        f"API keys, passwords, tokens, and credentials. "
        f"Check all source code and configuration files. "
        f"Call report_vulnerability for each finding with file, start_line, end_line, description. "
        f"Call mark_file_scanned after analyzing each file."
    )

    print(f"\n🔍 Scanner output:\n{result.text[:500]}...")
    print(f"\n🧠 Vulnerabilities in memory: {len(scan_memory.vulnerabilities)}")
    print(f"📂 Files covered: {scan_memory.files_covered}")

    assert len(scan_memory.vulnerabilities) > 0, "Should find at least one secret"

    for v in scan_memory.vulnerabilities[:5]:
        print(f"   📌 {v['file']}:{v['start_line']}-{v['end_line']} — {v['description'][:60]}")

    print("\n✅ Challenge 04 complete — secrets scanner is operational!")

if __name__ == "__main__":
    asyncio.run(test_challenge_04())
