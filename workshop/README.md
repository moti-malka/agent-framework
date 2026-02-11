# Agent Framework Security Workshop

A hands-on workshop teaching you to build AI-powered security scanning agents using the Microsoft Agent Framework. You'll create specialized scanner agents and orchestrate them into a complete vulnerability detection workflow.

## 🎯 What You'll Build

By the end of this workshop, you'll have:
- **4 specialized security scanner agents** (secrets, code vulnerabilities, infrastructure, auth/crypto)
- **Repository access tools** using Model Context Protocol (MCP)
- **Shared memory system** for vulnerability tracking across agents
- **Structured output** with Pydantic models for consistent findings
- **Agent middleware** for logging and observability
- **Orchestrated workflow** coordinating all scanners to produce comprehensive security reports

## 📋 Prerequisites

### Required Software
- **Python 3.10+** with pip
- **VS Code** or your preferred IDE
- **Git** for cloning the repository

### Required Azure Services

#### 1. Azure OpenAI via API Management (APIM)
You'll need an Azure OpenAI instance **accessible through API Management** with:
- **Model**: `gpt-4o` or `gpt-4o-mini` deployed
- **APIM Gateway URL**: Your API Management gateway endpoint
- **API Key**: Your APIM subscription key

**Environment variables needed:**
```bash
AZURE_OPENAI_ENDPOINT=https://your-apim-instance.azure-api.net/openai/
AZURE_OPENAI_API_KEY=your-apim-subscription-key
AZURE_OPENAI_DEPLOYMENT=gpt-4o  # or your model deployment name
AZURE_OPENAI_API_VERSION=2024-07-01-preview
```

#### 2. Azure AI Agent Service (via Service Principal)
You'll need a Service Principal with access to Azure AI Agent Service:
- **Project Connection String**: From Azure AI Foundry portal
- **Client Credentials**: Service principal with appropriate permissions

**Environment variables needed:**
```bash
PROJECT_CONNECTION_STRING=your-project-connection-string
AZURE_CLIENT_ID=your-service-principal-client-id
AZURE_CLIENT_SECRET=your-service-principal-secret
AZURE_TENANT_ID=your-azure-tenant-id
```

#### 3. GitHub Personal Access Token
Required for scanning repositories via MCP:
- Create a token at https://github.com/settings/tokens
- Scopes needed: `repo` (for private repos) or `public_repo` (for public only)

**Environment variable needed:**
```bash
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token_here
```

### Target Repository
The workshop scans a vulnerable demo application. Set:
```bash
GITHUB_REPO=workshop/vulnerable_app
```

## 🚀 Getting Started

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd agent-framework
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file in the root directory with all required variables:

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
GITHUB_REPO=workshop/vulnerable_app
```

### 3. Verify Setup

Run the verification script to check your environment:

```bash
python _verify.py
```

This ensures:
- All required environment variables are set
- Azure OpenAI connection works
- Azure AI Agent Service connection works
- MCP server can access GitHub
- Target repository is accessible

## 📚 Workshop Challenges

The workshop consists of 10 progressive challenges, each building on the previous ones:

| # | Challenge | What You'll Learn | Key Concepts |
|---|-----------|-------------------|--------------|
| 01 | **MCP Repo Access** | Connect to GitHub via Model Context Protocol | MCP tools, repository navigation |
| 02 | **File Reading Tools** | Create reusable functions for reading files | Tool encapsulation, error handling |
| 03 | **Shared Memory** | Build context provider for vulnerability tracking | Memory persistence, context sharing |
| 04 | **Secrets Scanner** | Detect hardcoded secrets and credentials | Pattern matching, agent instructions |
| 05 | **Structured Output** | Use Pydantic models for consistent findings | Structured data, type safety |
| 06 | **Code Vulnerability Scanner** | Find injection, XSS, SSRF patterns | Security patterns, code analysis |
| 07 | **Infrastructure Scanner** | Scan Docker, Terraform, CI/CD configs | Infrastructure as code security |
| 08 | **Auth & Crypto Scanner** | Detect auth and cryptography vulnerabilities | Authentication, encryption best practices |
| 09 | **Agent Middleware** | Add logging and observability | Middleware chains, debugging |
| 10 | **Orchestrated Workflow** | Coordinate all scanners into complete workflow | Workflow builders, agent orchestration |

Each challenge directory (`workshop/challenges/challenge_0X_*.py`) contains:
- **Instructions** in the docstring
- **TODO sections** marking where you need to implement code
- **Test function** to validate your solution
- **Export requirements** for variables and functions

Start with Challenge 01 and work through them sequentially.

## 🧪 Testing Your Solutions

### Individual Challenge Testing

Test a single challenge using the test runner:

```bash
python workshop/run_tests.py --only 1   # Test challenge 01
python workshop/run_tests.py --only 5   # Test challenge 05
python workshop/run_tests.py --only 10  # Test final workflow
```

### Understanding Test Output

Each test shows:
- **Agent activation logs** — which agents were called
- **Tool invocation logs** — what functions were executed  
- **Vulnerability counts** — findings stored in memory
- **Timing information** — how long the scan took
- **Pass/Fail status** — whether assertions passed

Example test output:
```
🛡️  CHALLENGE TEST RUNNER
===========================================================
Solution 04 — Secrets Scanner
===========================================================
   🔑 [SecretsScanner] activated
  📞 Calling: list_repo_files()
  📤 Result: .env, app.py, auth.py...
