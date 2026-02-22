# 📧 Microsoft Agent Framework — Learning Examples

A comprehensive collection of learning resources for building AI-powered systems using the **Microsoft Agent Framework**. This repository includes an interactive Jupyter notebook tutorial and a hands-on security workshop with 10 progressive challenges.

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

### 2. **Agent Framework Security Workshop** (Hands-on Challenges)
A practical workshop with 10 progressive challenges building a multi-agent security scanner:

- 🔐 **MCP Integration** - Connect to GitHub repositories via Model Context Protocol
- 🛠️ **Function Tools** - Create reusable @tool decorators for file operations
- 💾 **Shared Memory** - Build context providers for cross-agent state
- 🔍 **Security Scanners** - Detect secrets, code vulnerabilities, infrastructure misconfigurations
- 🎯 **Workflow Orchestration** - Coordinate multiple specialist agents
- 📊 **Structured Output** - Use Pydantic models for consistent findings
- 🎮 **Competition Dashboard** - Live leaderboard for vulnerability hunting

## 🚀 Quick Start

### Prerequisites

1. ✅ **Azure subscription** with access to Azure OpenAI
2. ✅ **Azure OpenAI resource** with a deployed model (e.g., `gpt-4o-mini`)
3. ✅ **Azure CLI** installed and authenticated (`az login`)
4. ✅ **Python 3.10+**
5. ✅ **Azure AI Foundry project** *(Notebook Section 7 + Workshop)*
   - **Project endpoint** — found in your project's **Overview** page
   - **Model deployment name** — found in your project's **Models + endpoints** page
6. ✅ **GitHub Personal Access Token** *(Workshop only)*

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
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini
API_VERSION=2025-01-01-preview  # Optional, defaults to this value

# For Section 7 (MCP Integration) and Workshop:
AZURE_AI_PROJECT_ENDPOINT=https://<resource>.services.ai.azure.com/api/projects/<project>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o-mini

# For Workshop only:
GITHUB_TOKEN=ghp_your-github-token

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
# Navigate to the workshop directory
cd workshop

# Follow the progressive challenges (0-10)
# See workshop/README.md for detailed instructions

# Example: Run Challenge 1
cd challenge-1
python challenge_01_repo_access.py
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

### Workshop (`workshop/`)

| Feature | Description |
|---------|-------------|
| **Security Scanning Agents** | Specialized agents for secrets, code, infrastructure, and auth scanning |
| **MCP GitHub Integration** | Model Context Protocol for repository access |
| **Shared Memory** | BaseContextProvider for cross-agent vulnerability tracking |
| **Function Tools** | Reusable @tool decorators for file operations |
| **Structured Output** | Pydantic models for consistent security findings |
| **Middleware** | Logging and observability hooks |
| **Workflow Orchestration** | Sequential and parallel agent coordination |
| **Competition Dashboard** | Live leaderboard for vulnerability hunting |

## 📁 Project Structure

```
agent-framework/
├── agent_framework.ipynb      # Interactive tutorial notebook (12 sections)
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variable template
├── .venv/                     # Python virtual environment
├── images/                    # Architecture and workflow diagrams
│   ├── agent-components.png
│   ├── concurrent-workflow.png
│   ├── group-chat.png
│   ├── magentic-workflow.png
│   ├── sequential-workflow.png
│   ├── threads-and-memory.png
│   └── workflow-example.png
├── docs/                      # HTML documentation files
│   ├── index.html
│   ├── supportpilot.html
│   ├── devopsagent.html
│   ├── businessbrain.html
│   ├── docmind.html
│   └── warroom.html
├── workshop/                  # Security scanning workshop (10 challenges)
│   ├── README.md              # Workshop instructions
│   ├── SECURITY_GUIDE.md      # Security scanning guide
│   ├── .env.sample            # Workshop-specific environment template
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
│   ├── shared_models.py       # Pydantic models for findings
│   └── images/                # Workshop diagrams
└── README.md                  # This file
```

## 📝 Environment Variables

Create a `.env` file in the project root with the following variables:

```bash
# Required: Azure OpenAI Configuration
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini

# Optional: API Version (defaults to 2025-01-01-preview)
API_VERSION=2025-01-01-preview

# Required for Notebook Section 7 and Workshop (MCP Integration)
# AZURE_AI_PROJECT_ENDPOINT: Azure AI Foundry → your project → Overview → Project endpoint
AZURE_AI_PROJECT_ENDPOINT=https://<resource>.services.ai.azure.com/api/projects/<project>
# AZURE_AI_MODEL_DEPLOYMENT_NAME: Azure AI Foundry → your project → Models + endpoints → Deployment name
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o-mini

# Required for Workshop only (GitHub Access)
GITHUB_TOKEN=ghp_your-github-token

# Optional: Service Principal for DefaultAzureCredential (Workshop)
# If set, DefaultAzureCredential uses these automatically (no az login needed)
AZURE_CLIENT_ID=<your-service-principal-client-id>
AZURE_TENANT_ID=<your-azure-tenant-id>
AZURE_CLIENT_SECRET=<your-service-principal-secret>
```

**Authentication Options:**
1. **Azure CLI** (recommended): Run `az login` before starting
2. **API Key**: Set `AZURE_OPENAI_API_KEY` in `.env`
3. **Service Principal** (workshop): Set `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_CLIENT_SECRET`

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

## 🔐 Security Workshop Contents

The `workshop/` directory contains a hands-on security scanning workshop with 10 progressive challenges:

| # | Challenge | Duration | What You'll Learn |
|---|-----------|----------|-------------------|
| **0** | [Environment Setup](workshop/challenge-0/README.md) | 20 min | Configure Azure and GitHub credentials |
| **1** | [MCP Repository Access](workshop/challenge-1/README.md) | 15 min | Connect to GitHub via Model Context Protocol |
| **2** | [File Reading Tools](workshop/challenge-2/README.md) | 15 min | Create reusable @tool functions |
| **3** | [Scan Memory](workshop/challenge-3/README.md) | 20 min | Build BaseContextProvider for vulnerability tracking |
| **4** | [Observability Middleware](workshop/challenge-4/README.md) | 15 min | Add logging and observability |
| **5** | [Secrets Scanner](workshop/challenge-5/README.md) | 20 min | Detect hardcoded secrets and API keys |
| **6** | [Structured Output](workshop/challenge-6/README.md) | 15 min | Use Pydantic models for findings |
| **7** | [Code Vulnerability Scanner](workshop/challenge-7/README.md) | 20 min | Find injection, XSS, SSRF patterns |
| **8** | [Infrastructure Scanner](workshop/challenge-8/README.md) | 20 min | Scan Docker, Terraform, CI/CD configs |
| **9** | [Auth and Crypto Scanner](workshop/challenge-9/README.md) | 20 min | Detect weak hashing and JWT flaws |
| **10** | [Orchestrated Workflow](workshop/challenge-10/README.md) | 30 min | Coordinate all scanners into scored workflow |

See [workshop/README.md](workshop/README.md) for detailed instructions and the competition dashboard.

## 📖 Learn More

- [Agent Framework Documentation](https://github.com/microsoft/agent-framework)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)

## License

MIT
