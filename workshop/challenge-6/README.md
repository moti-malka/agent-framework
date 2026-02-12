# Challenge 6: Code Vulnerability Scanner 🐛

**Duration:** 20 minutes

Secrets are just one category. Applications also have **code-level vulnerabilities**: SQL injection, command injection, XSS, SSRF, insecure deserialization, path traversal, and more. In this challenge, you'll build a dedicated scanner for these patterns.

## Learning Objectives

- Build a domain-specific agent for code vulnerability detection
- Craft instructions that guide the agent to recognize injection flaws and unsafe patterns
- Produce structured output while reporting findings to shared memory

## Vulnerability Categories

| Category | Patterns to Detect |
|----------|--------------------|
| **SQL Injection** | String concatenation in queries, unsanitized user input |
| **Command Injection** | `os.system()`, `subprocess` with `shell=True` |
| **XSS** | Unescaped user input in HTML responses |
| **SSRF** | User-controlled URLs in server-side requests |
| **Insecure Deserialization** | `pickle.loads()`, `yaml.load()` without `SafeLoader` |
| **Path Traversal** | Unsanitized file paths from user input |
| **XXE** | XML parsing without entity restrictions |
| **Eval/Exec** | `eval()` or `exec()` with user-controlled input |

## Step-by-Step Instructions

### What You Need to Build

A `code_vuln_scanner` agent that:
- Reads Python source files from the repository
- Identifies code-level security vulnerabilities
- Calls `report_vulnerability()` for EACH finding
- Calls `mark_file_scanned()` after analyzing each file
- Uses `response_format=VulnerabilityList` and `context_provider=scan_memory`

### Exports

| Variable | Type | Description |
|----------|------|-------------|
| `code_vuln_scanner` | `ChatAgent` | Agent that detects code vulnerabilities |

## Testing

```bash
cd workshop/challenge-6
python challenge_06_code_scanner.py
```

**Expected output**: The scanner finds injection flaws, unsafe function usage, and other code-level issues.

## Resources

- **Challenge file**: [`challenge_06_code_scanner.py`](./challenge_06_code_scanner.py)
- **Security guide**: [`SECURITY_GUIDE.md`](../SECURITY_GUIDE.md)
- **OWASP Top 10**: [owasp.org/www-project-top-ten](https://owasp.org/www-project-top-ten/)
