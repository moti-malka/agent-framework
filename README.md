# 📧 Microsoft Agent Framework — Learning Examples

A comprehensive collection of learning resources for building AI-powered systems using the **Microsoft Agent Framework**. This repository includes an interactive Jupyter notebook tutorial and a hands-on security workshop demonstrating advanced orchestration patterns.

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

### 2. **Agent Framework Security Workshop** (Python Challenges)
A hands-on workshop building a multi-agent security scanning system:

- 🔒 **10 Progressive Challenges** - From basic setup to orchestrated workflows
- 🔍 **Specialized Security Agents** - Secrets, code vulnerabilities, infrastructure, auth/crypto scanners
- 🔧 **Model Context Protocol (MCP)** - GitHub repository integration
- 🧠 **Shared Memory** - Cross-agent state coordination with context providers
- 📊 **Structured Output** - Pydantic models for consistent security findings
- 🔄 **Workflow Orchestration** - Coordinate multiple agents into unified security reports
- 📈 **Achievement System** - Score-based vulnerability detection goals (Bronze to Diamond tiers)

## 🚀 Quick Start

### Prerequisites

1. ✅ **Python 3.10+**
2. ✅ **Azure subscription** with access to Azure OpenAI or Azure AI Agent Service
3. ✅ **Azure OpenAI resource** with a deployed model (e.g., `gpt-4o-mini`)
4. ✅ **Azure CLI** installed and authenticated (`az login`) — for CLI-based authentication
5. ✅ **GitHub Personal Access Token** — required for workshop challenges

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

# For workshop challenges, also add:
GITHUB_PERSONAL_ACCESS_TOKEN=your-github-pat  # Required for MCP GitHub integration

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

**Option 2: Security Workshop Challenges**
```bash
# Start with Challenge 0 for environment setup
cd workshop/challenge-0
# Follow the README.md in each challenge directory

# Then proceed through challenges 1-10
cd ../challenge-1
python challenge_01_repo_access.py

# See workshop/README.md for full challenge list and instructions
```

## 🏗️ Framework Features Demonstrated

### Jupyter Notebook (`agent_framework.ipynb`)

| Feature | Section | Description |
|---------|---------|-------------|
| **Agent** | 1-3 | Core agent with instructions, streaming, threads |
| **Function Tools** | 4 | `@tool` decorator for custom capabilities |
| **Approval Mode** | 5 | `approval_mode="always_require"` for HITL |
| **Middleware** | 6 | Agent and function invocation hooks |
| **BaseContextProvider** | 7 | Memory with `invoking`/`invoked` lifecycle |
| **WorkflowBuilder** | 8-10 | Sequential, branching, fan-out patterns |
| **AgentExecutor** | 8-10 | Wrap agents for workflow orchestration |
| **Switch-Case** | 9 | Multi-way routing with `Case`/`Default` |
| **Multi-Selection** | 10 | Dynamic fan-out to parallel paths |
| **Fan-In** | 10 | Aggregate results from parallel execution |
| **ConcurrentBuilder** | 11 | Parallel multi-agent processing |
| **MagenticBuilder** | 11 | Manager-orchestrated agent teams |

### Security Workshop (`workshop/`)

| Feature | Description |
|---------|-------------|
| **MCP Integration** | Model Context Protocol for GitHub repository access |
| **Tool Functions** | Reusable `@tool` decorators for file operations |
| **Context Providers** | Shared memory and state management across agents |
| **Structured Output** | Pydantic models with `response_format` for consistent findings |
| **Agent Middleware** | Custom logging and observability hooks |
| **Workflow Orchestration** | Coordinate multiple specialized security scanners |
| **Azure AI Agent Service** | Integration with Azure AI Foundry for agent execution |

## 📁 Project Structure