🧠 Vulnerabilities in memory: 11
📂 Files covered: 5
✅ Test passed in 22.8s
```

### Final Workflow Scoring

Challenge 10 generates a JSON output file that you can score:

```bash
# Run the final workflow
python workshop/run_tests.py --only 10

# Score your results
python workshop/score_workflow.py workshop/challenge_10_output.json
```

**Scoring output:**
```
📊 Workflow Scoring Results
Total vulnerabilities found: 45
Catalog vulnerabilities: 95
Matched: 35 ✅
Missed: 60 ❌
Score: 36.8% (Bronze 🥉)
```

## 🏆 Achievement Tiers

Your score is based on how many catalog vulnerabilities you detected:

| Tier | Percentage | Badge | Description |
|------|------------|-------|-------------|
| **Diamond** | 90%+ | 💎 | Security expert! Near-perfect detection |
| **Gold** | 75-89% | 🥇 | Excellent! Found most vulnerabilities |
| **Silver** | 50-74% | 🥈 | Good job! Covered major security issues |
| **Bronze** | 25-49% | 🥉 | Nice start! Keep scanning more files |
| **- ** | <25% | - | Needs work — ensure all scanners activate |

### Scoring Algorithm

Matches use **file name + line range overlap** with ±10 line tolerance:
- Your finding: `app.py:45-48 "SQL injection"`
- Catalog entry: `app.py:42-50 "SQL Injection vulnerability"`
- **Result**: ✅ Match (overlapping range, same file)

**Tips for higher scores:**
1. **Scan ALL files** — don't skip subdirectories (deploy/, utils/, api/, .github/)
2. **Use ALL 4 scanners** — each covers different vulnerability types
3. **Report line ranges accurately** — include context, not just single lines
4. **Follow scanner instructions** — ensure each scanner calls `report_vulnerability()` and `mark_file_scanned()`
5. **Iterate on coverage** — if score is low, check which files weren't scanned

## 📖 Expected Output Format

Your Challenge 10 workflow should produce JSON matching this structure:

```json
{
  "workshop_id": "agent-framework-security-scan",
  "timestamp": "2025-01-09T12:00:00Z",
  "repository": "workshop/vulnerable_app",
  "scan_summary": {
    "total_vulnerabilities": 45,
    "files_scanned": 15,
    "scanners_used": ["SecretsScanner", "CodeVulnScanner", "InfraScanner", "AuthCryptoScanner"],
    "scan_duration_seconds": 87.3
  },
  "vulnerabilities": [
    {
      "file": "app.py",
      "start_line": 45,
      "end_line": 48,
      "description": "SQL injection vulnerability in database query"
    }
  ],
  "files_covered": ["app.py", "auth.py", "database.py", ...],
  "scanner_breakdown": {
    "SecretsScanner": {"findings": 11, "files": ["app.py", ".env", ...]},
    "CodeVulnScanner": {"findings": 15, "files": ["app.py", "api/endpoints.py", ...]},
    ...
  }
}
```

See [workshop/expected_workflow_output.json](workshop/expected_workflow_output.json) for a complete template.

## 🛠️ Key Concepts

### Agent Framework Components

1. **ChatAgent** — Individual AI agents with specific roles
   ```python
   agent = ChatAgent(
       chat_client=create_chat_client(),
       name="SecretsScanner",
       description="Finds hardcoded secrets",
       instructions="Your behavioral instructions...",
       tools=[read_file, report_vulnerability]
   )
   ```

2. **MCP Tools** — Model Context Protocol for external integrations
   ```python
   github_tool = McpHub.create_client_tool("github")
   ```

3. **Workflow Builders** — Orchestration patterns
   - **MagenticBuilder**: Manager delegates to specialist agents
   - **GroupChatBuilder**: Agents collaborate in shared conversation
   - **HandoffBuilder**: Agents pass control in sequence
   - **ConcurrentBuilder**: All agents run in parallel

4. **Context Providers** — Shared state across agents
   ```python
   @context_provider(name="scan_memory")
   def get_scan_context() -> str:
       return json.dumps(scan_memory.vulnerabilities)
   ```

5. **Middleware** — Cross-cutting concerns (logging, timing)
   ```python
   agent.middleware = [logging_middleware, timing_middleware]
   ```

### Security Scanning Patterns

Each scanner follows a consistent pattern:
1. **List files** in the repository
2. **Read file contents** using read tools
3. **Analyze** for specific vulnerability patterns
4. **Report findings** via `report_vulnerability(file, start_line, end_line, description)`
5. **Mark completion** via `mark_file_scanned(file_path)`

## 🤔 Troubleshooting

### Common Issues

**"Agent didn't activate any scanners"**
- Check that your workflow participants include all 4 scanners
- Verify the manager's instructions tell it to activate ALL agents
- Ensure task prompt is clear about using all scanners

**"Low score despite many findings"**
- Check if findings have correct line numbers (not just line 1)
- Ensure you're scanning subdirectories (deploy/, utils/, api/)
- Verify file paths match exactly (e.g., `app.py` not `./app.py`)

**"MCP connection failed"**
- Verify `GITHUB_PERSONAL_ACCESS_TOKEN` is set correctly
- Check token has `repo` or `public_repo` scope
- Ensure target repository path is correct

**"Azure OpenAI authentication failed"**
- Confirm you're using the **APIM endpoint**, not direct Azure OpenAI endpoint
- Verify `AZURE_OPENAI_ENDPOINT` ends with `/openai/`
- Check that `AZURE_OPENAI_API_KEY` is your APIM subscription key

**"Project connection string invalid"**
- Ensure Service Principal has access to Azure AI Agent Service
- Verify all 4 credential environment variables are set
- Check connection string format from Azure AI Foundry portal

### Debugging Tips

1. **Run with verbose logging**
   ```python
   logging.basicConfig(level=logging.DEBUG)
   ```

2. **Check memory state**
   ```python
   print(f"Vulnerabilities: {len(scan_memory.vulnerabilities)}")
   print(f"Files covered: {scan_memory.files_covered}")
   ```

3. **Test tools individually**
   ```python
   files = list_repo_files()  # Should return list of files
   content = read_repo_file("app.py")  # Should return file content
   ```

4. **Verify scanner activation**
   - Look for emoji indicators in test output (🔑 🐛 🏗️ 🔐)
   - Check that each scanner calls its tools
   - Ensure manager doesn't stall (max_stall_count)

## 📚 Additional Resources

- **Agent Framework Docs**: [Microsoft Agent Framework Documentation](https://aka.ms/agent-framework)
- **MCP Specification**: [Model Context Protocol](https://modelcontextprotocol.io/)
- **Azure AI Foundry**: [Azure AI Studio](https://ai.azure.com/)
- **OWASP Top 10**: [Web Application Security Risks](https://owasp.org/www-project-top-ten/)

## 🎓 Learning Outcomes

After completing this workshop, you'll understand:

✅ How to build AI agents with specific roles and responsibilities  
✅ How to use Model Context Protocol for external integrations  
✅ How to share state between agents using context providers  
✅ How to structure agent outputs with Pydantic models  
✅ How to add observability with middleware  
✅ How to orchestrate multiple agents into workflows  
✅ How to apply AI agents to practical problems like security scanning  

## 🤝 Contributing

Found an issue or have a suggestion for improving the workshop? Contributions welcome!

## 📄 License

This workshop is provided for educational purposes.

---

**Ready to start?** Jump to [Challenge 01](workshop/challenges/challenge_01_repo_access.py) and begin building your security scanning agents!
