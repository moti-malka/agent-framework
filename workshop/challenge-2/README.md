# Challenge 2: File Reading Tools 📄

**Duration:** 15 minutes

MCP gives you raw access to the repo, but your scanning agents need **reusable tools** that read files and list directory contents programmatically. In this challenge, you'll build utility functions that wrap MCP into clean, callable tools.

## Learning Objectives

- Create `@tool`-decorated functions for the Agent Framework
- Build reusable file reading and listing utilities
- Understand how agents compose tools from previous challenges

## Architecture

```
Scanner Agent
  ├── list_repo_files()  → returns file listing
  └── read_repo_file()   → returns file contents
        └── Uses: github_mcp_tool (from Challenge 1)
```

## Step-by-Step Instructions

### What You Need to Build

1. **`list_repo_files`** — A `@tool` function that returns a list of all files in the repository
2. **`read_repo_file`** — A `@tool` function that reads a single file's contents given its relative path

### Think About

- How can an agent with MCP discover the full repository tree?
- What format should the output be for downstream agents to consume?
- What should the tool return if a file doesn't exist?
- Should the tool include the file path in its output for context?

### Exports

| Variable | Type | Description |
|----------|------|-------------|
| `list_repo_files` | `@tool` function | Lists all files in the repository |
| `read_repo_file` | `@tool` function | Reads a single file's contents |

## Testing

```bash
cd workshop/challenge-2
python challenge_02_file_tools.py
```

**Expected output**: The tool lists files and reads `app.py` content successfully.

## Resources

- **Challenge file**: [`challenge_02_file_tools.py`](./challenge_02_file_tools.py)
- **Agent Framework Tools**: [aka.ms/agent-framework](https://aka.ms/agent-framework)
