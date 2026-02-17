# Challenge 4: Secrets Scanner Agent 🔑

**Duration:** 20 minutes

Hardcoded secrets are one of the most common and dangerous vulnerabilities. API keys, passwords, and tokens committed to source code can be exploited by anyone with access to the repository.

## Learning Objectives

- Build a specialized security scanning agent with domain-specific instructions
- Use tools and context providers together in an agent
- Detect hardcoded secrets, API keys, passwords, tokens, and credentials

## What Your Scanner Should Find

| Secret Type | Examples |
|-------------|----------|
| **API Keys** | AWS keys, Azure keys, third-party API tokens |
| **Database Credentials** | Connection strings, passwords in config |
| **Encryption Keys** | Hardcoded symmetric keys, key material in source |
| **Tokens** | JWT secrets, OAuth tokens, session secrets |
| **Environment Leaks** | `.env` files with real credentials committed |

## Step-by-Step Instructions

### What You Need to Build

A `secrets_scanner` agent that:
- Reads source code files from the repository
- Identifies hardcoded secrets and credentials
- Calls `report_vulnerability()` for EACH finding
- Calls `mark_file_scanned()` after analyzing each file
- Uses `context_providers=[scan_memory]` to avoid duplicate work

### Think About

- What tools does this agent need? (file tools + memory tools)
- What instructions would guide it to recognize different types of secrets?
- Which files are most likely to contain secrets?

> **Note**: Every secret is self-contained in its own file — no cross-file correlation is needed.

### Exports

| Variable | Type | Description |
|----------|------|-------------|
| `secrets_scanner` | `Agent` | Agent that detects hardcoded secrets |

## Testing

```bash
cd workshop/challenge-4
python challenge_04_secrets_scanner.py
```

**Expected output**: The scanner finds multiple hardcoded secrets across repository files.

## Resources

- **Challenge file**: [`challenge_04_secrets_scanner.py`](./challenge_04_secrets_scanner.py)
- **Security guide**: [`SECURITY_GUIDE.md`](../SECURITY_GUIDE.md)
