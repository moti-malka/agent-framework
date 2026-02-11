# 🔍 Security Breach Guide

The target repository is a realistic web application with security vulnerabilities
planted across the full stack. Your agents should scan for issues in these areas:

1. **Secrets & Credentials** — leaked or hardcoded sensitive values
2. **Injection** — unsanitized user input reaching dangerous sinks
3. **Authentication & Cryptography** — weak or broken security implementations
4. **Dependencies** — third-party packages with known CVEs
5. **Infrastructure & CI/CD** — misconfigurations in deployment and pipeline files
6. **Unsafe Code Patterns** — dangerous language features used without safeguards

Your agents need to discover the specific issues on their own — that's the challenge.

---

## 🗂️ Project Structure Hints

The repository spans **multiple layers** of a web application. A good scanning
strategy considers what kind of vulnerability is likely in each layer:

| Layer | Files to look at | What to look for |
|-------|-----------------|------------------|
| **Configuration** | `config.py`, `.env` | Hardcoded API keys (AWS, Stripe, SendGrid, GitHub), SMTP creds, encryption keys, debug flags |
| **Application Core** | `app.py` | Secret keys, webhook URLs, API keys, injection sinks, XSS, SSRF, debug mode |
| **Auth & Sessions** | `auth.py` | JWT secrets, hardcoded admin/service passwords, weak hashing, JWT misconfig, timing attacks, plaintext logging |
| **Data Layer** | `database.py`, `payments.py` | DB credentials, connection strings, SQL injection, Stripe keys, card data logging |
| **Utilities** | `utils/crypto.py`, `utils/file_handler.py`, `utils/xml_parser.py` | Embedded RSA private key, DES/AES hardcoded keys, weak hashing, path traversal, XXE |
| **API** | `api/endpoints.py`, `api/middleware.py` | Partner API keys, SQL injection, open redirect, stack traces, request body logging |
| **Dependencies** | `requirements.txt` | Outdated packages with known CVEs |
| **Infrastructure** | `deploy/Dockerfile`, `deploy/docker-compose.yml`, `deploy/terraform/main.tf` | Running as root, exposed ports, secrets as env vars, privileged mode, public S3, open security groups |
| **CI/CD** | `.github/workflows/ci.yml` | `pull_request_target` trigger, unpinned actions, secrets echoed to logs, script injection |

> **Tip for agent design:** Don't build one agent that tries to do everything.
> Split the work by security domain — a secrets scanner, a code-level scanner,
> an infra scanner, etc. Each specialist can focus on the file types that matter
> most for its domain.
>
> **Secrets are self-contained:** Every secret can be found by reading a single
> file — no cross-file correlation is needed. Each file with secrets has them
> directly visible as string literals, variable assignments, or config values.
>
> Make sure your orchestration covers **all** files — vulnerabilities live
> in every corner of the repo, including subdirectories.
