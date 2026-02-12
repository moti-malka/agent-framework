# Challenge 0 — Environment Setup & Prerequisites

**Expected Duration:** 20 minutes

Welcome to the first challenge! Your goal is to set up the development environment and verify that all required services are accessible before diving into the hands-on challenges.

## Learning Objectives

- Set up your local Python development environment
- Configure Azure OpenAI, Azure AI Agent Service, and GitHub credentials
- Verify connectivity to all required services

## Prerequisites

### Required Software

| Tool | Version | Purpose |
|------|---------|---------|
| **Python** | 3.10+ | Runtime |
| **pip** | Latest | Package management |
| **VS Code** | Latest | IDE (recommended) |
| **Git** | Latest | Repository cloning |

### Required Azure Services

#### 1. Azure OpenAI via API Management (APIM)

You need an Azure OpenAI instance accessible through API Management:
- **Model**: `gpt-4o` or `gpt-4o-mini` deployed
- **APIM Gateway URL**: Your API Management gateway endpoint
- **API Key**: Your APIM subscription key

#### 2. Azure AI Agent Service (via Service Principal)

You need a Service Principal with access to Azure AI Agent Service:
- **Project Endpoint**: From Azure AI Foundry portal
- **Client Credentials**: Service principal with appropriate permissions

#### 3. GitHub Personal Access Token

Required for scanning repositories via MCP:
- Create a token at https://github.com/settings/tokens
- Scopes needed: `repo` (for private repos) or `public_repo` (for public only)

## Step-by-Step Instructions

### Step 1: Clone and Install

```bash
git clone <your-repo-url>
cd agent-framework
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: Configure Environment Variables

Create a `.env` file in the root directory:

```bash
# Azure OpenAI via APIM
AZURE_OPENAI_ENDPOINT=https://your-apim-instance.azure-api.net/openai/
AZURE_OPENAI_API_KEY=your-apim-subscription-key
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o
API_VERSION=2025-01-01-preview

# Azure AI Agent Service (Service Principal)
AZURE_AI_PROJECT_ENDPOINT=your-project-endpoint
AZURE_CLIENT_ID=your-sp-client-id
AZURE_CLIENT_SECRET=your-sp-secret
AZURE_TENANT_ID=your-tenant-id

# GitHub Access
GITHUB_TOKEN=ghp_your_token_here
```

### Step 3: Verify Setup

Test your environment by running Challenge 01:

```bash
cd workshop/challenge-1
python challenge_01_repo_access.py
```

If it runs successfully:
- ✅ Azure OpenAI connection works
- ✅ MCP server can access GitHub
- ✅ Target repository is accessible

## Conclusion

By reaching this point, you have all services configured and dependencies installed. In the next challenges, you'll start building security scanning agents using the Microsoft Agent Framework.

Now the real fun begins!
