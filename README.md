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

### 2. **Security Scanning Workshop** (Hands-on Challenges)
A comprehensive workshop teaching you to build AI-powered security agents:

- 🔍 **MCP Integration** - Connect to GitHub repositories via Model Context Protocol
- 🛡️ **4 Specialized Scanners** - Secrets, code vulnerabilities, infrastructure, auth/crypto
- 🧠 **Shared Memory** - Track findings across multiple agents
- 📋 **Structured Output** - Use Pydantic models for consistent results
- 🔧 **Agent Middleware** - Add logging and observability
- 🔄 **Orchestrated Workflows** - Coordinate multiple agents with MagenticBuilder
- 🎯 **10 Progressive Challenges** - Build from basics to complete security scanning system

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

**Option 2: Security Scanning Workshop**
```bash
# Navigate to the workshop directory
cd workshop

# Follow the challenges sequentially
cd challenges
python challenge_01_repo_access.py    # Start with Challenge 01
python challenge_04_secrets_scanner.py # Test secrets scanner
python challenge_10_workflow.py        # Run complete workflow

# See workshop/README.md for complete instructions
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

### Security Workshop (`workshop/challenges/`)

| Feature | Challenge | Description |
|---------|-----------|-------------|
| **MCP Tools** | 01 | Model Context Protocol for GitHub access |
| **Function Tools** | 02 | Reusable file reading functions |
| **ContextProvider** | 03 | Shared memory for vulnerability tracking |
| **ChatAgent** | 04-08 | Specialized security scanner agents |
| **Structured Output** | 05 | Pydantic models for consistent findings |
| **Agent Middleware** | 09 | Logging and observability hooks |
| **MagenticBuilder** | 10 | Orchestrate 4 scanners into unified workflow |
| **Azure Authentication** | All | APIM, Service Principal, and token auth |

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
├── docs/                      # HTML documentation files
│   ├── index.html
│   ├── businessbrain.html
│   ├── devopsagent.html
│   ├── docmind.html
│   ├── supportpilot.html
│   └── warroom.html
├── workshop/                  # Security scanning workshop
│   ├── README.md              # Workshop instructions and setup
│   └── challenges/            # 10 progressive challenges
│       ├── SECURITY_GUIDE.md  # Vulnerability knowledge base
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
│       ├── shared_models.py   # Shared data models
│       └── expected_workflow_output.json
├── .github/                   # GitHub Actions workflows
│   ├── agents/
│   │   └── readme-updater.agent.md
│   └── workflows/
│       ├── notebook-sync.lock.yml
│       ├── notebook-sync.md
│       ├── readme-updater.lock.yml
│       └── readme-updater.md
└── README.md                  # This file
```

## 📝 Environment Variables

Create a `.env` file in the project root with the following variables:

### For Jupyter Notebook Tutorial

```bash
# Required: Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini

# Optional: API Key (if not using Azure CLI authentication)
AZURE_OPENAI_API_KEY=your-api-key

# Optional: API Version (defaults to 2025-01-01-preview)
API_VERSION=2025-01-01-preview
```

### For Security Workshop

```bash
# Azure OpenAI via APIM
AZURE_OPENAI_ENDPOINT=https://your-apim-instance.azure-api.net/openai/
AZURE_OPENAI_API_KEY=your-apim-subscription-key
AZURE_OPENAI_DEPLOYMENT=gpt-4o
AZURE_OPENAI_API_VERSION=2024-07-01-preview

# Azure AI Agent Service (Service Principal)
PROJECT_CONNECTION_STRING=your-project-connection-string
AZURE_CLIENT_ID=your-sp-client-id
AZURE_CLIENT_SECRET=your-sp-secret
AZURE_TENANT_ID=your-tenant-id

# GitHub Access
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token_here
```

**Authentication Options:**
1. **Azure CLI** (notebook): Run `az login` before starting
2. **API Key** (notebook): Set `AZURE_OPENAI_API_KEY` in `.env`
3. **APIM + Service Principal** (workshop): Required for MCP and Azure AI Agent Service

## 📖 Learn More

### Jupyter Notebook Tutorial

The `agent_framework.ipynb` tutorial is organized into 12 progressive sections covering all framework capabilities. See the full table of contents in the notebook.

### Security Workshop

The `workshop/` directory contains a comprehensive hands-on workshop teaching AI-powered security scanning. See [workshop/README.md](workshop/README.md) for:
- Complete setup instructions
- 10 progressive challenges (MCP integration → orchestrated workflows)
- Security vulnerability knowledge base
- Troubleshooting guide
- Achievement tiers and scoring

### External Resources

- [Agent Framework Documentation](https://github.com/microsoft/agent-framework)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Azure AI Foundry](https://ai.azure.com/)

## License

MIT
