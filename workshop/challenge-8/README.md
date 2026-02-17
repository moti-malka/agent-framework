# Challenge 8: Authentication & Cryptography Scanner 🔐

**Duration:** 20 minutes

Authentication weaknesses and cryptographic flaws are critical security issues. This scanner specializes in detecting weak password handling, JWT vulnerabilities, deprecated cryptography, and authentication bypass patterns.

## Learning Objectives

- Build a specialized agent for authentication and cryptography analysis
- Detect weak hashing, insecure JWT patterns, and deprecated crypto algorithms
- Understand the difference between code-level and auth/crypto vulnerabilities

## Vulnerability Categories

| Category | Patterns to Detect |
|----------|--------------------|
| **Weak Password Handling** | MD5/SHA1 without salt, timing-vulnerable comparisons (`==` instead of `hmac.compare_digest`) |
| **JWT Issues** | `none` algorithm allowed, excessively long expiry, weak signing secrets |
| **Deprecated Crypto** | DES encryption, ECB mode, hardcoded IV reuse, SHA1 for sensitive data |
| **Auth Bypass** | Predictable random seeds, no auth on admin endpoints, missing CSRF |

## Step-by-Step Instructions

### What You Need to Build

An `auth_crypto_scanner` agent that:
- Focuses on `auth.py`, `utils/crypto.py`, and related authentication/crypto files
- Identifies weak hashing, insecure JWT usage, deprecated cryptography
- Calls `report_vulnerability()` for EACH finding
- Calls `mark_file_scanned()` after analyzing each file
- Uses `response_format=VulnerabilityList` and `context_providers=[scan_memory]`

> **Note**: Each vulnerability is self-contained within its file. No cross-file correlation is needed.

### Exports

| Variable | Type | Description |
|----------|------|-------------|
| `auth_crypto_scanner` | `Agent` | Agent that detects auth & crypto issues |

## Testing

```bash
cd workshop/challenge-8
python challenge_08_auth_crypto_scanner.py
```

**Expected output**: The scanner finds weak hashing, JWT issues, and deprecated crypto patterns.

## Resources

- **Challenge file**: [`challenge_08_auth_crypto_scanner.py`](./challenge_08_auth_crypto_scanner.py)
- **Security guide**: [`SECURITY_GUIDE.md`](../SECURITY_GUIDE.md)