```
agent-framework/
├── agent_framework.ipynb      # Interactive tutorial notebook (12 sections)
├── requirements.txt           # Python dependencies (agent-framework 1.0.0b260212)
├── .env                       # Azure OpenAI + GitHub configuration (create this)
├── .venv/                     # Python virtual environment
├── images/                    # Architecture and workflow diagrams
│   ├── agent-components.png
│   ├── concurrent-workflow.png
│   ├── group-chat.png
│   ├── handoff-workflow.png
│   ├── magentic-workflow.png
│   ├── sequential-workflow.png
│   ├── threads-and-memory.png
│   └── workflow-example.png
├── workshop/                  # Security workshop challenges (10 challenges)
│   ├── README.md              # Workshop overview and instructions
│   ├── SECURITY_GUIDE.md      # Vulnerability knowledge base
│   ├── .env.sample            # Environment template
│   ├── shared_models.py       # Pydantic models and utilities
│   ├── expected_workflow_output.json  # Target output structure
│   ├── challenge-0/           # Environment setup
│   ├── challenge-1/           # MCP repository access
│   ├── challenge-2/           # File reading tools
│   ├── challenge-3/           # Scan memory context provider
│   ├── challenge-4/           # Secrets scanner
│   ├── challenge-5/           # Structured output
│   ├── challenge-6/           # Code vulnerability scanner
│   ├── challenge-7/           # Infrastructure scanner
│   ├── challenge-8/           # Auth and crypto scanner
│   ├── challenge-9/           # Agent middleware
│   └── challenge-10/          # Orchestrated workflow
├── docs/                      # Additional documentation and examples
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

# Required for Workshop: GitHub Personal Access Token
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token_here

# Optional for Workshop: Azure AI Agent Service
AZURE_AI_AGENT_SERVICE_ENDPOINT=https://your-project.api.azureml.ms
AZURE_AI_AGENT_SERVICE_API_KEY=your-service-key
```

**Authentication Options:**
1. **Azure CLI** (recommended): Run `az login` before starting
2. **API Key**: Set `AZURE_OPENAI_API_KEY` in `.env`
3. **Service Principal**: For Azure AI Agent Service in workshop challenges

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

## 🔒 Security Workshop Challenges

The `workshop/` directory contains 10 hands-on challenges building a multi-agent security scanning system:

| # | Challenge | Duration | What You'll Build |
|---|-----------|----------|-------------------|
| **0** | [Environment Setup](workshop/challenge-0/README.md) | 20 min | Azure and GitHub credentials |
| **1** | [MCP Repository Access](workshop/challenge-1/README.md) | 15 min | Connect to GitHub via MCP |
| **2** | [File Reading Tools](workshop/challenge-2/README.md) | 15 min | Reusable @tool functions |
| **3** | [Scan Memory](workshop/challenge-3/README.md) | 20 min | Context provider for cross-agent state |
| **4** | [Secrets Scanner](workshop/challenge-4/README.md) | 20 min | Detect hardcoded credentials |
| **5** | [Structured Output](workshop/challenge-5/README.md) | 15 min | Pydantic response models |
| **6** | [Code Vulnerability Scanner](workshop/challenge-6/README.md) | 20 min | Find injection and XSS flaws |
| **7** | [Infrastructure Scanner](workshop/challenge-7/README.md) | 20 min | Docker, Terraform, CI/CD checks |
| **8** | [Auth and Crypto Scanner](workshop/challenge-8/README.md) | 20 min | Weak hashing and JWT issues |
| **9** | [Agent Middleware](workshop/challenge-9/README.md) | 15 min | Logging and observability |
| **10** | [Orchestrated Workflow](workshop/challenge-10/README.md) | 30 min | Coordinate all scanners |

See [workshop/README.md](workshop/README.md) for complete workshop guide and achievement tiers.

## 📖 Learn More

- [Microsoft Agent Framework Documentation](https://aka.ms/agent-framework)
- [Agent Framework on GitHub](https://github.com/microsoft/agent-framework)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)
- [Azure AI Foundry](https://ai.azure.com/)

## License

MIT
