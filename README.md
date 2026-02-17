# 📧 Microsoft Agent Framework — Learning Examples

A comprehensive collection of learning resources for building AI-powered systems using the **Microsoft Agent Framework**. This repository includes both an interactive Jupyter notebook tutorial and standalone Python examples demonstrating advanced orchestration patterns.

## 🎯 What's Included

This repository contains two main learning resources:

### 1. **Support Email Copilot** (Jupyter Notebook)
An interactive tutorial that progressively teaches framework capabilities:

- ✅ **Classifies** incoming emails (Spam / Not Spam / Uncertain)
- ✅ **Looks up** customer SLA and ticket status via function tools
- ✅ **Drafts** professional responses with customizable tone
- ✅ **Requires approval** before sending sensitive replies
- ✅ **Remembers** user preferences (language, tone, name)
- ✅ **Processes in parallel** for long emails (response + summary)
- ✅ **Uses multiple reviewers** for quality control (security, tone, accuracy)
- ✅ **Logs** every operation for observability

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
| **Multimodal Input** | 4.1 | Handle images and screenshots |
| **Structured Output** | 4.2 | Pydantic models for validated JSON responses |
| **MCP Integration** | 4.3 | Connect external tools via MCP protocol |
| **Approval Mode** | 5 | `approval_mode="always_require"` for HITL |
| **Middleware** | 6 | Agent and function invocation hooks |
| **Error Handling** | 6.2 | Retry logic, circuit breakers, resilience patterns |
| **Rate Limiting** | 6.3 | Token bucket pattern for traffic control |
| **Caching** | 6.4 | Cache decorator for repeated queries |
| **ContextProvider** | 7 | Memory with `invoking`/`invoked` lifecycle |
| **WorkflowBuilder** | 8-10 | Sequential, branching, fan-out patterns |
| **AgentExecutor** | 8-10 | Wrap agents for workflow orchestration |
| **Switch-Case** | 9 | Multi-way routing with `Case`/`Default` |
| **Checkpointing** | 9.1 | Resume workflows from failure points |
| **Multi-Selection** | 10 | Dynamic fan-out to parallel paths |
| **Fan-In** | 10 | Aggregate results from parallel execution |
| **ConcurrentBuilder** | 11 | Parallel multi-agent processing |
| **MagenticBuilder** | 12 | Manager-orchestrated agent teams |
| **Evaluation** | 13 | Quality metrics and automated testing |
| **Durable Agents** | 14 | Production deployment with Azure Functions |
| **AG-UI** | 15 | Web interface integration |

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
├── .github/                   # GitHub automation
│   ├── agents/               # Custom agent configurations
│   │   └── readme-updater.agent.md
│   └── workflows/            # GitHub Actions workflows
│       ├── notebook-sync.lock.yml      # Auto-sync notebook changes
│       ├── notebook-sync.md
│       ├── readme-updater.lock.yml     # Auto-update README
│       └── readme-updater.md
├── .gitattributes            # Git attribute rules for workflows
├── .gitignore                # Python, IDE, and environment ignores
├── agent_framework.ipynb     # Interactive tutorial (15+ sections)
├── magentic_example.py       # Standalone Magentic orchestration demo
├── requirements.txt          # Python dependencies
├── .env                      # Azure OpenAI configuration (create this)
├── .venv/                    # Python virtual environment (ignored)
├── images/                   # Architecture and workflow diagrams
│   ├── agent-components.png
│   ├── concurrent-workflow.png
│   ├── customer_image.png
│   ├── group-chat.png
│   ├── maf.png
│   ├── magentic-workflow.png
│   ├── main.png
│   ├── sequential-workflow.png
│   ├── threads-and-memory.png
│   ├── what-is-agent.png
│   └── workflow-example.png
├── discussions/              # Auto-generated: Markdown logs from magentic_example.py
└── README.md                 # This file
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

The `agent_framework.ipynb` tutorial is organized into 15+ progressive sections covering basic to production-ready patterns:

| # | Section | What You'll Learn |
|---|---------|------------------|
| **0** | Environment Setup | Azure OpenAI client, models, sample data |
| **1** | V0 — Basic Agent | Create and run your first support agent |
| **2** | V0.1 — Streaming | Real-time token streaming for better UX |
| **3** | V1 — Multi-Turn Conversations | Thread-based memory across conversations |
| **4** | V1.1 — Function Tools | Connect to internal systems with `@tool` |
| **4.1** | V1.2 — Multimodal Input | Handle screenshots and images |
| **4.2** | V1.3 — Structured Output | Generate validated JSON with Pydantic |
| **4.3** | V1.4 — MCP Integration | Connect external tools via MCP protocol |
| **5** | V2 — Human-in-the-Loop | Approval workflows for sensitive actions |
| **6** | V2.1 — Middleware | Logging, observability, and monitoring |
| **6.2** | V2.2 — Error Handling | Retry logic, circuit breakers, resilience |
| **6.3** | V2.3 — Rate Limiting | Protect against traffic spikes |
| **6.4** | V2.4 — Caching | Optimize repeated queries (FAQ) |
| **7** | V3 — Persistent Memory | Context that survives beyond single threads |
| **8** | Sequential Workflows | Multi-stage pipelines (classify → draft → review) |
| **9** | Branching Workflows | Conditional routing with switch-case logic |
| **9.1** | Checkpointing | Resume failed workflows from last checkpoint |
| **10** | Fan-Out/Fan-In | Parallel processing with result aggregation |
| **11** | Group Chat | Multi-agent collaboration patterns |
| **12** | Magentic Orchestration | Dynamic planning with manager coordination |
| **13** | V4 — Evaluation & Testing | Quality metrics and automated testing |
| **14** | Durable Agents | Production scalability with Azure Functions |
| **15** | AG-UI Integration | Web interface for agent interactions |

## 📖 Learn More

- [Agent Framework Documentation](https://github.com/microsoft/agent-framework)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)

## License

MIT
