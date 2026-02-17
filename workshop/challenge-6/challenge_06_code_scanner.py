"""
Challenge 06 — Code Vulnerability Scanner
==========================================
Secrets are just one category. The application also has code-level
vulnerabilities: SQL injection, command injection, XSS, SSRF,
insecure deserialization, path traversal, and more.

Your task: Build a dedicated code vulnerability scanner agent that
specializes in finding injection flaws and unsafe code patterns.
It outputs structured results AND reports findings to shared memory.

Export:
    code_vuln_scanner  — an agent that detects code vulnerabilities
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

from shared_models import GITHUB_REPO, VulnerabilityList, create_mcp_client, create_chat_client

load_dotenv()

chat_client = create_chat_client()
chat_client_mcp = create_mcp_client()

# Import tools from previous challenges
from challenge_01_repo_access import github_mcp_tool
from challenge_02_file_tools import read_repo_file, list_repo_files
from challenge_03_memory import scan_memory, report_vulnerability, mark_file_scanned


# ═════════════════════════════════════════════════════════════════════
# TODO: Create a code_vuln_scanner agent
#
# This agent specializes in finding code-level vulnerabilities:
#   - SQL injection
#   - Command injection (os.system, subprocess with shell=True)
#   - Cross-site scripting (XSS)
#   - Server-side request forgery (SSRF)
#   - Insecure deserialization (pickle, yaml.load)
#   - Path traversal
#   - XML external entity injection (XXE)
#   - Use of eval/exec with user input
#   - Missing authentication/authorization checks
#   - Sensitive data in logs
#
# The agent MUST:
#   - Use tools: read_repo_file, list_repo_files,
#     report_vulnerability, mark_file_scanned
#   - Use context_providers=[scan_memory]
#   - Use response_format=VulnerabilityList for structured output
#   - Call report_vulnerability for EACH finding
#   - Call mark_file_scanned after analyzing each file
#
# Assign to: code_vuln_scanner
# ═════════════════════════════════════════════════════════════════════

code_vuln_scanner = None  # Replace with your implementation


# ─── Test (DO NOT MODIFY) ────────────────────────────────────────────
async def test_challenge_06():
    assert code_vuln_scanner is not None, "code_vuln_scanner is not set"

    scan_memory.reset()

    print("🐛 Running code vulnerability scanner...")
    result = await code_vuln_scanner.run(
        f"Scan the repository {GITHUB_REPO} for code-level security vulnerabilities. "
        f"Focus on injection flaws, unsafe deserialization, path traversal, "
        f"and dangerous function usage. Check all Python source files. "
        f"Call report_vulnerability for each finding. "
        f"Call mark_file_scanned after analyzing each file."
    )

    findings = VulnerabilityList.model_validate_json(result.text)

    print(f"\n🐛 Structured output: {len(findings.vulnerabilities)} code vulnerabilities")
    for v in findings.vulnerabilities[:5]:
        print(f"   {v.file}:{v.start_line}-{v.end_line} — {v.description[:60]}")

    print(f"\n🧠 Memory: {len(scan_memory.vulnerabilities)} vulnerabilities")

    assert len(scan_memory.vulnerabilities) > 0, "Should find at least one code vulnerability"
    print("\n✅ Challenge 06 complete — code vulnerability scanner operational!")

if __name__ == "__main__":
    asyncio.run(test_challenge_06())
