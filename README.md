# 📧 Microsoft Agent Framework — Learning Examples

A comprehensive collection of learning resources for building AI-powered systems using the **Microsoft Agent Framework**. This repository includes both an interactive Jupyter notebook tutorial and standalone Python examples demonstrating advanced orchestration patterns.

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

### 2. **Security Workshop** (Hands-on Python Challenges)
A progressive workshop teaching AI-powered security scanning:

- 🛡️ **10 progressive challenges** - Build from basics to complete workflow
- 🔍 **4 specialized scanner agents** - Secrets, code vulnerabilities, infrastructure, auth/crypto
- 🔧 **Model Context Protocol (MCP)** - GitHub repository integration
- 🧠 **Shared memory system** - Cross-agent vulnerability tracking
- 📊 **Structured output** - Pydantic models for consistent findings
- 🎯 **Orchestrated workflow** - Coordinate scanners into comprehensive reports
- 🏆 **Scoring system** - Achievement tiers from Bronze to Diamond

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
cd workshop/challenges

# Start with Challenge 01 and work through sequentially
# Each challenge file contains instructions and TODO sections

# Test individual challenges
python ../run_tests.py --only 1   # Test challenge 01
python ../run_tests.py --only 5   # Test challenge 05

# Run the complete workflow (Challenge 10)
python ../run_tests.py --only 10

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

### Security Workshop (`workshop/challenges/`)

| Feature | Description |
|---------|-------------|
| **MCP Integration** | Model Context Protocol for GitHub repository access |
| **Context Providers** | Shared memory for cross-agent vulnerability tracking |
| **Structured Output** | Pydantic models for type-safe findings |
| **Scanner Agents** | Specialized agents for secrets, code, infrastructure, auth/crypto |
| **Workflow Orchestration** | MagenticBuilder for coordinated multi-agent scanning |
| **Agent Middleware** | Logging and observability hooks |
| **Progressive Learning** | 10 challenges from basics to complete workflow |
| **Scoring System** | Automated evaluation with achievement tiers |

## 📁 Project Structure

```
agent-framework/
├── agent_framework.ipynb      # Interactive tutorial notebook (12 sections)
├── requirements.txt           # Python dependencies
├── .env                       # Azure OpenAI configuration (create this)
├── .venv/                     # Python virtual environment
├── workshop/                  # Security workshop challenges
│   ├── README.md              # Workshop instructions
│   └── challenges/            # 10 progressive challenges
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
│       └── expected_workflow_output.json
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
│   ├── businessbrain.html
│   ├── devopsagent.html
│   ├── docmind.html
│   ├── supportpilot.html
│   └── warroom.html
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

## 🛡️ Security Workshop

The `workshop/` directory contains a comprehensive hands-on workshop for building AI-powered security scanning agents. See [workshop/README.md](workshop/README.md) for complete instructions.

**Workshop Highlights:**
- 10 progressive challenges building from basics to complete workflow
- Learn to create specialized security scanner agents
- Master Model Context Protocol (MCP) for repository integration
- Build orchestrated multi-agent workflows
- Implement shared memory and structured outputs
- Score your results with automated evaluation

**Quick Start:**
```bash
cd workshop/challenges
# Follow instructions in workshop/README.md
python ../run_tests.py --only 1  # Start with Challenge 01
```

## 📖 Learn More

- [Agent Framework Documentation](https://github.com/microsoft/agent-framework)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)
- [Workshop Guide](workshop/README.md)

## License

MIT
