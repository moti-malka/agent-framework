# 🤖 Microsoft Agent Framework — Learning Repository

A comprehensive collection of learning resources for building AI-powered systems using the **Microsoft Agent Framework**. This repository offers two complementary learning paths: an interactive Jupyter notebook tutorial covering core concepts and a hands-on security workshop with 10 progressive challenges.

## 🎯 What's Included

This repository offers two learning paths:

### 1. **Interactive Jupyter Notebook Tutorial** (`agent_framework.ipynb`)
A 12-section progressive tutorial teaching framework fundamentals:

- ✅ **Core Concepts** - Agents, streaming, threads, and memory
- ✅ **Function Tools** - Custom capabilities with `@tool` decorator
- ✅ **Human-in-the-Loop** - Approval workflows for sensitive operations
- ✅ **Middleware** - Logging and observability hooks
- ✅ **Context Providers** - Persistent memory across conversations
- ✅ **Workflow Patterns** - Sequential, branching, fan-out/fan-in orchestration
- ✅ **Multi-Agent Collaboration** - Concurrent and Magentic team coordination
- 🎓 **Example Use Case** - Email copilot for customer support

### 2. **Security Workshop** (`workshop/`)
A hands-on workshop building AI-powered security scanning agents:

- 🛡️ **10 Progressive Challenges** - From basics to complete workflow orchestration
- 🔍 **4 Specialized Scanners** - Secrets, code vulnerabilities, infrastructure, auth/crypto
- 🔧 **MCP Integration** - Model Context Protocol for GitHub repository access
- 🧠 **Shared Memory** - Context providers for vulnerability tracking
- 📊 **Structured Output** - Pydantic models for consistent findings
- 🎯 **Scoring System** - Automated evaluation with achievement tiers (Bronze → Diamond)
- 📖 **Security Knowledge Base** - Guided learning on vulnerability detection patterns

For detailed workshop instructions, see [workshop/README.md](workshop/README.md).

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

**Jupyter Notebook Tutorial**
```bash
# Open the interactive notebook
jupyter notebook agent_framework.ipynb
# Or open in VS Code with Jupyter extension
```

**Security Workshop**
```bash
# See the workshop README for detailed instructions
cd workshop
cat README.md

# Quick test of Challenge 01
python run_tests.py --only 1

# Run final workflow (Challenge 10)
python run_tests.py --only 10
```

For comprehensive workshop setup and testing instructions, see [workshop/README.md](workshop/README.md).

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

| Feature | Challenges | Description |
|---------|-----------|-------------|
| **MCP Tools** | 01 | Model Context Protocol for GitHub integration |
| **Tool Functions** | 02 | Reusable `@tool` decorated functions |
| **Context Providers** | 03 | Shared memory for vulnerability tracking |
| **Agent Instructions** | 04, 06-08 | Domain-specific scanner agents |
| **Structured Output** | 05 | Pydantic models for consistent data |
| **Agent Middleware** | 09 | Logging and observability patterns |
| **Workflow Orchestration** | 10 | MagenticBuilder coordinating multiple scanners |
| **Real-World Application** | All | Practical security scanning use case |

## 📁 Project Structure

```
agent-framework/
├── agent_framework.ipynb      # Interactive tutorial notebook (12 sections)
├── requirements.txt           # Python dependencies
├── .env                       # Azure OpenAI configuration (create this)
├── .venv/                     # Python virtual environment
├── workshop/                  # Security workshop with 10 challenges
│   ├── README.md              # Comprehensive workshop guide
│   └── challenges/            # Challenge implementation files
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
│       ├── SECURITY_GUIDE.md
│       ├── expected_workflow_output.json
│       └── shared_models.py
├── docs/                      # HTML documentation
│   ├── index.html
│   ├── supportpilot.html
│   ├── businessbrain.html
│   ├── devopsagent.html
│   ├── docmind.html
│   └── warroom.html
├── images/                    # Architecture and workflow diagrams
│   ├── agent-components.png
│   ├── concurrent-workflow.png
│   ├── group-chat.png
│   ├── magentic-workflow.png
│   ├── sequential-workflow.png
│   ├── threads-and-memory.png
│   └── workflow-example.png
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

**Note:** The security workshop has additional requirements (Azure AI Agent Service, GitHub token). See [workshop/README.md](workshop/README.md) for complete setup instructions.

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

## 🛡️ Security Workshop Challenges

The workshop consists of 10 progressive challenges teaching AI-powered security scanning:

| # | Challenge | What You'll Build | Key Concepts |
|---|-----------|-------------------|--------------|
| **01** | MCP Repo Access | GitHub repository connection | Model Context Protocol integration |
| **02** | File Reading Tools | Reusable file access functions | Tool encapsulation, error handling |
| **03** | Shared Memory | Vulnerability tracking system | Context providers, memory persistence |
| **04** | Secrets Scanner | Detect hardcoded credentials | Pattern matching, security analysis |
| **05** | Structured Output | Consistent finding reports | Pydantic models, type safety |
| **06** | Code Vulnerability Scanner | Find injection, XSS, SSRF | Code analysis, security patterns |
| **07** | Infrastructure Scanner | Scan Docker, Terraform, CI/CD | Infrastructure as code security |
| **08** | Auth & Crypto Scanner | Authentication vulnerabilities | Cryptography best practices |
| **09** | Agent Middleware | Logging and observability | Middleware chains, debugging |
| **10** | Orchestrated Workflow | Complete scanning system | Workflow coordination, scoring |

**Achievement System:**
- 💎 Diamond (90%+) - Security expert
- 🥇 Gold (75-89%) - Excellent detection
- 🥈 Silver (50-74%) - Good coverage
- 🥉 Bronze (25-49%) - Nice start

For detailed instructions, testing, and scoring, see [workshop/README.md](workshop/README.md).

## 📖 Learn More

- [Agent Framework Documentation](https://github.com/microsoft/agent-framework)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)

## License

MIT
