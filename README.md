# 📧 Microsoft Agent Framework — Learning Examples

A comprehensive collection of learning resources for building AI-powered systems using the **Microsoft Agent Framework**. This repository includes an interactive Jupyter notebook tutorial and a hands-on security workshop with real-world challenges.

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

### 2. **Agent Framework Security Workshop**
A hands-on workshop building AI-powered security scanning agents:

- 🔐 **10 Progressive Challenges** - From setup to full workflow orchestration
- 🛡️ **Specialized Scanners** - Secrets, code vulnerabilities, infrastructure, auth/crypto
- 🔗 **MCP Integration** - GitHub repository access via Model Context Protocol
- 🧠 **Shared Memory** - Cross-agent state coordination
- 📊 **Structured Output** - Pydantic models for consistent findings
- 🔄 **Workflow Orchestration** - Multi-agent collaboration patterns
- 🎯 **Achievement Tiers** - Score-based badges (Bronze to Diamond)

## 🚀 Quick Start

### Prerequisites

1. ✅ **Azure subscription** with access to Azure OpenAI
2. ✅ **Azure OpenAI resource** with a deployed model (e.g., `gpt-4o-mini`)
3. ✅ **Azure CLI** installed and authenticated (`az login`)
4. ✅ **Python 3.10+**
5. ✅ **Azure AI Foundry project** *(Notebook Section 7 — MCP Integration only)*
   - **Project endpoint** — found in your project's **Overview** page
   - **Model deployment name** — found in your project's **Models + endpoints** page
6. ✅ **GitHub Personal Access Token** *(Workshop only)*
7. ✅ **Azure AI Agent Service** *(Workshop only)*

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
# Copy the example environment file and customize it:
cp .env.example .env

# Edit .env with your Azure OpenAI configuration:
# AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
# AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini
# AZURE_OPENAI_API_KEY=your-api-key  # Or use Azure CLI authentication
# API_VERSION=2025-01-01-preview  # Optional, defaults to this value

# For Section 7 (MCP Integration), also add:
# AZURE_AI_PROJECT_ENDPOINT=https://<resource>.services.ai.azure.com/api/projects/<project>
# AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o-mini

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
# Navigate to the workshop directory
cd workshop

# Follow the README for detailed instructions
# Start with Challenge 0 for environment setup, then proceed through Challenges 1-10

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

### Security Workshop (`workshop/`)

| Feature | Challenges | Description |
|---------|------------|-------------|
| **MCP Integration** | 1 | GitHub repository access via Model Context Protocol |
| **Custom Tools** | 2 | `@tool` decorator for file reading and code analysis |
| **BaseContextProvider** | 3 | Shared memory for cross-agent vulnerability tracking |
| **Middleware** | 4 | Logging, observability, and debugging hooks |
| **Specialized Agents** | 5-9 | Role-based scanners (secrets, code, infra, auth/crypto) |
| **Structured Output** | 6 | `response_format` with Pydantic for consistent findings |
| **Workflow Orchestration** | 10 | Multi-agent coordination with scored aggregation |

## 📁 Project Structure

```
agent-framework/
├── agent_framework.ipynb      # Interactive tutorial notebook (12 sections)
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variable template
├── .env                       # Your local config (create from .env.example)
├── .venv/                     # Python virtual environment
├── images/                    # Architecture and workflow diagrams
│   ├── agent-components.png
│   ├── concurrent-workflow.png
│   ├── group-chat.png
│   ├── magentic-workflow.png
│   ├── sequential-workflow.png
│   ├── threads-and-memory.png
│   └── workflow-example.png
├── docs/                      # HTML documentation pages
│   ├── index.html
│   ├── supportpilot.html
│   ├── businessbrain.html
│   ├── devopsagent.html
│   ├── docmind.html
│   └── warroom.html
├── workshop/                  # Security workshop (10 challenges)
│   ├── README.md              # Workshop overview and instructions
│   ├── SECURITY_GUIDE.md      # Vulnerability knowledge base
│   ├── .env.sample            # Workshop environment template
│   ├── shared_models.py       # Pydantic models and utilities
│   ├── _paths.py              # Path helpers
│   ├── expected_workflow_output.json  # Target output structure
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
│   └── challenge-10/          # Orchestrated workflow
└── README.md                  # This file
```

## 📝 Environment Variables

### For Jupyter Notebook

Create a `.env` file in the project root using `.env.example` as a template:

```bash
# Required: Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini

# Optional: API Key (if not using Azure CLI authentication)
AZURE_OPENAI_API_KEY=your-api-key

# Optional: API Version (defaults to 2025-01-01-preview)
API_VERSION=2025-01-01-preview

# Required for Section 7 only (MCP Integration)
AZURE_AI_PROJECT_ENDPOINT=https://<resource>.services.ai.azure.com/api/projects/<project>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o-mini
```

**Authentication Options:**
1. **Azure CLI** (recommended): Run `az login` before starting
2. **API Key**: Set `AZURE_OPENAI_API_KEY` in `.env`

### For Security Workshop

See `workshop/.env.sample` for additional workshop-specific variables including:
- Azure AI Agent Service credentials
- GitHub Personal Access Token
- Target repository configuration

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

### Documentation & Resources
- [Agent Framework Documentation](https://github.com/microsoft/agent-framework)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Azure AI Foundry](https://ai.azure.com/)

### Workshop Resources
- [Workshop README](workshop/README.md) — Full challenge guide
- [Security Guide](workshop/SECURITY_GUIDE.md) — Vulnerability detection reference
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — Web application security risks

## License

MIT
