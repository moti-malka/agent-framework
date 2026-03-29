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

### 2. **Security Workshop** (Hands-on Challenges)
A comprehensive hands-on workshop featuring multi-agent security scanning:

- 🔐 **Secrets Scanner** - Detects hardcoded API keys and credentials
- 🐛 **Code Vulnerability Scanner** - Finds injection, XSS, SSRF patterns
- 🏗️ **Infrastructure Scanner** - Scans Docker, Terraform, CI/CD configs
- 🔑 **Auth and Crypto Scanner** - Identifies weak hashing and JWT flaws
- 🔗 **MCP Integration** - Connects agents to GitHub via Model Context Protocol
- 🧠 **Shared Memory** - Cross-agent state coordination
- 📊 **Structured Output** - Pydantic models for consistent findings
- 🔄 **Workflow Orchestration** - Coordinates multiple specialized agents

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
# Navigate to the workshop directory
cd workshop

# Start with Challenge 0 for environment setup
# Then progress through 10 hands-on challenges
cd challenge-1
python challenge_01_repo_access.py

# Complete all challenges to build a full security scanning system
# See workshop/README.md for detailed instructions
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

| Feature | Description |
|---------|-------------|
| **MCP Protocol** | GitHub integration via Model Context Protocol |
| **Specialized Scanners** | Role-based security agents (secrets, code, infra, auth) |
| **Context Provider** | Shared scan memory across agents |
| **Structured Output** | Pydantic models with `response_format` |
| **Agent Middleware** | Custom logging and observability hooks |
| **Workflow Orchestration** | Sequential and parallel agent coordination |
| **Security Knowledge** | OWASP-based vulnerability detection patterns |
| **Achievement Tiers** | Scored challenges (Bronze to Diamond) |

## 📁 Project Structure

```
agent-framework/
├── agent_framework.ipynb      # Interactive tutorial notebook (12 sections)
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
├── workshop/                  # Security workshop with 10 hands-on challenges
│   ├── README.md              # Workshop instructions and architecture
│   ├── SECURITY_GUIDE.md      # Vulnerability knowledge base
│   ├── .env.sample            # Workshop environment template
│   ├── shared_models.py       # Pydantic models and factories
│   ├── challenge-0/           # Environment setup
│   ├── challenge-1/           # MCP repository access
│   ├── challenge-2/           # File reading tools
│   ├── challenge-3/           # Scan memory context
│   ├── challenge-4/           # Secrets scanner
│   ├── challenge-5/           # Structured output
│   ├── challenge-6/           # Code vulnerability scanner
│   ├── challenge-7/           # Infrastructure scanner
│   ├── challenge-8/           # Auth and crypto scanner
│   ├── challenge-9/           # Agent middleware
│   └── challenge-10/          # Orchestrated workflow
├── docs/                      # HTML documentation and examples
│   ├── index.html
│   ├── supportpilot.html
│   ├── businessbrain.html
│   ├── devopsagent.html
│   ├── docmind.html
│   └── warroom.html
└── README.md                  # This file
```

## 📝 Environment Variables

Create a `.env` file in the project root with the following variables:

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

## 📖 Additional Resources

### Security Workshop
- [Workshop README](workshop/README.md) - Complete workshop guide with all challenges
- [Security Guide](workshop/SECURITY_GUIDE.md) - Vulnerability patterns and detection techniques
- [Model Context Protocol](https://modelcontextprotocol.io/) - MCP specification and documentation

### Framework Documentation
- [Agent Framework Documentation](https://github.com/microsoft/agent-framework)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)
- [Azure AI Foundry](https://ai.azure.com/)

## License

MIT
