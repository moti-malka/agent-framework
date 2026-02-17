"""
Challenge 10 — Final Orchestrated Security Workflow
====================================================
You've built all the components. Now wire them together into a
complete, orchestrated security scanning workflow.

Import your agents from previous challenges and build a workflow
that runs them together to produce a comprehensive security scan.

📋 OUTPUT FORMAT: The test function will automatically save your scan
results to 'workshop/challenge_10_output.json' in the expected format.
See 'workshop/expected_workflow_output.json' for the structure.
Run 'python workshop/score_workflow.py workshop/challenge_10_output.json'
to check your score against the catalog.

You choose the orchestration pattern:
  - MagenticBuilder    — manager dynamically delegates to scanners
  - GroupChatBuilder   — agents collaborate and cross-check
  - HandoffBuilder     — agents pass control to each other

Export:
    TASK_PROMPT          — the main scanning task description
    FINAL_ANSWER_PROMPT  — instructions for how the manager wraps up
    security_workflow    — the complete orchestrated workflow
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import _paths  # noqa: F401

import asyncio
import os
import logging
import time
import nest_asyncio
nest_asyncio.apply()

from typing import cast, Any
from dotenv import load_dotenv
from agent_framework import (
    Agent, Message, WorkflowEvent, AgentResponseUpdate,
)
from agent_framework.orchestrations import (
    # ── Workflow Builders (pick one) ──────────────────────────────────
    MagenticBuilder,    # Option A: manager dynamically delegates to scanners
    GroupChatBuilder,   # Option B: agents collaborate in shared conversation
    HandoffBuilder,     # Option C: agents hand off control in a chain
    ConcurrentBuilder,  # Option D: all agents run in parallel simultaneously
)

from shared_models import GITHUB_REPO, create_mcp_client, create_chat_client

load_dotenv()

chat_client = create_chat_client()
chat_client_mcp = create_mcp_client()

# ─── Import your agents from previous challenges ─────────────────────
from challenge_01_repo_access import github_mcp_tool, repo_explorer
from challenge_02_file_tools import read_repo_file, list_repo_files
from challenge_03_memory import scan_memory, report_vulnerability, mark_file_scanned
from challenge_04_middleware import agent_logging_middleware, tool_logging_middleware
from challenge_05_secrets_scanner import secrets_scanner
from challenge_07_code_scanner import code_vuln_scanner
from challenge_08_infra_scanner import infra_scanner
from challenge_09_auth_crypto_scanner import auth_crypto_scanner


# ═════════════════════════════════════════════════════════════════════
# TODO 1: Define TASK_PROMPT
#
# This is the main task description passed to your workflow via
# security_workflow.run(TASK_PROMPT, stream=True).
#
# It should instruct the scanning team to:
#   - Comprehensively scan the repository for ALL vulnerability types
#   - Cover every file in the repository
#   - Use report_vulnerability for each finding (so memory is populated)
#   - Use mark_file_scanned for each file analyzed
#
# Think about:
#   - What repo should be scanned?
#   - What vulnerability categories exist?
#   - How to emphasize calling report_vulnerability
#
# Assign to: TASK_PROMPT (string)
# ═════════════════════════════════════════════════════════════════════

TASK_PROMPT = None  # Replace with your implementation


# ═════════════════════════════════════════════════════════════════════
# TODO 2: Define FINAL_ANSWER_PROMPT
#
# This tells the manager how to produce its final message after all
# scanners have finished. Used with MagenticBuilder's constructor:
# MagenticBuilder(..., final_answer_prompt=FINAL_ANSWER_PROMPT).
#
# The manager's final message is for display only — scoring comes
# from memory. But a good summary helps you understand what was found.
#
# Think about:
#   - Telling the manager to summarize what each scanner found
#   - Mentioning how many total vulnerabilities are in memory
#   - Confirming all files were covered
#
# If you're using GroupChatBuilder or HandoffBuilder, this may not
# be needed, but define it anyway for compatibility.
#
# Assign to: FINAL_ANSWER_PROMPT (string)
# ═════════════════════════════════════════════════════════════════════

FINAL_ANSWER_PROMPT = None  # Replace with your implementation


# ═════════════════════════════════════════════════════════════════════
# TODO 3: Build your orchestrated security_workflow
#
# You have these components from previous challenges:
#   - secrets_scanner       (from challenge 05)
#   - code_vuln_scanner     (from challenge 07)
#   - infra_scanner         (from challenge 08)
#   - auth_crypto_scanner   (from challenge 09)
#   - scan_memory           (from challenge 03)
#   - agent/tool middleware (from challenge 04)
#
# Choose a Builder pattern:
#
#   ── Option A: MagenticBuilder (dynamic delegation) ─────────────────
#   Uses: WorkflowEvent (event.type == "executor_invoked" / "output" / ...)
#
#     manager = Agent(client=chat_client, name="ScanManager", ...)
#     workflow = MagenticBuilder(
#         participants=[scanner1, scanner2, ...],
#         manager_agent=manager,
#         max_round_count=N,
#         max_stall_count=5,
#         final_answer_prompt=FINAL_ANSWER_PROMPT,
#     ).build()
#
#   Event loop:
#     async for event in workflow.run(TASK_PROMPT, stream=True):
#         if event.type == "executor_invoked":
#             agent_id = event.executor_id  # which agent is speaking
#             token = event.data            # streaming token (str)
#         elif event.type == "output":
#             print("Final output:", event.data)
#
#   ── Option B: GroupChatBuilder (collaborative cross-checking) ──────
#   Uses: WorkflowEvent (event.type == "output" / ...)
#
#     workflow = GroupChatBuilder(
#         participants=[scanner1, scanner2, ...],
#         selection_func=my_selector,         # or orchestrator_agent=agent
#         orchestrator_name="MyOrchestrator",
#         termination_condition=my_condition,
#     ).build()
#
#   ── Option C: HandoffBuilder (sequential escalation chain) ─────────
#   Uses: WorkflowEvent (event.type == "output" / "request_info" / ...)
#
#     workflow = HandoffBuilder(
#         start_agent=scanner1,
#         handoffs=[
#             (scanner1, scanner2, "Hand off to code vuln scanner"),
#             (scanner2, scanner3, "Hand off to infra scanner"),
#         ],
#     ).build()
#
#   ── Option D: ConcurrentBuilder (parallel fan-out) ─────────────────
#   Uses: WorkflowEvent (event.type == "executor_response" / ...)
#
#     workflow = ConcurrentBuilder(
#         agents=[
#             (scanner1, "Scan for secrets..."),
#             (scanner2, "Scan for code vulns..."),
#         ],
#     ).build()
#
# If using MagenticBuilder, you'll need a manager agent (Agent)
# to coordinate the scanners. Think about:
#   - What instructions should the manager have?
#   - How many rounds should the conversation go?
#   - The manager does NOT need response_format (it breaks routing)
#
# Assign to: security_workflow
# ═════════════════════════════════════════════════════════════════════

security_workflow = None  # Replace with your implementation


# ─── Test (DO NOT MODIFY) ────────────────────────────────────────────
async def test_challenge_10():
    assert security_workflow is not None, "security_workflow is not set"
    assert TASK_PROMPT is not None, "TASK_PROMPT is not set"

    # ── Suppress SSL/aiohttp noise ──
    for name in ["aiohttp", "asyncio", "aiohttp.client"]:
        logging.getLogger(name).setLevel(logging.CRITICAL)

    loop = asyncio.get_event_loop()
    _orig = loop.get_exception_handler()

    def _quiet_handler(loop, context):
        exc = context.get("exception")
        if exc and ("SSL shutdown" in str(exc) or "ClientConnection" in str(exc)):
            return
        if _orig:
            _orig(loop, context)
        else:
            loop.default_exception_handler(context)

    loop.set_exception_handler(_quiet_handler)

    # ── Reset memory before the workflow ──
    scan_memory.reset()

    print("🛡️  FULL SECURITY SCAN")
    print("=" * 60)
    print(f"Target: {GITHUB_REPO}")
    print("=" * 60)

    start_time = time.time()
    agent_calls: dict[str, int] = {}

    async for event in security_workflow.run(TASK_PROMPT, stream=True):
        if event.type == "executor_invoked":
            eid = event.executor_id or str(event.data)
            if eid not in agent_calls:
                emoji = {
                    "SecretsScanner": "🔑", "CodeVulnScanner": "🐛",
                    "InfraScanner": "🏗️", "AuthCryptoScanner": "🔐",
                }.get(eid, "🤖")
                print(f"   {emoji} [{eid}] activated")
            agent_calls[eid] = agent_calls.get(eid, 0) + 1

    elapsed = time.time() - start_time

    print(f"\n⏱️  Scan completed in {elapsed:.1f}s")
    print(f"📊 Agents activated: {list(agent_calls.keys())}")

    # ── Results from memory ──
    print(f"\n🧠 Vulnerabilities in memory: {len(scan_memory.vulnerabilities)}")
    print(f"📂 Files covered: {len(scan_memory.files_covered)}")

    for v in scan_memory.vulnerabilities[:10]:
        print(f"   📌 {v['file']}:{v['start_line']}-{v['end_line']} — {v['description'][:60]}")
    if len(scan_memory.vulnerabilities) > 10:
        print(f"   ... and {len(scan_memory.vulnerabilities) - 10} more")

    assert len(scan_memory.vulnerabilities) > 0, \
        "Memory should have vulnerabilities after the scan"

    # ── Export results to JSON ──
    import json
    from datetime import datetime
    
    output_data = {
        "workshop_id": "agent-framework-security-scan",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "repository": GITHUB_REPO,
        "scan_summary": {
            "total_vulnerabilities": len(scan_memory.vulnerabilities),
            "files_scanned": len(scan_memory.files_covered),
            "scanners_used": list(agent_calls.keys()),
            "scan_duration_seconds": round(elapsed, 1),
        },
        "vulnerabilities": list(scan_memory.vulnerabilities),
        "files_covered": sorted(scan_memory.files_covered),
        "scanner_breakdown": {
            scanner: {
                "findings": sum(1 for v in scan_memory.vulnerabilities 
                              if v.get('scanner', 'unknown') == scanner),
                "files": sorted({v['file'] for v in scan_memory.vulnerabilities 
                               if v.get('scanner', 'unknown') == scanner})
            } for scanner in agent_calls.keys()
        }
    }
    
    output_file = "workshop/challenge_10_output.json"
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"\n💾 Results saved to: {output_file}")
    print(f"   Run: python workshop/score_workflow.py {output_file}")

    print(f"\n{'=' * 60}")
    print("✅ Challenge 10 complete — run the test runner to see your score!")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(test_challenge_10())
