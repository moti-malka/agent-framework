# OpsCopilot DevUI Demo

**A complete incident triage system demonstrating Microsoft Agent Framework capabilities.**

## Purpose

This demo showcases how to build a **production-style AI operations assistant** using the Agent Framework. It simulates an incident management workflow where:

1. An incident comes in (e.g., "AKS Node NotReady")
2. The system **enriches** it with service health, runbooks, and known issues
3. An AI agent **classifies** severity and recommends actions
4. Another agent **writes** a response plan with customer messaging
5. **Dangerous actions** (like restarting services) require human approval

**This is a demo with mock data** - no real Azure resources are affected.

## What This Demonstrates

| Framework Feature | How It's Used |
|-------------------|---------------|
| **Agents** | 3 specialized agents: Classifier, Writer, QA |
| **Workflows** | Multi-step orchestration: triage → write → format |
| **Tools (@ai_function)** | `fetch_service_health`, `lookup_runbook`, `restart_service` |
| **Human-in-the-Loop** | `approval_mode="always_require"` on dangerous tools |
| **Middleware** | Async logging for all agent and function calls |
| **Context Providers** | Memory that injects user preferences into prompts |
| **DevUI** | Visual interface to interact with agents and workflows |

## Quick Start

```bash
# Setup
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
az login

# Configure (create .env or export)
export AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
export AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini

# Run
python run_devui.py
```

Open **http://localhost:8282**

## Testing the Workflow

In the DevUI, select the **OpsCopilot Incident Triage** workflow and send:

```json
{
  "id": "INC-001",
  "title": "AKS Node NotReady",
  "description": "Node aks-nodepool1-vmss000003 in cluster prod-west is NotReady for 15 minutes",
  "service": "AKS-Prod-West",
  "customer": "Contoso",
  "severity_hint": "High"
}
```

### Sample Incidents

| ID | Title | Severity Hint |
|----|-------|---------------|
| INC-001 | AKS Node NotReady | High |
| INC-002 | VM CPU at 95% | Medium |
| INC-003 | API Gateway Latency Spike | High |
| INC-004 | User Can't Sign In (MFA) | Low |
| INC-005 | Storage Account Throttling | Medium |
| INC-006 | SSL Certificate Expiring | Low |
| INC-007 | Redis Cache Memory Pressure | Medium |
| INC-008 | Kubernetes Pod CrashLoopBackOff | High |

## Architecture

```
                         ┌─────────────────────────┐
                         │   DevUI (port 8282)     │
                         └───────────┬─────────────┘
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         │                    WORKFLOW                           │
         │  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐ │
         │  │   Triage    │ → │   Writer    │ → │   Format    │ │
         │  │  Executor   │   │  Executor   │   │   Output    │ │
         │  └──────┬──────┘   └──────┬──────┘   └─────────────┘ │
         └─────────┼─────────────────┼───────────────────────────┘
                   │                 │
         ┌─────────┴─────────┐       │
         │ Enrichment Tools  │       │
         │ • service_health  │       │
         │ • lookup_runbook  │       │
         │ • known_issues    │       │
         └───────────────────┘       │
                                     │
                   ┌─────────────────┴─────────────────┐
                   │         Writer Agent              │
                   │  ┌─────────────────────────────┐  │
                   │  │ Tools with Approval:        │  │
                   │  │ • restart_service ⚠️        │  │
                   │  │ • open_sev1_bridge ⚠️       │  │
                   │  └─────────────────────────────┘  │
                   └───────────────────────────────────┘
                                     │
                                     ▼
                   ┌───────────────────────────────────┐
                   │     Human Approval Required       │
                   │  (approval_mode="always_require") │
                   └───────────────────────────────────┘
```

## File Structure

```
opscopilot/
├── models.py      # Incident, TriageResult, FinalPlan (Pydantic)
├── mock_data.py   # 8 sample incidents
├── tools.py       # Enrichment functions + dangerous actions
├── middleware.py  # Async logging middleware
├── memory.py      # OpsMemory context provider
├── agents.py      # ClassifierAgent, WriterAgent, QAAgent
└── workflow.py    # Workflow definition with executors
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 8282 in use | `lsof -ti:8282 \| xargs kill -9` |
| Azure auth failed | Run `az login` |
| Module not found | Activate venv: `source .venv/bin/activate` |
| Invalid message name | Agent names must not contain spaces |
