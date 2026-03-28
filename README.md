# 📧 Microsoft Agent Framework — Learning Examples

A comprehensive collection of learning resources for building AI-powered systems using the **Microsoft Agent Framework**. This repository includes an interactive Jupyter notebook tutorial, standalone Python examples, and a hands-on security workshop.

## 🎯 What's Included

This repository contains three main learning resources:

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

### 2. **Security Workshop** (Hands-on Challenges)
A 10-challenge workshop for building AI-powered security scanning agents:

- 🔐 **Secrets Scanner** - Detects hardcoded API keys, credentials, and tokens
- 🐛 **Code Vulnerability Scanner** - Finds injection, XSS, SSRF patterns
- 🏗️ **Infrastructure Scanner** - Scans Docker, Terraform, CI/CD configs
- 🔑 **Auth & Crypto Scanner** - Identifies weak hashing, JWT flaws
- 🔄 **Workflow Orchestration** - Coordinates multiple scanners into unified reports
- 📊 **Structured Output** - Pydantic models for consistent findings
- 🧠 **Shared Memory** - Cross-agent state coordination
- 🔌 **MCP Integration** - GitHub repository access via Model Context Protocol
- 📝 **Observability** - Middleware for logging and debugging
- 🎯 **Achievement System** - Tiered scoring based on vulnerability detection

### 3. **Startup Idea Analyzer** (Standalone Python Script) — TODO
A planned Magentic orchestration demo featuring collaborative AI agents:

- 🔍 **Market Researcher** - Pessimistic analyst focused on risks
- 💰 **Financial Analyst** - Optimistic view on revenue potential
- ⚙️ **Tech Advisor** - Skeptical technical feasibility assessor
- 🎯 **Magentic Manager** - Coordinates the team and balances perspectives
- 📄 **Live Logging** - Real-time Markdown discussion logs
- ⚡ **Streaming Output** - See agent discussions as they happen
- 🔄 **Human-in-the-Loop** - Optional plan review and approval

> **Note**: `magentic_example.py` implementation is planned for a future update.

## 🚀 Quick Start

### Prerequisites

1. ✅ **Azure subscription** with access to Azure OpenAI
2. ✅ **Azure OpenAI resource** with a deployed model (e.g., `gpt-4o-mini`)
3. ✅ **Azure CLI** installed and authenticated (`az login`)
4. ✅ **Python 3.10+**
5. ✅ **Azure AI Foundry project** *(Section 7 — MCP Integration only)*
   - **Project endpoint** — found in your project's **Overview** page
   - **Model deployment name** — found in your project's **Models + endpoints** page

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

**Option 2: Security Workshop**
```bash
# Start with Challenge 0 and progress through Challenge 10
cd workshop/challenge-1
python challenge_01_repo_access.py

# See workshop/README.md for complete challenge guide
```

**Option 3: Standalone Magentic Demo** — TODO
```bash
# Planned for future release
# python magentic_example.py
```

## 🏗️ Framework Features Demonstrated

### Jupyter Notebook (`agent_framework.ipynb`)

| Feature | Section | Description |
|---------|---------|-------------|
| **ChatAgent** | 1-3 | Core agent with instructions, streaming, threads |
| **Function Tools** | 4 | `@tool` decorator for custom capabilities |
| **Approval Mode** | 5 | `approval_mode="always_require"` for HITL |
| **Middleware** | 6 | Agent and function invocation hooks |
| **ContextProvider** | 7 | Memory with `invoking`/`invoked` lifecycle |
| **WorkflowBuilder** | 8-10 | Sequential, branching, fan-out patterns |
| **AgentExecutor** | 8-10 | Wrap agents for workflow orchestration |
| **Switch-Case** | 9 | Multi-way routing with `Case`/`Default` |
| **Multi-Selection** | 10 | Dynamic fan-out to parallel paths |
| **Fan-In** | 10 | Aggregate results from parallel execution |
| **ConcurrentBuilder** | 11 | Parallel multi-agent processing |
| **MagenticBuilder** | 11 | Manager-orchestrated agent teams |

### Security Workshop (`workshop/`)

| Challenge | Feature | Description |
|-----------|---------|-------------|
| **Challenge 1** | MCP GitHub Access | Connect agents to repositories via Model Context Protocol |
| **Challenge 2** | Custom Tools | Build reusable `@tool` functions for file operations |
| **Challenge 3** | Shared Memory | ContextProvider for cross-agent vulnerability tracking |
| **Challenge 4-8** | Scanner Agents | Specialized agents for secrets, code, infra, auth/crypto |
| **Challenge 5** | Structured Output | Pydantic models with `response_format` for consistency |
| **Challenge 9** | Middleware | Logging and observability for agent execution |
| **Challenge 10** | Workflow Orchestration | Coordinate multiple scanners into unified reports |

