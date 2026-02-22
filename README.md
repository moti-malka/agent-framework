# 📧 Microsoft Agent Framework — Learning Examples

A comprehensive collection of learning resources for building AI-powered systems using the **Microsoft Agent Framework**. This repository includes both an interactive Jupyter notebook tutorial and standalone Python examples demonstrating advanced orchestration patterns.

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

### 2. **Startup Idea Analyzer** (Standalone Python Script)
A Magentic orchestration demo featuring collaborative AI agents:

- 🔍 **Market Researcher** - Pessimistic analyst focused on risks
- 💰 **Financial Analyst** - Optimistic view on revenue potential
- ⚙️ **Tech Advisor** - Skeptical technical feasibility assessor
- 🎯 **Magentic Manager** - Coordinates the team and balances perspectives
- 📄 **Live Logging** - Real-time Markdown discussion logs
- ⚡ **Streaming Output** - See agent discussions as they happen
- 🔄 **Human-in-the-Loop** - Optional plan review and approval

### 3. **Security Workshop** (Hands-on Challenges)
A progressive 10-challenge workshop teaching AI-powered security scanning:

- 🔐 **Build security scanner agents** - Detect secrets, code vulnerabilities, misconfigurations
- 🔗 **MCP GitHub Integration** - Connect agents to real repositories via Model Context Protocol
- 🧠 **Shared Memory** - Cross-agent coordination with context providers
- 📊 **Structured Output** - Consistent findings with Pydantic models
- 🔄 **Workflow Orchestration** - Coordinate multiple scanners into scored reports
- 🏆 **VULN-HUNT Competition** - Live leaderboard game with real-time scoring

## 🚀 Quick Start

### Prerequisites

**For Notebook & Magentic Examples:**
1. ✅ **Azure subscription** with access to Azure OpenAI
2. ✅ **Azure OpenAI resource** with a deployed model (e.g., `gpt-4o-mini`)
3. ✅ **Azure CLI** installed and authenticated (`az login`)
4. ✅ **Python 3.10+**
5. ✅ **Azure AI Foundry project** *(Section 7 — MCP Integration only)*
   - **Project endpoint** — found in your project's **Overview** page
   - **Model deployment name** — found in your project's **Models + endpoints** page

**Additional for Security Workshop:**
6. ✅ **GitHub Personal Access Token** with repo access
7. ✅ **Azure AI Agent Service** via Service Principal (for MCP integration)

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
# Copy the example file and fill in your values:
cp .env.example .env
# Then edit .env with your Azure OpenAI and GitHub credentials
# See "Environment Variables" section below for details

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

**Option 3: Security Workshop**
```bash
# Navigate to workshop directory
cd workshop

# Start with Challenge 0 for setup
# Then progress through challenges 1-10
cd challenge-1
python challenge_01_repo_access.py

# See workshop/README.md for complete challenge list
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
├── .env.example               # Environment variable template
├── .env                       # Your configuration (create from .env.example)
├── .venv/                     # Python virtual environment
├── images/                    # Architecture and workflow diagrams
├── docs/                      # HTML documentation pages
├── workshop/                  # Security scanning workshop (10 challenges)
│   ├── README.md              # Workshop overview and challenge list
│   ├── SECURITY_GUIDE.md      # Vulnerability knowledge base
│   ├── .env.sample            # Workshop environment template
│   ├── challenge-0/           # Environment setup
│   ├── challenge-1/           # MCP repository access
│   ├── challenge-2/           # File reading tools
│   ├── challenge-3/           # Scan memory
│   ├── challenge-4/           # Observability middleware
│   ├── challenge-5/           # Secrets scanner
│   ├── challenge-6/           # Structured output
│   ├── challenge-7/           # Code vulnerability scanner
│   ├── challenge-8/           # Infrastructure scanner
│   ├── challenge-9/           # Auth and crypto scanner
│   ├── challenge-10/          # Orchestrated workflow
│   └── shared_models.py       # Common Pydantic models
├── discussions/               # Created by magentic_example.py at runtime
└── README.md                  # This file
```

## 📝 Environment Variables

Create a `.env` file by copying `.env.example`:

```bash
cp .env.example .env
```

**Required variables** (see `.env.example` for complete template):

```bash
# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini
AZURE_OPENAI_API_KEY=your-api-key  # Optional if using Azure CLI auth

# For MCP Integration (Section 7 / Workshop)
AZURE_AI_PROJECT_ENDPOINT=https://<resource>.services.ai.azure.com/api/projects/<project>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o-mini
```

**For Security Workshop** (`workshop/.env.sample`):
- GitHub Personal Access Token
- Azure AI Agent Service credentials
- See `workshop/.env.sample` for complete workshop configuration

**Authentication Options:**
1. **Azure CLI** (recommended): Run `az login` before starting
2. **API Key**: Set `AZURE_OPENAI_API_KEY` in `.env`

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

## 🔐 Security Workshop

The `workshop/` directory contains a comprehensive hands-on workshop for building AI-powered security scanning systems. Progress through 10 challenges to create specialized scanner agents that detect vulnerabilities in GitHub repositories.

### Workshop Highlights

- **Progressive Learning**: Start with MCP basics, advance to multi-agent orchestration
- **Real Security Scanning**: Build agents that find secrets, code vulnerabilities, and misconfigurations
- **Live Competition**: Test your scanners in the VULN-HUNT leaderboard game
- **Production Patterns**: Learn context providers, middleware, structured outputs, and workflow orchestration

### Challenge Overview

| Challenge | Focus | Key Concepts |
|-----------|-------|--------------|
| 0-1 | Setup & MCP | Environment configuration, GitHub repository access |
| 2-4 | Agent Infrastructure | Custom tools, shared memory, middleware |
| 5-9 | Security Scanners | Secrets, code vulns, infrastructure, auth/crypto |
| 10 | Workflow | Sequential orchestration, scoring, aggregation |

**Get Started**: See [workshop/README.md](workshop/README.md) for detailed instructions and challenge descriptions.

## 📖 Learn More

- [Agent Framework Documentation](https://github.com/microsoft/agent-framework)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)

## License

MIT
