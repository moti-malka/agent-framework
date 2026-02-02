"""
OpsCopilot Workflow for DevUI demo.
Demonstrates routing, fan-out/fan-in, and human-in-the-loop approval.
"""
import json
from typing import AsyncIterator

from agent_framework import (
    Workflow,
    WorkflowBuilder,
    AgentExecutor,
    Executor,
    ExecutorContext,
)

from .models import Incident, TriageResult, Enrichment, FinalPlan
from .tools import (
    fetch_service_health,
    lookup_runbook,
    search_known_issues,
    restart_service,
    open_sev1_bridge,
)
from .agents import build_agents


# ============================================================================
# Executor Functions
# ============================================================================

async def to_classifier_request(incident: Incident, context: ExecutorContext) -> str:
    """Convert incident to a prompt for the classifier agent."""
    return f"""Please triage the following incident:

ID: {incident.id}
Title: {incident.title}
Description: {incident.description}
Service: {incident.service}
Customer: {incident.customer}
Severity Hint: {incident.severity_hint or 'Not provided'}

Classify this incident and determine the appropriate response."""


async def parse_triage_result(response: str, context: ExecutorContext) -> TriageResult:
    """Parse the classifier response into a TriageResult."""
    # The agent should return JSON, but handle edge cases
    try:
        if isinstance(response, TriageResult):
            return response
        if isinstance(response, dict):
            return TriageResult(**response)
        # Try to extract JSON from the response
        data = json.loads(response)
        return TriageResult(**data)
    except (json.JSONDecodeError, TypeError) as e:
        # Fallback: create a default triage result
        print(f"⚠️ Failed to parse triage result: {e}")
        return TriageResult(
            category="Incident",
            severity="Sev2",
            confidence=0.5,
            next_action="Manual review required",
            needs_approval=False,
        )


async def enrich_incident(
    incident: Incident,
    triage: TriageResult,
    context: ExecutorContext,
) -> Enrichment:
    """
    Non-LLM executor that calls mock tools to gather enrichment data.
    """
    # Call the mock tools directly (they're just Python functions)
    service_health = fetch_service_health.func(incident.service)
    runbook = lookup_runbook.func(incident.service, triage.category)
    known_issues = search_known_issues.func(
        incident.service,
        incident.title.lower()
    )
    
    return Enrichment(
        service_health=service_health,
        runbook_snippet=runbook,
        known_issue=known_issues,
    )


async def execute_dangerous_action(
    triage: TriageResult,
    incident: Incident,
    context: ExecutorContext,
) -> str:
    """
    Execute dangerous actions that require approval.
    This will trigger the approval flow in DevUI.
    """
    if not triage.needs_approval:
        return "No dangerous action required."
    
    if triage.approval_action == "restart_service":
        # This will trigger approval due to @tool(approval_mode="always_require")
        result = await restart_service.async_func(incident.service)
        return f"🔄 Restart Action: {result}"
    
    elif triage.approval_action == "open_sev1_bridge":
        result = await open_sev1_bridge.async_func(incident.id, incident.customer)
        return f"📞 Bridge Action: {result}"
    
    return f"Unknown approval action: {triage.approval_action}"


async def to_writer_request(
    incident: Incident,
    triage: TriageResult,
    enrichment: Enrichment,
    danger_result: str | None,
    context: ExecutorContext,
) -> str:
    """Prepare the prompt for the writer agent."""
    return f"""Create an incident response plan based on the following:

## Incident
- ID: {incident.id}
- Title: {incident.title}
- Description: {incident.description}
- Service: {incident.service}
- Customer: {incident.customer}

## Triage Result
- Category: {triage.category}
- Severity: {triage.severity}
- Confidence: {triage.confidence}
- Recommended Action: {triage.next_action}

## Enrichment Data
Service Health: {enrichment.service_health}

Runbook:
{enrichment.runbook_snippet}

Known Issues: {enrichment.known_issue}

## Dangerous Action Result
{danger_result or 'N/A - No dangerous action was executed'}

Please create a comprehensive response plan."""


async def parse_final_plan(response: str, context: ExecutorContext) -> FinalPlan:
    """Parse the writer response into a FinalPlan."""
    try:
        if isinstance(response, FinalPlan):
            return response
        if isinstance(response, dict):
            return FinalPlan(**response)
        data = json.loads(response)
        return FinalPlan(**data)
    except (json.JSONDecodeError, TypeError) as e:
        print(f"⚠️ Failed to parse final plan: {e}")
        return FinalPlan(
            summary="Plan parsing failed - manual review required",
            steps=["Review incident manually", "Contact on-call engineer"],
            customer_message="We are investigating your issue and will update you shortly.",
            internal_note=f"Auto-plan failed: {e}",
        )