### Standalone Script (`magentic_example.py`) — TODO

Planned features for future release:
- **MagenticBuilder** for dynamic team coordination
- **Specialized Agents** with role-based personalities
- **Streaming Events** for real-time updates
- **Human-in-the-loop** approval workflows

## 📁 Project Structure

```
agent-framework/
├── agent_framework.ipynb      # Interactive tutorial notebook (12 sections)
├── requirements.txt           # Python dependencies
├── .env                       # Azure OpenAI configuration (create this)
├── .venv/                     # Python virtual environment
├── workshop/                  # Security scanning workshop
│   ├── README.md              # Workshop guide and challenge overview
│   ├── SECURITY_GUIDE.md      # Vulnerability knowledge base
│   ├── .env.sample            # Environment variable template
│   ├── challenge-0/           # Environment setup
│   ├── challenge-1/           # MCP repository access
│   ├── challenge-2/           # File reading tools
│   ├── challenge-3/           # Scan memory
│   ├── challenge-4/           # Secrets scanner
│   ├── challenge-5/           # Structured output
│   ├── challenge-6/           # Code vulnerability scanner
│   ├── challenge-7/           # Infrastructure scanner
│   ├── challenge-8/           # Auth and crypto scanner
│   ├── challenge-9/           # Agent middleware
│   ├── challenge-10/          # Orchestrated workflow
│   ├── shared_models.py       # Pydantic models and client factories
│   ├── expected_workflow_output.json  # Target output structure
│   └── images/                # Workflow architecture diagrams
├── images/                    # Tutorial diagrams
│   ├── agent-components.png
│   ├── concurrent-workflow.png
│   ├── group-chat.png
│   ├── magentic-workflow.png
│   ├── sequential-workflow.png
│   ├── threads-and-memory.png
│   └── workflow-example.png
├── docs/                      # HTML documentation (generated)
│   ├── index.html
│   ├── supportpilot.html
│   ├── businessbrain.html
│   ├── devopsagent.html
│   ├── docmind.html
│   └── warroom.html
└── README.md                  # This file
```

## 📝 Environment Variables

### For Jupyter Notebook & Magentic Demo

Create a `.env` file in the project root:

```bash
# Required: Azure OpenAI Configuration (Sections 1–16)
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini

# Optional: API Key (if not using Azure CLI authentication)
AZURE_OPENAI_API_KEY=your-api-key

# Optional: API Version (defaults to 2025-01-01-preview)
API_VERSION=2025-01-01-preview

# Required for Section 7 only (MCP Integration)
# AZURE_AI_PROJECT_ENDPOINT: Azure AI Foundry → your project → Overview → Project endpoint
AZURE_AI_PROJECT_ENDPOINT=https://<resource>.services.ai.azure.com/api/projects/<project>
# AZURE_AI_MODEL_DEPLOYMENT_NAME: Azure AI Foundry → your project → Models + endpoints → Deployment name
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o-mini
```

**Authentication Options:**
1. **Azure CLI** (recommended): Run `az login` before starting
2. **API Key**: Set `AZURE_OPENAI_API_KEY` in `.env`

### For Security Workshop

The workshop requires additional environment variables. Copy `workshop/.env.sample` and configure:

```bash
cp workshop/.env.sample .env
```

See [workshop/README.md](workshop/README.md) and [workshop/.env.sample](workshop/.env.sample) for complete workshop configuration including:
- Azure AI Agent Service credentials (via Service Principal)
- GitHub Personal Access Token
- APIM gateway configuration

## 📚 Jupyter Notebook Contents

The `agent_framework.ipynb` tutorial is organized into 12 progressive sections:

| # | Section | What You'll Learn |
|---|---------|------------------|
| **0** | Shared Setup | Environment, models, sample data |
| **1** | Basic Agent | Create and run your first agent |
| **2** | Streaming | Real-time token streaming |
| **3** | Multi-Turn Conversations | Thread-based memory |
| **4** | Function Tools | Add custom capabilities |
| **5** | Human-in-the-Loop | Approval workflows |
| **6** | Middleware | Logging & observability |
| **7** | Memory | Persistent user context |
| **8** | Sequential Workflows | Classify → Draft → Review |
| **9** | Branching Logic | Spam vs. NotSpam vs. Uncertain |
| **10** | Fan-Out/Fan-In | Parallel processing |
| **11** | Multi-Agent Group Chat | Team collaboration |
| **12** | Capstone Demo | End-to-end system |

## 📖 Learn More

- [Agent Framework Documentation](https://github.com/microsoft/agent-framework)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)

## License

MIT
