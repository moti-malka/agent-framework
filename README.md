# 🛡️ Microsoft Agent Framework — Learning Examples

A comprehensive collection of learning resources for building AI-powered security and automation systems using the **Microsoft Agent Framework**. This repository includes a hands-on security workshop and an interactive Jupyter notebook demonstrating advanced orchestration patterns.

## 🎯 What's Included

This repository contains two main learning paths:

### 1. **Security Workshop** (`workshop/`)
A hands-on workshop where you build a multi-agent security scanning system:

- 🔐 **Secrets Scanner** - Detects hardcoded API keys, passwords, and credentials
- 🐛 **Code Vulnerability Scanner** - Finds injection, XSS, SSRF patterns
- ⚙️ **Infrastructure Scanner** - Audits Docker, Terraform, CI/CD configs
- 🔒 **Auth & Crypto Scanner** - Identifies weak hashing and JWT flaws
- 🔄 **Orchestrated Workflow** - Coordinates all scanners with scoring
- 📊 **Structured Output** - Pydantic models for consistent findings
- 🔗 **MCP Integration** - Model Context Protocol for GitHub access
- 📝 **Middleware & Memory** - Logging and cross-agent state sharing

**11 progressive challenges** teaching agent development, MCP tools, context providers, middleware, and workflow orchestration.

### 2. **Interactive Tutorial** (`agent_framework.ipynb`)
A Jupyter notebook demonstrating framework capabilities through an email copilot:

- ✅ **ChatAgent** fundamentals with streaming and threads
- ✅ **Function Tools** with `@tool` decorator
- ✅ **Human-in-the-Loop** approval workflows
- ✅ **Context Providers** for memory and state management
- ✅ **Middleware** for logging and observability
- ✅ **WorkflowBuilder** for sequential, branching, and parallel patterns
- ✅ **Multi-Agent Coordination** with Concurrent and Magentic builders

## 🚀 Quick Start

### Prerequisites

1. ✅ **Python 3.10+** with pip
2. ✅ **Azure OpenAI** via API Management (APIM)
3. ✅ **Azure AI Agent Service** via Service Principal (for workshop)
4. ✅ **GitHub Personal Access Token** (for workshop)
5. ✅ **VS Code** (recommended)

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
# Copy the sample and fill in your credentials:
cp workshop/.env.sample .env

# 5. Verify setup
cd workshop/challenge-1
python challenge_01_repo_access.py
```

### Running the Examples

**Option 1: Security Workshop (Recommended)**
```bash
# Start with Challenge 0 for environment setup
cd workshop/challenge-0
# Read README.md and follow setup instructions

# Then proceed through challenges 1-10
cd ../challenge-1
python challenge_01_repo_access.py
# Continue with subsequent challenges...
```

**Option 2: Jupyter Notebook Tutorial**
```bash
# Open the notebook
jupyter notebook agent_framework.ipynb
# Or open in VS Code with Jupyter extension
```

## 🏗️ Framework Features Demonstrated

### Security Workshop (`workshop/`)

| Feature | Challenge | Description |
|---------|-----------|-------------|
| **MCP Integration** | 1 | Model Context Protocol for GitHub repository access |
| **@tool Decorator** | 2 | Reusable file reading tools |
| **BaseContextProvider** | 3 | Scan memory for tracking vulnerabilities across agents |
| **Middleware** | 4 | Agent and tool logging with chained middleware |
| **Specialized Agents** | 5-9 | Domain-specific scanners (secrets, code, infra, auth) |
| **Structured Output** | 6 | `response_format` with Pydantic models |
| **WorkflowBuilder** | 10 | Orchestration with sequential and parallel patterns |
| **AgentExecutor** | 10 | Wrap agents for workflow integration |
| **Scoring System** | 10 | Aggregate findings and calculate security scores |

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

## 📁 Project Structure

```
agent-framework/
├── workshop/                     # Security workshop (11 challenges)
│   ├── challenge-0/              # Environment setup
│   ├── challenge-1/              # MCP repository access
│   ├── challenge-2/              # File reading tools
│   ├── challenge-3/              # Scan memory (context provider)
│   ├── challenge-4/              # Observability middleware
│   ├── challenge-5/              # Secrets scanner agent
│   ├── challenge-6/              # Structured output with Pydantic
│   ├── challenge-7/              # Code vulnerability scanner
│   ├── challenge-8/              # Infrastructure scanner
│   ├── challenge-9/              # Auth & crypto scanner
│   ├── challenge-10/             # Orchestrated workflow
│   ├── README.md                 # Workshop overview
│   ├── SECURITY_GUIDE.md         # Vulnerability knowledge base
│   ├── .env.sample               # Environment template
│   ├── shared_models.py          # Pydantic models & factories
│   ├── expected_workflow_output.json  # Target output structure
│   └── images/                   # Workshop diagrams
├── docs/                         # HTML documentation
│   ├── index.html                # Main documentation portal
│   ├── businessbrain.html        # BusinessBrain agent example
│   ├── devopsagent.html          # DevOps agent example
│   ├── docmind.html              # DocMind agent example
│   ├── supportpilot.html         # Support Pilot example
│   └── warroom.html              # WarRoom agent example
├── images/                       # Architecture diagrams
│   ├── agent-components.png
│   ├── concurrent-workflow.png
│   ├── group-chat.png
│   ├── handoff-workflow.png
│   ├── magentic-workflow.png
│   ├── sequential-workflow.png
│   ├── threads-and-memory.png
│   └── workflow-example.png
├── agent_framework.ipynb         # Interactive tutorial (12 sections)
├── requirements.txt              # Python dependencies
├── .env                          # Your credentials (create from .env.sample)
├── .venv/                        # Python virtual environment
└── README.md                     # This file
```

## 📝 Environment Variables

Create a `.env` file in the project root with the following variables (copy from `workshop/.env.sample`):

```bash
# Azure OpenAI Configuration (via APIM)
AZURE_OPENAI_ENDPOINT=https://your-apim-gateway.azure-api.net
AZURE_OPENAI_API_KEY=your-apim-subscription-key
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini
API_VERSION=2025-01-01-preview

