"""
Challenge 08 — Authentication & Cryptography Scanner
=====================================================
Authentication weaknesses and cryptographic flaws are critical:
  - Weak password hashing (MD5, SHA1 without salt)
  - JWT algorithm confusion ('none' algorithm allowed)
  - Deprecated crypto (DES, ECB mode, hardcoded IVs)
  - Timing-attack vulnerable comparisons
  - Predictable tokens and session management flaws

Your task: Build a dedicated auth/crypto scanner agent that
specializes in authentication and cryptography vulnerabilities.
It reports all findings to the shared scan memory.

Export:
    auth_crypto_scanner  — an agent that detects auth & crypto issues
"""

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
# TODO: Create an auth_crypto_scanner agent
#
# This agent specializes in authentication & cryptography issues:
#
#   WEAK PASSWORD HANDLING:
#   - Weak hashing (MD5, SHA1 without salt)
#   - Timing-attack vulnerable string comparison (== instead of
#     hmac.compare_digest)
#   - Plaintext passwords logged to files or stdout
#
#   JWT / TOKEN ISSUES:
#   - JWT algorithm confusion: 'none' algorithm allowed
#   - Excessively long token expiry (e.g. 1 year)
#   - Weak/hardcoded JWT signing secrets
#
#   WEAK / DEPRECATED CRYPTOGRAPHY:
#   - DES encryption (deprecated)
#   - Hardcoded IV reuse in AES-CBC
#   - SHA1 for hashing sensitive data
#   - ECB mode encryption
#   - Static encryption keys or IVs
#
#   AUTHENTICATION BYPASS:
#   - Predictable random seeds for security tokens
#   - No authentication on admin endpoints
#   - Missing CSRF protection
#
# The agent MUST:
#   - Use tools: read_repo_file, list_repo_files,
#     report_vulnerability, mark_file_scanned
#   - Use context_provider=scan_memory
#   - Use response_format=VulnerabilityList
#   - Focus on auth.py, utils/crypto.py, and related files
#
# NOTE: Each vulnerability is self-contained within its file.
# The agent does NOT need cross-file memory correlation to find
# these issues — each weak pattern is visible in the file itself.
#
# Assign to: auth_crypto_scanner
# ═════════════════════════════════════════════════════════════════════

auth_crypto_scanner = None  # Replace with your implementation


# ─── Test (DO NOT MODIFY) ────────────────────────────────────────────
async def test_challenge_08():
    assert auth_crypto_scanner is not None, "auth_crypto_scanner is not set"

    scan_memory.reset()

    print("🔐 Running auth & crypto scanner...")
    result = await auth_crypto_scanner.run(
        f"Scan the repository {GITHUB_REPO} for authentication weaknesses "
        f"and cryptography issues. Focus on auth.py, utils/crypto.py, "
        f"and any file handling sessions, tokens, or encryption. "
        f"Call report_vulnerability for each finding with file, start_line, end_line, description. "
        f"Call mark_file_scanned after analyzing each file."
    )

    findings = VulnerabilityList.model_validate_json(result.text)

    print(f"\n🔐 Structured output: {len(findings.vulnerabilities)} auth/crypto issues")
    for v in findings.vulnerabilities[:5]:
        print(f"   {v.file}:{v.start_line}-{v.end_line} — {v.description[:60]}")

    print(f"\n🧠 Memory: {len(scan_memory.vulnerabilities)} vulnerabilities")

    assert len(scan_memory.vulnerabilities) > 0, "Should find at least one auth/crypto issue"
    print("\n✅ Challenge 08 complete — auth/crypto scanner operational!")

if __name__ == "__main__":
    asyncio.run(test_challenge_08())
