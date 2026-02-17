# 📧 Microsoft Agent Framework — Learning Examples

A comprehensive collection of learning resources for building AI-powered systems using the **Microsoft Agent Framework**. This repository includes both an interactive Jupyter notebook tutorial and standalone Python examples demonstrating advanced orchestration patterns.

## 🎯 What's Included

This repository contains two main learning resources:

### 1. **InboxOps Support Copilot** (Jupyter Notebook)
A comprehensive 16-section tutorial covering the full framework:

- ✅ **Single agents** with streaming and thread-based memory
- ✅ **Function tools** for API integration (`@tool` decorator)
- ✅ **Multimodal input** accepting images and attachments
- ✅ **Structured output** returning Pydantic models
- ✅ **MCP integration** connecting to external systems
- ✅ **Human-in-the-loop** approval gates for sensitive actions
- ✅ **Middleware** for logging and observability
- ✅ **Error handling** with retry and circuit breakers
- ✅ **Memory** with persistent context providers
- ✅ **Multi-agent workflows** (Sequential, Concurrent, Group Chat, Magentic, Handoff)

### 2. **Startup Idea Analyzer** (Standalone Python Script)
A Magentic orchestration demo featuring collaborative AI agents:

- 🔍 **Market Researcher** - Pessimistic analyst focused on risks
- 💰 **Financial Analyst** - Optimistic view on revenue potential
- ⚙️ **Tech Advisor** - Skeptical technical feasibility assessor
- 🎯 **Magentic Manager** - Coordinates the team and balances perspectives
- 📄 **Live Logging** - Real-time Markdown discussion logs
- ⚡ **Streaming Output** - See agent discussions as they happen
- 🔄 **Human-in-the-Loop** - Optional plan review and approval

## 🚀 Quick Start

### Prerequisites

1. ✅ **Azure subscription** with access to Azure OpenAI
2. ✅ **Azure OpenAI resource** with a deployed model (e.g., `gpt-4o-mini`)
3. ✅ **Azure CLI** installed and authenticated (`az login`)
4. ✅ **Python 3.10+**

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/moti-malka/agent-framework.git
cd agent-framework

# 2. Create virtual environment
python3.10 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or .venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
# Create a .env file with your Azure OpenAI configuration:
AZURE_OPENAI_ENDPOINT=https://your-apim-gateway.azure-api.net  # APIM gateway URL
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini
AZURE_OPENAI_API_KEY=your-apim-subscription-key  # APIM subscription key
API_VERSION=2025-01-01-preview  # Optional, defaults to this value

# 5. Login to Azure (for CLI-based authentication)
az login
```

### Running the Examples

**Option 1: Jupyter Notebook Tutorial**
```bash
# Open the notebook
jupyter notebook agent_framework.ipynb
# Or open in VS Code with Jupyter extension
```

**Option 2: Standalone Magentic Demo**
```bash
# Run the startup analyzer
python magentic_example.py

