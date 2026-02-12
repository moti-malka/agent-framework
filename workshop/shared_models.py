"""
Shared Models & Utilities for All Challenges
=============================================
Every challenge imports from here. This defines the Pydantic models
used for structured output so that all teams produce comparable results.

The target application lives in a GitHub repository and is accessed
via MCP (Model Context Protocol) — NOT by reading local files.
"""

from pydantic import BaseModel, Field
from typing import List


# ─── Agent Client Factory ─────────────────────────────────────────────
def create_mcp_client():
    """Create an AzureAIAgentClient using DefaultAzureCredential.

    Auth is resolved automatically in this order:
      1. Service-principal env vars (AZURE_CLIENT_ID, AZURE_TENANT_ID,
         AZURE_CLIENT_SECRET)  – best for CI / shared workshops
      2. Managed Identity            – on Azure compute
      3. Azure CLI (``az login``)     – local dev fallback
    """
    import os
    from azure.identity.aio import DefaultAzureCredential
    from agent_framework_azure_ai import AzureAIAgentClient

    return AzureAIAgentClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        credential=DefaultAzureCredential(),
    )


# ─── Chat Client Factory ──────────────────────────────────────────────
def create_chat_client():
    """Create an AzureOpenAIChatClient routed through APIM.

    The client uses the APIM gateway endpoint with a subscription key.
    ``base_url`` is set to bypass the SDK's automatic ``/openai`` prefix,
    since APIM's inbound policy already adds ``/openai`` to the backend URL.
    """
    import os
    from agent_framework.azure import AzureOpenAIChatClient

    return AzureOpenAIChatClient(
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/deployments/{os.environ['AZURE_OPENAI_CHAT_DEPLOYMENT_NAME']}",
        api_version=os.environ.get("API_VERSION", "2025-01-01-preview"),
    )


# ─── GitHub Repository ────────────────────────────────────────────────
# The vulnerable application is hosted here. Agents access it via GitHub MCP.
GITHUB_REPO_OWNER = "galshohat"
GITHUB_REPO_NAME = "vulnerable-app"
GITHUB_REPO = f"{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}"


# ─── Pydantic Models ─────────────────────────────────────────────────
class Vulnerability(BaseModel):
    """A single detected vulnerability.

    Vulnerabilities can span multiple lines (e.g. an entire function).
    Use start_line and end_line to mark the full range.
    If the vulnerability is a single line, set start_line == end_line.
    """
    file: str = Field(description="Relative path within the repository")
    start_line: int = Field(description="Starting line number where the vulnerability begins")
    end_line: int = Field(description="Ending line number where the vulnerability ends (same as start_line for single-line issues)")
    description: str = Field(description="Short description of the vulnerability")


class VulnerabilityList(BaseModel):
    """Structured list of vulnerabilities.

    Every vulnerability MUST include 'file' (relative path),
    'start_line' (integer), 'end_line' (integer), and 'description' (string).
    A vulnerability can span multiple lines — use start_line and end_line to
    mark the full extent. For single-line issues, set start_line == end_line.
    Scoring matches by file name + line range overlap.
    """
    vulnerabilities: List[Vulnerability] = Field(default_factory=list)
