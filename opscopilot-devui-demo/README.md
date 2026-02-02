# OpsCopilot DevUI Demo

🎯 **דמו של מערכת Incident Triage עם Microsoft Agent Framework DevUI**

## 🌟 Features

| Feature | Description |
|---------|-------------|
| **Agents** | Classifier, Writer, QA agents |
| **Workflow** | Multi-step orchestration with routing |
| **Tools** | Mock enrichment tools + dangerous actions |
| **Human-in-the-loop** | Approval required for restart/Sev1 bridge |
| **Middleware** | Logging for agent & function calls |
| **Memory** | Context providers (language preference) |

## 📁 Structure

```
opscopilot-devui-demo/
├── opscopilot/
│   ├── __init__.py
│   ├── models.py          # Pydantic models: Incident, TriageResult, FinalPlan
│   ├── mock_data.py       # 8 sample incidents (AKS, VM, APIM, etc.)
│   ├── tools.py           # fetch_service_health, lookup_runbook, restart_service
│   ├── middleware.py      # Async logging middleware
│   ├── memory.py          # OpsMemory ContextProvider
│   ├── agents.py          # ClassifierAgent, WriterAgent, QAAgent
│   └── workflow.py        # triage_incident → writer → format_output
├── run_devui.py           # DevUI server launcher
├── requirements.txt
└── README.md
```

## 🚀 Quick Start

### 1. Setup

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Azure CLI login
az login
```

### 2. Environment Variables

Create `.env` file or export:

```bash
export AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
export AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini
```

### 3. Run

```bash
python run_devui.py
```

Open http://localhost:8282

## 🎮 Usage

### Test Workflow

Send a JSON incident to the workflow:

```json
{
  "id": "INC-001",
  "title": "AKS Node NotReady",
  "description": "Node aks-nodepool1-12345678-vmss000003 in cluster prod-west is NotReady for 15 minutes",
  "service": "AKS-Prod-West",
  "customer": "Contoso",
  "severity_hint": "High"
}
```

### Available Incidents

| ID | Title | Service |
|----|-------|---------|
| INC-001 | AKS Node NotReady | AKS-Prod-West |
| INC-002 | VM CPU at 95% | VM-Analytics-Pool |
| INC-003 | API Gateway Latency Spike | APIM-Global |
| INC-004 | User Can't Sign In (MFA) | Identity-Prod |
| INC-005 | Storage Account Throttling | Storage-DataLake |
| INC-006 | SSL Certificate Expiring | AppGW-Frontend |
| INC-007 | Redis Cache Memory Pressure | Redis-Session-Cache |
| INC-008 | Kubernetes Pod CrashLoopBackOff | AKS-Prod-West |

### Test Individual Agents

- **ClassifierAgent**: Triage and categorize incidents
- **WriterAgent**: Create response plans with tools
- **QAAgent**: Review and approve plans

## 🔧 Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        DevUI (port 8282)                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Workflow: OpsCopilot                     │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐    │
│  │   triage     │ → │    writer    │ → │   format     │    │
│  │  (enrich +   │   │   (agent)    │   │   output     │    │
│  │   classify)  │   │              │   │              │    │
│  └──────────────┘   └──────────────┘   └──────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
    ┌──────────┐        ┌──────────┐        ┌──────────┐
    │Classifier│        │  Writer  │        │    QA    │
    │  Agent   │        │  Agent   │        │  Agent   │
    └──────────┘        └──────────┘        └──────────┘
          │                   │
          ▼                   ▼
    ┌──────────┐        ┌──────────────────────────┐
    │TriageResult       │ Tools:                   │
    │ (structured)│     │ - fetch_service_health   │
    └──────────┘        │ - lookup_runbook         │
                        │ - search_known_issues    │
                        │ - restart_service ⚠️     │
                        │ - open_sev1_bridge ⚠️    │
                        └──────────────────────────┘
                                    │
                                    ▼
                        ┌──────────────────────────┐
                        │ Human Approval Required  │
                        │ (approval_mode="always") │
                        └──────────────────────────┘
```

## 🔐 Human-in-the-Loop

The following tools require human approval:

| Tool | Description |
|------|-------------|
| `restart_service` | Restart a production service |
| `open_sev1_bridge` | Open Sev1 bridge call |

These are decorated with `@ai_function(approval_mode="always_require")`.

## 📝 Notes

- **Mock Data**: All data is mock - no real Azure calls
- **In-Memory**: No database, all state is in-memory
- **Hebrew Support**: Context provider includes Hebrew language preference
- **Demo Only**: For learning and demonstration purposes

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 8282 in use | `lsof -ti:8282 \| xargs kill -9` |
| Azure auth failed | Run `az login` |
| Module not found | Activate venv: `source .venv/bin/activate` |
