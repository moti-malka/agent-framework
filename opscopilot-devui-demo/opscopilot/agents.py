"""
Agent definitions for OpsCopilot demo.
"""
import os
from dotenv import load_dotenv

from agent_framework import Agent
from agent_framework.chat_completion import (
    AzureOpenAIChatClient,
    OpenAIChatClient,
)

from .models import TriageResult, FinalPlan
from .tools import (
    fetch_service_health,
    lookup_runbook,
    search_known_issues,
    restart_service,
    open_sev1_bridge,
)
from .middleware import LoggingAgentMiddleware, LoggingFunctionMiddleware
from .memory import get_ops_memory

# Load environment variables
load_dotenv()


def create_chat_client():
    """
    Create a chat client based on environment configuration.
    Uses Azure OpenAI if configured, otherwise falls back to OpenAI.
    """
    # Check for Azure OpenAI configuration
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    azure_key = os.getenv("AZURE_OPENAI_API_KEY")
    azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")
    
    if azure_endpoint and azure_key:
        print("🔵 Using Azure OpenAI")
        return AzureOpenAIChatClient(
            endpoint=azure_endpoint,
            api_key=azure_key,
            deployment=azure_deployment,
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
        )
    
    # Fall back to OpenAI
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key:
        print("🟢 Using OpenAI")
        return OpenAIChatClient(
            api_key=openai_key,
            model=os.getenv("OPENAI_MODEL", "gpt-4o"),
        )
    
    raise ValueError(
        "No AI configuration found. Set either:\n"
        "  - AZURE_OPENAI_ENDPOINT + AZURE_OPENAI_API_KEY, or\n"
        "  - OPENAI_API_KEY"
    )


# Shared chat client (created lazily)
_chat_client = None


def get_chat_client():
    """Get or create the shared chat client."""
    global _chat_client
    if _chat_client is None:
        _chat_client = create_chat_client()
    return _chat_client


def build_classifier_agent() -> Agent:
    """
    Build the classifier agent that triages incidents.
    Determines category, severity, and whether approval is needed.
    """
    return Agent(
        id="opscopilot_classifier",
        name="Classifier Agent",
        description="Triages incidents by category, severity, and determines required actions",
        chat_client=get_chat_client(),
        instructions="""You are an expert incident classifier for cloud operations.

Your job is to analyze an incident and determine:
1. **Category**: Is this an Incident, Question, Change request, or Security issue?
2. **Severity**: Sev1 (critical), Sev2 (high), or Sev3 (low)
3. **Confidence**: How confident are you in this classification (0.0 to 1.0)
4. **Next Action**: What should be done next
5. **Needs Approval**: Does this require human approval for a dangerous action?
6. **Approval Action**: If approval needed, specify: "restart_service" or "open_sev1_bridge"

Classification guidelines:
- Sev1: Customer-facing outage, data loss risk, security breach
- Sev2: Degraded performance, partial outage, potential escalation
- Sev3: Minor issues, questions, planned changes

Set needs_approval=true if:
- The recommended action involves restarting a production service
- A Sev1 bridge call should be opened
- Any action that could cause customer impact

Always output valid JSON matching the TriageResult schema.""",
        response_format=TriageResult,
        middleware=[LoggingAgentMiddleware(), LoggingFunctionMiddleware()],
        context_providers=[get_ops_memory()],
    )


def build_writer_agent() -> Agent:
    """
    Build the writer agent that creates the final incident plan.
    """
    return Agent(
        id="opscopilot_writer",
        name="Writer Agent",
        description="Creates final incident response plans with customer communication",
        chat_client=get_chat_client(),
        instructions="""You are an expert technical writer for cloud operations.

Your job is to create a comprehensive incident response plan that includes:
1. **Summary**: A brief 1-2 sentence summary of the situation
2. **Steps**: 3-6 actionable steps to resolve or investigate the issue
3. **Customer Message**: A professional message to send to the customer (can be in Hebrew if context indicates)
4. **Internal Note**: Technical notes for the ops team

Guidelines:
- Be concise but thorough
- Steps should be actionable and specific
- Customer message should be empathetic and informative
- Internal notes can include technical details and caveats

Use the available tools to gather enrichment data:
- fetch_service_health: Get current service status
- lookup_runbook: Find relevant runbook procedures
- search_known_issues: Check for known issues

Always output valid JSON matching the FinalPlan schema.""",
        response_format=FinalPlan,
        tools=[fetch_service_health, lookup_runbook, search_known_issues],
        middleware=[LoggingAgentMiddleware(), LoggingFunctionMiddleware()],
        context_providers=[get_ops_memory()],
    )


def build_qa_agent() -> Agent:
    """
    Build the QA agent that reviews plans for safety and consistency.
    """
    return Agent(
        id="opscopilot_qa",
        name="QA Agent",
        description="Reviews incident plans for safety, consistency, and completeness",
        chat_client=get_chat_client(),
        instructions="""You are a quality assurance reviewer for incident response plans.

Your job is to review a proposed incident plan and:
1. Verify the plan is safe and won't cause additional issues
2. Check for consistency between the summary, steps, and messages
3. Ensure customer communication is appropriate
4. Suggest 1-2 improvements if needed

Output your review as plain text with:
- ✅ APPROVED or ⚠️ NEEDS REVISION
- Brief explanation
- Suggested improvements (if any)

Be constructive but thorough. Safety is the top priority.""",
        middleware=[LoggingAgentMiddleware(), LoggingFunctionMiddleware()],
        context_providers=[get_ops_memory()],
    )


def build_agents() -> dict[str, Agent]:
    """
    Build all agents and return them in a dictionary.
    """
    return {
        "classifier": build_classifier_agent(),
        "writer": build_writer_agent(),
        "qa": build_qa_agent(),
    }


# Convenience exports
__all__ = [
    "build_classifier_agent",
    "build_writer_agent", 
    "build_qa_agent",
    "build_agents",
    "get_chat_client",
]