# Follow the interactive prompts to:
# - Choose streaming or human-in-the-loop mode
# - Select a pre-defined startup idea or enter your own
# - Watch agents collaborate in real-time
# - Review the generated discussion log in discussions/ folder
```

## 🏗️ Framework Features Demonstrated

### Jupyter Notebook (`agent_framework.ipynb`)

| Feature | Section | Description |
|---------|---------|-------------|
| **ChatAgent** | 1-3 | Core agent with instructions, streaming, threads |
| **Function Tools** | 4 | `@tool` decorator for custom capabilities |
| **Multimodal Input** | 5 | Image and file attachment support |
| **Structured Output** | 6 | Pydantic model responses |
| **MCP Integration** | 7 | Model Context Protocol server connections |
| **Approval Mode** | 8 | `approval_mode="always_require"` for HITL |
| **Middleware** | 9 | Agent and function invocation hooks |
| **Error Handling** | 10 | Retry logic and circuit breaker patterns |
| **ContextProvider** | 11 | Memory with `invoking`/`invoked` lifecycle |
| **Sequential Workflow** | 12 | Fixed pipeline execution patterns |
| **Concurrent Workflow** | 13 | Fan-out/fan-in parallel processing |
| **Group Chat** | 14 | Round-robin and orchestrated discussions |
| **MagenticBuilder** | 15 | Dynamic manager-orchestrated teams |
| **Handoff Pattern** | 16 | Peer-to-peer agent routing |

### Python Script (`magentic_example.py`)

| Feature | Description |
|---------|-------------|
| **MagenticBuilder** | Dynamic team coordination with manager agent |
| **Specialized Agents** | Role-based agents with distinct personalities |
| **Streaming Events** | Real-time agent updates via `AgentRunUpdateEvent` |
| **Progress Tracking** | `MagenticProgressLedger` for workflow state |
| **Plan Review** | Human-in-the-loop approval with `MagenticPlanReviewRequest` |
| **Discussion Logging** | Custom middleware for Markdown conversation logs |
| **Agent Middleware** | Custom logging hooks for observability |
| **Azure Authentication** | Both API key and Azure CLI auth support |

## 📁 Project Structure

```
agent-framework/
├── agent_framework.ipynb      # Interactive tutorial notebook (12 sections)
├── magentic_example.py        # Standalone Magentic orchestration demo
├── requirements.txt           # Python dependencies
├── .env                       # Azure OpenAI configuration (create this)
├── .venv/                     # Python virtual environment
├── images/                    # Architecture and workflow diagrams
│   ├── agent-components.png
│   ├── concurrent-workflow.png
│   ├── group-chat.png
│   ├── magentic-workflow.png
│   ├── sequential-workflow.png
│   ├── threads-and-memory.png
│   └── workflow-example.png
├── discussions/               # Created by magentic_example.py at runtime (Markdown logs)
└── README.md                  # This file
```

## 📝 Environment Variables

Create a `.env` file in the project root with the following variables:

```bash
# Required: Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini

# Optional: API Key (if not using Azure CLI authentication)
AZURE_OPENAI_API_KEY=your-api-key

# Optional: API Version (defaults to 2025-01-01-preview)
API_VERSION=2025-01-01-preview
```

**Authentication Options:**
1. **Azure CLI** (recommended): Run `az login` before starting
2. **API Key**: Set `AZURE_OPENAI_API_KEY` in `.env`

## 📚 Jupyter Notebook Contents

The `agent_framework.ipynb` tutorial is organized into 16 progressive sections:

| # | Section | What You'll Learn |
|---|---------|------------------|
| **0** | Environment Setup | Azure OpenAI setup, models, sample data |
| **1** | Single Agent | Create and run your first agent |
| **2** | Streaming Responses | Real-time token streaming |
| **3** | Threads | Thread-based conversation history |
| **4** | Tools | Add custom function capabilities with `@tool` |
| **5** | Multimodal Input | Accept images and attachments |
| **6** | Structured Output | Return Pydantic models instead of text |
| **7** | MCP Integration | Connect to external systems via MCP servers |
| **8** | Human-in-the-Loop | Approval gates before risky actions |
| **9** | Middleware & Observability | Logging, timing, and hooks |
| **10** | Error Handling & Retry | Exponential backoff and circuit breakers |
| **11** | Memory | Persistent context with `ContextProvider` |
| **12** | Sequential Workflow | Fixed pipeline (classify → draft → review) |
| **13** | Concurrent Workflow | Fan-out / fan-in with parallel agents |
| **14** | Group Chat | Round-robin and orchestrator-led discussions |
| **15** | Magentic Orchestration | Dynamic planning with HITL approval |
| **16** | Handoff Orchestration | Peer-to-peer agent routing |

## 📖 Learn More

- [Agent Framework Documentation](https://github.com/microsoft/agent-framework)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)

## License

MIT
