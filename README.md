# Microsoft Agent Framework - Demo Repository

This repository demonstrates the **Microsoft Agent Framework** - a Python SDK for building AI agents with Azure OpenAI. The demos showcase key framework capabilities including multi-agent orchestration, workflows, tool calling, and human-in-the-loop approval patterns.

## What is Agent Framework?

Agent Framework is Microsoft's SDK for building production-ready AI agents that can:
- 🤖 **Orchestrate multiple agents** working together
- 🔄 **Execute workflows** with routing, fan-out/fan-in, and state management
- 🛠️ **Call tools** (functions) with structured inputs/outputs
- ✋ **Require human approval** for dangerous operations
- 📊 **Provide observability** through middleware hooks
- 🧠 **Maintain context** via memory/context providers

## Demos

### 1. Basic Notebook Demo (`agent_framework.ipynb`)

A Jupyter notebook showing fundamental agent interactions:
- Creating a chat client with Azure OpenAI
- Building simple agents
- Basic conversation flows

**Best for**: Getting started, understanding core concepts

### 2. OpsCopilot DevUI Demo (`opscopilot-devui-demo/`)

A complete incident triage system demonstrating **all major framework features**:

| Feature | Implementation |
|---------|----------------|
| **Multi-Agent** | Classifier → Writer → QA agents |
| **Workflow** | 3-step orchestration with executor routing |
| **Tools** | Enrichment tools + dangerous action tools |
| **Human-in-the-Loop** | Approval required for `restart_service`, `open_sev1_bridge` |
| **Middleware** | Logging hooks for agent and function calls |
| **Memory** | Context providers for user preferences |
| **DevUI** | Visual interface at http://localhost:8282 |

**Best for**: Understanding production patterns, exploring the DevUI

## Quick Start

### Prerequisites

```bash
# 1. Azure CLI login (required for authentication)
az login

# 2. Set environment variables
export AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
export AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini
```

### Run the Notebook Demo

```bash
pip install agent-framework --pre python-dotenv
jupyter notebook agent_framework.ipynb
```

### Run the OpsCopilot DevUI Demo

```bash
cd opscopilot-devui-demo
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python run_devui.py
# Open http://localhost:8282
```

## Project Structure

```
agent-framework/
├── agent_framework.ipynb              # Basic notebook demo
├── opscopilot-devui-demo/             # Full-featured DevUI demo
│   ├── opscopilot/
│   │   ├── models.py                  # Pydantic data models
│   │   ├── mock_data.py               # Sample incidents
│   │   ├── tools.py                   # AI functions with approval
│   │   ├── middleware.py              # Logging middleware
│   │   ├── memory.py                  # Context providers
│   │   ├── agents.py                  # Agent definitions
│   │   └── workflow.py                # Workflow orchestration
│   ├── run_devui.py                   # Server launcher
│   └── README.md                      # Detailed demo docs
└── README.md                          # This file
```

## Learn More

- [Agent Framework Documentation](https://github.com/microsoft/agent-framework)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)

## License

MIT
