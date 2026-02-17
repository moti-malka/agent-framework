# Challenge 7: Infrastructure & Dependency Scanner 🏗️

**Duration:** 20 minutes

Vulnerabilities aren't only in application code. They hide in third-party dependencies with known CVEs, Dockerfiles with insecure configurations, CI/CD pipelines missing security checks, and Terraform/IaC files with overly permissive policies.

## Learning Objectives

- Scan infrastructure-as-code and configuration files for security issues
- Detect dependency vulnerabilities in `requirements.txt`
- Identify Docker, CI/CD, and Terraform misconfigurations

## Vulnerability Categories

| Category | Files to Check | Patterns |
|----------|---------------|----------|
| **Dependency CVEs** | `requirements.txt` | Outdated packages with known vulnerabilities |
| **Docker** | `Dockerfile`, `docker-compose.yml` | Running as root, no health checks, exposed ports |
| **CI/CD** | `.github/workflows/` | Secrets in workflows, missing security scanning |
| **Terraform/IaC** | `*.tf`, `deploy/` | Public S3 buckets, overly permissive IAM |
| **App Config** | Various | Debug mode enabled, permissive CORS, verbose errors |

## Step-by-Step Instructions

### What You Need to Build

An `infra_scanner` agent that:
- Scans dependency files, Dockerfiles, CI/CD configs, and IaC files
- Identifies misconfigurations and known vulnerability patterns
- Calls `report_vulnerability()` for EACH finding
- Calls `mark_file_scanned()` after analyzing each file
- Uses `response_format=VulnerabilityList` and `context_providers=[scan_memory]`

### Think About

- Which files should this agent prioritize?
- Should it try to identify specific CVE IDs for dependency issues?
- Don't forget subdirectories like `deploy/`, `.github/workflows/`

### Exports

| Variable | Type | Description |
|----------|------|-------------|
| `infra_scanner` | `Agent` | Agent that scans dependencies, Docker, CI/CD, and IaC |

## Testing

```bash
cd workshop/challenge-7
python challenge_07_infra_scanner.py
```

**Expected output**: The scanner finds dependency vulnerabilities, Docker misconfigurations, and IaC issues.

## Resources

- **Challenge file**: [`challenge_07_infra_scanner.py`](./challenge_07_infra_scanner.py)
- **Security guide**: [`SECURITY_GUIDE.md`](../SECURITY_GUIDE.md)
