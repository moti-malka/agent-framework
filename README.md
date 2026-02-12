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

### 2. **Agent Framework Security Workshop** (Hands-on Python Workshop)
A hands-on workshop teaching you to build AI-powered security scanning agents:

- 🔍 **4 specialized scanner agents** - secrets, code vulnerabilities, infrastructure, auth/crypto
- 🔧 **Repository access tools** - Using Model Context Protocol (MCP)
- 🧠 **Shared memory system** - Vulnerability tracking across agents
- 📋 **Structured output** - Pydantic models for consistent findings
- 📊 **Agent middleware** - Logging and observability
- 🔄 **Orchestrated workflow** - Coordinating all scanners for comprehensive security reports

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

**Option 2: Security Workshop**
```bash
# Navigate to the workshop directory
cd workshop

# Follow the workshop README for setup and challenges
# Complete 10 progressive challenges from basic repo access to full workflow orchestration
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
| **Challenge-Based Learning** | 10 progressive challenges from basics to advanced |
| **MCP Integration** | Model Context Protocol for repository access |
| **Security Scanners** | Specialized agents for secrets, code, infrastructure, auth/crypto |
| **Shared Memory** | Context providers for vulnerability tracking |
| **Structured Output** | Pydantic models for consistent security findings |
| **Agent Middleware** | Custom logging hooks for observability |
| **WorkflowBuilder** | Sequential and branching orchestration patterns |
| **Azure AI Agent Service** | Service principal authentication and project connection |

## 📁 Project Structure

```
agent-framework/
├── agent_framework.ipynb      # Interactive tutorial notebook (12 sections)
├── requirements.txt           # Python dependencies (agent-framework v1.0.0b260130)
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
├── docs/                      # HTML documentation pages
│   ├── index.html            # Main documentation landing page
│   ├── supportpilot.html     # Support email copilot guide
│   ├── businessbrain.html    # Business analysis agent guide
│   ├── devopsagent.html      # DevOps automation guide
│   ├── docmind.html          # Documentation agent guide
│   └── warroom.html          # Incident management guide
├── workshop/                  # Security workshop challenges
│   ├── README.md             # Workshop setup and guide
│   └── challenges/           # 10 progressive Python challenges
│       ├── challenge_01_repo_access.py
│       ├── challenge_02_file_tools.py
│       ├── challenge_03_memory.py
│       ├── challenge_04_secrets_scanner.py
│       ├── challenge_05_structured_output.py
│       ├── challenge_06_code_scanner.py
│       ├── challenge_07_infra_scanner.py
│       ├── challenge_08_auth_crypto_scanner.py
│       ├── challenge_09_middleware.py
│       ├── challenge_10_workflow.py
│       ├── shared_models.py
│       ├── SECURITY_GUIDE.md
│       └── expected_workflow_output.json
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

### Documentation
- Browse the `docs/` folder for HTML guides on various agent patterns
- Open `docs/index.html` in a browser for interactive documentation
- See `workshop/README.md` for detailed workshop setup instructions

### External Links
- [Agent Framework Documentation](https://github.com/microsoft/agent-framework)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

## License

MIT
