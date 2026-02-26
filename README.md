# 📧 Microsoft Agent Framework — Learning Examples

A comprehensive collection of learning resources for building AI-powered systems using the **Microsoft Agent Framework**. This repository includes both an interactive Jupyter notebook tutorial and a hands-on security workshop demonstrating advanced orchestration patterns.

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

### 2. **Security Scanning Workshop** (Hands-on Challenges)
A practical workshop building multi-agent security scanners:

- 🔍 **10 Progressive Challenges** - From setup to full orchestration
- 🛡️ **Specialized Scanner Agents** - Secrets, code vulnerabilities, infrastructure, auth/crypto
- 🔗 **MCP Integration** - Connect agents to GitHub repositories via Model Context Protocol
- 🧠 **Shared Memory** - Cross-agent coordination with context providers
- 📊 **Structured Output** - Pydantic models for consistent security findings
- 🎯 **Workflow Orchestration** - Coordinate multiple agents into a unified scanning workflow
- 🏆 **VULN-HUNT Competition** - Test your scanner against a live leaderboard

## 🚀 Quick Start

### Prerequisites

1. ✅ **Azure subscription** with access to Azure OpenAI
2. ✅ **Azure OpenAI resource** with a deployed model (e.g., `gpt-4o-mini`)
3. ✅ **Python 3.10+**
4. ✅ **Azure CLI** installed and authenticated (`az login`) *(optional authentication method)*

**For Security Workshop:**
- ✅ **GitHub Personal Access Token** with `repo` scope
- ✅ **Azure AI Agent Service** access via Service Principal

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
pip install -r requirements.txt --pre

# 4. Configure environment
# Copy the example file and fill in your credentials:
cp .env.example .env
# Edit .env with your Azure OpenAI configuration

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
# Navigate to workshop directory
cd workshop

# Start with Challenge 0 for environment setup
# Then progress through challenges 1-10
cd challenge-1
python challenge_01_repo_access.py

# See workshop/README.md for full details
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

| Feature | Challenges | Description |
|---------|-----------|-------------|
| **Model Context Protocol** | 1 | GitHub integration via MCP servers |
| **Custom Tools** | 2 | Reusable `@tool` functions for file operations |
| **Shared Memory** | 3 | BaseContextProvider for cross-agent state |
| **Middleware Chains** | 4 | Logging and observability hooks |
| **Specialized Agents** | 5-9 | Role-based security scanners |
| **Structured Output** | 6 | Pydantic models with `response_format` |
| **Workflow Orchestration** | 10 | Sequential coordination of multiple agents |
| **Real-world Integration** | All | GitHub API, Azure OpenAI, Azure AI Agent Service |

## 📁 Project Structure

```
agent-framework/
├── agent_framework.ipynb      # Interactive tutorial notebook (12 sections)
├── requirements.txt           # Python dependencies
├── .env.example               # Azure OpenAI configuration template
├── .gitignore                 # Git ignore patterns
├── README.md                  # This file
│
├── docs/                      # HTML documentation for agent examples
│   ├── index.html            # Main documentation index
│   ├── businessbrain.html    # Business analysis agent
│   ├── devopsagent.html      # DevOps automation agent
│   ├── docmind.html          # Documentation agent
│   ├── supportpilot.html     # Support automation agent
│   └── warroom.html          # Incident management agent
│
├── images/                    # Architecture and workflow diagrams
│   ├── agent-components.png
│   ├── concurrent-workflow.png
│   ├── group-chat.png
│   ├── handoff-workflow.png
│   ├── magentic-workflow.png
│   ├── sequential-workflow.png
│   ├── threads-and-memory.png
│   └── workflow-example.png
│
├── workshop/                  # Security scanning workshop
│   ├── README.md             # Workshop guide and challenge overview
│   ├── SECURITY_GUIDE.md     # Vulnerability knowledge base
│   ├── .env.sample           # Workshop-specific environment variables
│   ├── shared_models.py      # Pydantic models and client factories
│   ├── expected_workflow_output.json  # Target JSON structure
│   ├── _paths.py             # Path utilities
│   ├── challenge-0/          # Environment setup
│   ├── challenge-1/          # MCP repository access
│   ├── challenge-2/          # File reading tools
│   ├── challenge-3/          # Scan memory
│   ├── challenge-4/          # Observability middleware
│   ├── challenge-5/          # Secrets scanner
│   ├── challenge-6/          # Structured output
│   ├── challenge-7/          # Code vulnerability scanner
│   ├── challenge-8/          # Infrastructure scanner
│   ├── challenge-9/          # Auth and crypto scanner
│   └── challenge-10/         # Orchestrated workflow
│
└── .github/                   # GitHub Actions workflows and agents
    ├── workflows/            # CI/CD automation
    └── agents/               # Custom agent definitions
```

## 📝 Environment Variables

### For Jupyter Notebook

Create a `.env` file in the project root with the following variables:

```bash
# Required: Azure OpenAI Configuration
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

### For Security Workshop

See `workshop/.env.sample` for additional variables required for the workshop:

```bash
# Workshop-specific variables (in addition to above)
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_xxxxx
SERVICE_PRINCIPAL_CLIENT_ID=xxxxx
SERVICE_PRINCIPAL_CLIENT_SECRET=xxxxx
SERVICE_PRINCIPAL_TENANT_ID=xxxxx
AZURE_AI_PROJECT_CONNECTION_STRING=xxxxx
TARGET_REPO_OWNER=owner
TARGET_REPO_NAME=repo
```

**Authentication Options:**
1. **Azure CLI** (recommended): Run `az login` before starting
2. **API Key**: Set `AZURE_OPENAI_API_KEY` in `.env`
3. **Service Principal**: Required for Azure AI Agent Service (workshop)

## 📚 Learning Path

### Jupyter Notebook Tutorial (`agent_framework.ipynb`)

The notebook is organized into 12 progressive sections:

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

### Security Workshop (`workshop/`)

Hands-on challenges building a complete security scanning system:

| Challenge | Title | Duration | Key Concepts |
|-----------|-------|----------|--------------|
| **0** | Environment Setup | 20 min | Azure, GitHub, credentials |
| **1** | MCP Repository Access | 15 min | Model Context Protocol, GitHub |
| **2** | File Reading Tools | 15 min | Custom `@tool` functions |
| **3** | Scan Memory | 20 min | BaseContextProvider, shared state |
| **4** | Observability Middleware | 15 min | Logging, debugging |
| **5** | Secrets Scanner | 20 min | Pattern detection, security |
| **6** | Structured Output | 15 min | Pydantic, `response_format` |
| **7** | Code Vulnerability Scanner | 20 min | Code analysis, OWASP |
| **8** | Infrastructure Scanner | 20 min | Docker, Terraform, CI/CD |
| **9** | Auth and Crypto Scanner | 20 min | Authentication, cryptography |
| **10** | Orchestrated Workflow | 30 min | Full pipeline, scoring |

**Bonus:** VULN-HUNT live competition to test your scanner against others!

## 📖 Learn More

- [Agent Framework Documentation](https://github.com/microsoft/agent-framework)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)

## License

MIT
