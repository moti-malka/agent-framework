"""
Pydantic models for OpsCopilot demo.
"""
from typing import Literal, Optional
from pydantic import BaseModel, Field


class Incident(BaseModel):
    """Incoming incident to triage."""
    id: str
    title: str
    description: str
    service: str
    customer: str
    severity_hint: Optional[str] = None


class TriageResult(BaseModel):
    """Output from classifier agent."""
    category: Literal["Incident", "Question", "Change", "Security"]
    severity: Literal["Sev1", "Sev2", "Sev3"]
    confidence: float = Field(ge=0.0, le=1.0)
    next_action: str
    needs_approval: bool = False
    approval_action: Optional[Literal["restart_service", "open_sev1_bridge"]] = None


class Enrichment(BaseModel):
    """Enrichment data from mock tools."""
    service_health: str
    runbook_snippet: str
    known_issue: str


class FinalPlan(BaseModel):
    """Final plan from writer agent."""
    summary: str
    steps: list[str]
    customer_message: str
    internal_note: str