# Azure AI Agent Service (for workshop)
AZURE_AI_AGENT_SERVICE_ENDPOINT=https://your-project.cognitiveservices.azure.com
AZURE_AI_PROJECT_ID=your-project-id
AZURE_AI_CLIENT_ID=your-service-principal-client-id
AZURE_AI_CLIENT_SECRET=your-service-principal-secret
AZURE_AI_TENANT_ID=your-tenant-id

# GitHub Access (for workshop)
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token_here
TARGET_REPO_OWNER=repo-owner
TARGET_REPO_NAME=repo-name

# Optional: MCP Server Configuration
MCP_GITHUB_TRANSPORT=stdio
```

**For Notebook Only**: You only need Azure OpenAI variables (`AZURE_OPENAI_*`)

**For Workshop**: All variables are required. See `workshop/.env.sample` for detailed descriptions.

## 📚 Learning Paths

### Security Workshop Challenges

The `workshop/` directory contains 11 progressive challenges:

| # | Challenge | Duration | Description |
|---|-----------|----------|-------------|
| **0** | [Environment Setup](workshop/challenge-0/README.md) | 20 min | Configure Azure and GitHub credentials |
| **1** | [MCP Repository Access](workshop/challenge-1/README.md) | 15 min | Connect to GitHub via Model Context Protocol |
| **2** | [File Reading Tools](workshop/challenge-2/README.md) | 15 min | Create reusable `@tool` functions |
| **3** | [Scan Memory](workshop/challenge-3/README.md) | 20 min | Build `BaseContextProvider` for cross-agent state |
| **4** | [Observability Middleware](workshop/challenge-4/README.md) | 15 min | Add logging with middleware chains |
| **5** | [Secrets Scanner](workshop/challenge-5/README.md) | 20 min | Detect hardcoded secrets and API keys |
| **6** | [Structured Output](workshop/challenge-6/README.md) | 15 min | Use `response_format` with Pydantic |
| **7** | [Code Vulnerability Scanner](workshop/challenge-7/README.md) | 20 min | Find injection, XSS, SSRF patterns |
| **8** | [Infrastructure Scanner](workshop/challenge-8/README.md) | 20 min | Audit Docker, Terraform, CI/CD configs |
| **9** | [Auth & Crypto Scanner](workshop/challenge-9/README.md) | 20 min | Detect weak hashing and JWT flaws |
| **10** | [Orchestrated Workflow](workshop/challenge-10/README.md) | 30 min | Coordinate scanners into scored workflow |

**Total Duration:** ~3.5 hours

### Jupyter Notebook Tutorial

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

- [Microsoft Agent Framework Documentation](https://aka.ms/agent-framework)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Azure AI Foundry](https://ai.azure.com/)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

## 🎓 Additional Resources

- **[SECURITY_GUIDE.md](workshop/SECURITY_GUIDE.md)** — Vulnerability knowledge base for security scanners
- **[HTML Documentation](docs/index.html)** — Agent examples and use cases
- **[Workshop Images](workshop/images/)** — Architecture diagrams and visualizations

## License

MIT
