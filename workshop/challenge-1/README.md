# Challenge 1: MCP Repository Access 🔌

**Duration:** 15 minutes

In this challenge, you'll establish the foundational connection to a GitHub repository using the **Model Context Protocol (MCP)**. This is the first building block — all subsequent scanning agents rely on this connection to browse and read repository files.

## Learning Objectives

- Understand how MCP tools connect agents to external services
- Create an MCP tool via `client.get_mcp_tool()` for GitHub integration
- Build a `repo_explorer` agent that can navigate repository structures

## Architecture

The connection follows this pattern:

```
Agent → McpTool (via client.get_mcp_tool()) → GitHub MCP Server → Repository
```

## About Model Context Protocol (MCP)

MCP is an open standard for connecting AI agents to external data sources and tools. In this challenge, you'll use GitHub's MCP endpoint to give your agent read access to repository files without needing to clone the repo locally.

Key concepts:
- **McpTool** (via `client.get_mcp_tool()`): A tool obtained from an MCP-capable client that connects to an MCP server
- **Approval mode**: Controls whether tool calls need user confirmation
- **Chat client**: The AI model client (e.g. `AzureAIAgentClient`) used by MCP for processing

## Step-by-Step Instructions

### What You Need to Build

1. **`github_mcp_tool`** — An MCP tool obtained via `client.get_mcp_tool()` configured to connect to GitHub's MCP endpoint
2. **`repo_explorer`** — An `Agent` that uses the MCP tool to browse repository contents

### Think About

- What URL does GitHub's MCP server live at?
- What approval mode makes sense for read-only operations?
- What instructions would make the explorer effective at navigating an unfamiliar codebase?

### Exports

| Variable | Type | Description |
|----------|------|-------------|
| `github_mcp_tool` | `McpTool` | Configured MCP tool for GitHub (via `client.get_mcp_tool()`) |
| `repo_explorer` | `Agent` | Agent that explores repository structure |

## Testing

```bash
cd workshop/challenge-1
python challenge_01_repo_access.py
```

**Expected output**: The agent lists all files and directories in the target repository.

## Resources

- **Challenge file**: [`challenge_01_repo_access.py`](./challenge_01_repo_access.py)
- **MCP Specification**: [modelcontextprotocol.io](https://modelcontextprotocol.io/)
- **Agent Framework Docs**: [aka.ms/agent-framework](https://aka.ms/agent-framework)
