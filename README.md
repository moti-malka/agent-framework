# Agent Framework Demos

דמואים של Microsoft Agent Framework עם Azure OpenAI.

## 📁 Project Structure

```
agent-framework/
├── agent_framework.ipynb          # Notebook demo - בסיסי
├── opscopilot-devui-demo/         # OpsCopilot DevUI demo - מתקדם
│   ├── opscopilot/
│   │   ├── models.py              # Pydantic models
│   │   ├── mock_data.py           # Mock incidents
│   │   ├── tools.py               # AI functions + approval
│   │   ├── middleware.py          # Logging middleware
│   │   ├── memory.py              # Context providers
│   │   ├── agents.py              # Agent definitions
│   │   └── workflow.py            # Workflow orchestration
│   ├── run_devui.py               # DevUI launcher
│   └── README.md                  # Demo documentation
└── README.md                      # This file
```

## 🚀 Quick Start

### Prerequisites

```bash
# Azure CLI login
az login

# Set environment variables (or create .env file)
export AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
export AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini
```

### Option 1: Notebook Demo (Basic)

```bash
pip install agent-framework --pre python-dotenv
```

Open `agent_framework.ipynb` and run the cells.

### Option 2: OpsCopilot DevUI Demo (Advanced)

```bash
cd opscopilot-devui-demo
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python run_devui.py
```

Open http://localhost:8282

## 📖 Demos

| Demo | Description | Features |
|------|-------------|----------|
| `agent_framework.ipynb` | Basic notebook demo | Simple agent interactions |
| `opscopilot-devui-demo` | Full incident triage workflow | Agents, Workflow, Tools, Human-in-the-loop, Middleware, Memory |

## License

MIT
