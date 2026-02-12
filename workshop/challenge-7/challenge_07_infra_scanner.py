"""
Challenge 07 — Dependency & Infrastructure Scanner
===================================================
Vulnerabilities aren't only in application code. They hide in:
  - Third-party dependencies with known CVEs
  - Dockerfiles with insecure configurations
  - CI/CD pipelines missing security checks
  - Terraform/IaC files with overly permissive policies

Your task: Build a scanner agent that covers dependencies and
infrastructure configuration files, reporting all findings to memory.

Export:
    infra_scanner  — an agent that scans deps, Docker, CI/CD, and IaC
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

from shared_models import GITHUB_REPO, VulnerabilityList, create_mcp_client, create_chat_client

load_dotenv()

chat_client = create_chat_client()
chat_client_mcp = create_mcp_client()

# Import tools from previous challenges
from challenge_01_repo_access import github_mcp_tool
from challenge_02_file_tools import read_repo_file, list_repo_files
from challenge_03_memory import scan_memory, report_vulnerability, mark_file_scanned


# ═════════════════════════════════════════════════════════════════════
# TODO: Create an infra_scanner agent
#
# This agent specializes in finding:
#   - Dependency vulnerabilities (requirements.txt with outdated/CVE packages)
#   - Docker misconfigurations (running as root, no health checks, etc.)
#   - CI/CD security issues (secrets in workflows, missing scanning)
#   - Terraform/IaC misconfigurations (public S3, overly permissive IAM)
#   - docker-compose exposures
#   - Application misconfigurations (debug mode, CORS, verbose errors)
#
# The agent MUST:
#   - Use tools: read_repo_file, list_repo_files,
#     report_vulnerability, mark_file_scanned
#   - Use context_provider=scan_memory
#   - Use response_format=VulnerabilityList for structured output
#   - Call report_vulnerability for EACH finding
#   - Call mark_file_scanned after analyzing each file
#
# Think about:
#   - Which files should this agent focus on?
#   - Should it try to identify specific CVE IDs for dependency issues?
#
# Assign to: infra_scanner
# ═════════════════════════════════════════════════════════════════════

infra_scanner = None  # Replace with your implementation


# ─── Test (DO NOT MODIFY) ────────────────────────────────────────────
async def test_challenge_07():
    assert infra_scanner is not None, "infra_scanner is not set"

    scan_memory.reset()

    print("🏗️ Running infrastructure scanner...")
    result = await infra_scanner.run(
        f"Scan the repository {GITHUB_REPO} for dependency vulnerabilities, "
        f"Docker misconfigurations, CI/CD security issues, and "
        f"Terraform/infrastructure misconfigurations. "
        f"Check requirements.txt, Dockerfile, docker-compose.yml, "
        f"CI/CD workflow files, and Terraform files. "
        f"Call report_vulnerability for each finding. "
        f"Call mark_file_scanned after analyzing each file."
    )

    findings = VulnerabilityList.model_validate_json(result.text)

    print(f"\n🏗️ Structured output: {len(findings.vulnerabilities)} infrastructure issues")
    for v in findings.vulnerabilities[:5]:
        print(f"   {v.file}:{v.start_line}-{v.end_line} — {v.description[:60]}")

    print(f"\n🧠 Memory: {len(scan_memory.vulnerabilities)} vulnerabilities")

    assert len(scan_memory.vulnerabilities) > 0, "Should find at least one infra issue"
    print("\n✅ Challenge 07 complete — infrastructure scanner operational!")

if __name__ == "__main__":
    asyncio.run(test_challenge_07())
