"""
Mock incident data for OpsCopilot demo.
"""
from .models import Incident


INCIDENTS: list[Incident] = [
    Incident(
        id="INC-001",
        title="AKS Node NotReady",
        description="Kubernetes node aks-nodepool1-12345 in cluster prod-west entered NotReady state. "
                    "Pods are being evicted. Customer: Contoso. Service: AKS-Prod-West.",
        service="AKS-Prod-West",
        customer="Contoso",
        severity_hint="High"
    ),
    Incident(
        id="INC-002",
        title="VM CPU at 95%",
        description="Virtual machine vm-sql-primary CPU utilization sustained at 95% for 30 minutes. "
                    "Database queries slowing down. Customer: Fabrikam. Service: VM-SQL-Primary.",
        service="VM-SQL-Primary",
        customer="Fabrikam",
        severity_hint="Medium"
    ),
    Incident(
        id="INC-003",
        title="API Gateway Latency Spike",
        description="API Gateway apim-prod-east showing p99 latency of 8 seconds (baseline: 200ms). "
                    "Multiple downstream services affected. Customer: Northwind. Service: APIM-Prod-East.",
        service="APIM-Prod-East",
        customer="Northwind",
        severity_hint="High"
    ),
    Incident(
        id="INC-004",
        title="Suspicious Login Activity",
        description="Multiple failed login attempts detected from IP 192.168.1.100 targeting admin accounts. "
                    "Possible brute force attack. Customer: AdventureWorks. Service: Identity-Prod.",
        service="Identity-Prod",
        customer="AdventureWorks",
        severity_hint="Critical"
    ),
    Incident(
        id="INC-005",
        title="Storage Account Throttling",
        description="Storage account stproddata01 hitting IOPS limits. Write operations failing intermittently. "
                    "Customer: WideWorldImporters. Service: Storage-Prod-Data.",
        service="Storage-Prod-Data",
        customer="WideWorldImporters",
        severity_hint="Medium"
    ),
    Incident(
        id="INC-006",
        title="SSL Certificate Expiring",
        description="SSL certificate for api.contoso.com expires in 3 days. Renewal process needs initiation. "
                    "Customer: Contoso. Service: Cert-Management.",
        service="Cert-Management",
        customer="Contoso",
        severity_hint="Low"
    ),
    Incident(
        id="INC-007",
        title="How to scale AKS cluster?",
        description="Customer asking how to scale their AKS cluster from 3 to 5 nodes. "
                    "This is a question, not an incident. Customer: Tailspin. Service: AKS-Dev.",
        service="AKS-Dev",
        customer="Tailspin",
        severity_hint=None
    ),
    Incident(
        id="INC-008",
        title="Redis Cache Out of Memory",
        description="Redis cache redis-prod-sessions showing 99% memory utilization. "
                    "Session data at risk of eviction. Customer: Fabrikam. Service: Redis-Prod.",
        service="Redis-Prod",
        customer="Fabrikam",
        severity_hint="High"
    ),
]


def get_incident_by_id(incident_id: str) -> Incident | None:
    """Retrieve an incident by its ID."""
    for incident in INCIDENTS:
        if incident.id == incident_id:
            return incident
    return None


def list_incident_ids() -> list[str]:
    """Return all available incident IDs."""
    return [inc.id for inc in INCIDENTS]