async def aggregate_results(
    incident: Incident,
    triage: TriageResult,
    enrichment: Enrichment,
    danger_result: str | None,
    plan: FinalPlan,
    context: ExecutorContext,
) -> str:
    """
    Final aggregator that combines all results into a human-readable output.
    """
    output_parts = [
        "=" * 60,
        "🎯 OPSCOPILOT INCIDENT RESPONSE",
        "=" * 60,
        "",
        f"📋 Incident: {incident.id} - {incident.title}",
        f"👤 Customer: {incident.customer}",
        f"🔧 Service: {incident.service}",
        "",
        "─" * 40,
        "📊 TRIAGE",
        "─" * 40,
        f"Category: {triage.category}",
        f"Severity: {triage.severity}",
        f"Confidence: {triage.confidence:.0%}",
        f"Next Action: {triage.next_action}",
        f"Approval Required: {'Yes' if triage.needs_approval else 'No'}",
        "",
        "─" * 40,
        "📝 PLAN",
        "─" * 40,
        f"Summary: {plan.summary}",
        "",
        "Steps:",
    ]
    
    for i, step in enumerate(plan.steps, 1):
        output_parts.append(f"  {i}. {step}")
    
    output_parts.extend([
        "",
        "─" * 40,
        "💬 CUSTOMER MESSAGE",
        "─" * 40,
        plan.customer_message,
        "",
        "─" * 40,
        "🔒 INTERNAL NOTE",
        "─" * 40,
        plan.internal_note,
    ])
    
    if danger_result and "No dangerous action" not in danger_result:
        output_parts.extend([
            "",
            "─" * 40,
            "⚠️ DANGEROUS ACTION EXECUTED",
            "─" * 40,
            danger_result,
        ])
    
    output_parts.extend([
        "",
        "=" * 60,
        "✅ END OF OPSCOPILOT RESPONSE",
        "=" * 60,
    ])
    
    return "\n".join(output_parts)


# ============================================================================
# Workflow Builder
# ============================================================================

def build_workflow(agents: dict | None = None) -> Workflow:
    """
    Build the OpsCopilot workflow.
    
    Flow:
    1. Incident input → Classifier Agent → TriageResult
    2. Fan-out:
       - Always: Enrichment (mock tools)
       - If needs_approval: Dangerous Action (with approval)
    3. Writer Agent → FinalPlan
    4. Aggregator → Final human-readable output
    """
    if agents is None:
        agents = build_agents()
    
    classifier = agents["classifier"]
    writer = agents["writer"]
    
    # Build the workflow
    builder = WorkflowBuilder(
        id="opscopilot_workflow",
        name="OpsCopilot Incident Triage",
        description="Automated incident triage with classification, enrichment, and response planning",
        input_type=Incident,
        output_type=str,
    )
    
    # Step 1: Convert incident to classifier request
    builder.add_executor(
        "prepare_classifier",
        Executor(to_classifier_request),
        input_edge="$input",
    )
    
    # Step 2: Run classifier agent
    builder.add_executor(
        "classifier",
        AgentExecutor(classifier),
        input_edge="prepare_classifier",
    )
    
    # Step 3: Parse triage result
    builder.add_executor(
        "parse_triage",
        Executor(parse_triage_result),
        input_edge="classifier",
    )
    
    # Step 4: Enrichment (always runs)
    builder.add_executor(
        "enrichment",
        Executor(enrich_incident),
        input_edges={"incident": "$input", "triage": "parse_triage"},
    )
    
    # Step 5: Dangerous action (conditionally based on needs_approval)
    builder.add_executor(
        "dangerous_action",
        Executor(execute_dangerous_action),
        input_edges={"triage": "parse_triage", "incident": "$input"},
        condition=lambda triage, **_: triage.needs_approval if hasattr(triage, 'needs_approval') else False,
    )
    
    # Step 6: Prepare writer request
    builder.add_executor(
        "prepare_writer",
        Executor(to_writer_request),
        input_edges={
            "incident": "$input",
            "triage": "parse_triage",
            "enrichment": "enrichment",
            "danger_result": "dangerous_action",
        },
    )
    
    # Step 7: Run writer agent
    builder.add_executor(
        "writer",
        AgentExecutor(writer),
        input_edge="prepare_writer",
    )
    
    # Step 8: Parse final plan
    builder.add_executor(
        "parse_plan",
        Executor(parse_final_plan),
        input_edge="writer",
    )
    
    # Step 9: Aggregate all results
    builder.add_executor(
        "aggregator",
        Executor(aggregate_results),
        input_edges={
            "incident": "$input",
            "triage": "parse_triage",
            "enrichment": "enrichment",
            "danger_result": "dangerous_action",
            "plan": "parse_plan",
        },
    )
    
    # Set output
    builder.set_output("aggregator")
    
    return builder.build()


# ============================================================================
# Convenience exports
# ============================================================================

__all__ = ["build_workflow"]
