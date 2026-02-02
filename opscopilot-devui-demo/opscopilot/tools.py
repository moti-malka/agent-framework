"""
Mock tools for OpsCopilot demo.
All tools return deterministic mock data - no external calls.
"""
from agent_framework import tool


@tool
def fetch_service_health(service: str) -> str:
    """
    Fetch current health status for a service.
    
    Args:
        service: The service name to check health for.
    
    Returns:
        A health status summary string.
    """
    # Mock health data based on service patterns
    health_map = {
        "AKS": "Status: Degraded. 1 of 3 nodes NotReady. Pods rescheduling in progress.",
        "VM-SQL": "Status: Warning. CPU high, memory OK. Last backup: 2h ago.",
        "APIM": "Status: Degraded. Latency elevated. Backend pool healthy.",
        "Identity": "Status: Healthy. Auth service responding. WAF active.",
        "Storage": "Status: Warning. IOPS at 95% limit. No data loss detected.",
        "Cert": "Status: Attention. Certificate expires in 3 days.",
        "Redis": "Status: Critical. Memory at 99%. Eviction policy active.",
    }
    
    for key, value in health_map.items():
        if key.lower() in service.lower():
            return value
    
    return f"Status: Unknown. No health data available for {service}."


@tool
def lookup_runbook(service: str, category: str) -> str:
    """
    Look up the relevant runbook for a service and incident category.
    
    Args:
        service: The affected service name.
        category: The incident category (Incident, Question, Change, Security).
    
    Returns:
        A runbook snippet with recommended steps.
    """
    runbooks = {
        ("AKS", "Incident"): """
            Runbook: AKS Node Recovery
            1. Check node status: kubectl get nodes
            2. Describe problematic node: kubectl describe node <name>
            3. Check for resource pressure (memory/disk)
            4. If unrecoverable, cordon and drain node
            5. Consider node restart or replacement
        """,
        ("VM", "Incident"): """
            Runbook: VM High CPU
            1. Check top processes via Azure Serial Console
            2. Review metrics in Azure Monitor
            3. Consider vertical scaling if sustained
            4. Check for runaway queries or processes
        """,
        ("APIM", "Incident"): """
            Runbook: API Gateway Latency
            1. Check backend health probes
            2. Review request/response sizes
            3. Check rate limiting policies
            4. Consider scaling out API Management
        """,
        ("Identity", "Security"): """
            Runbook: Suspicious Login Response
            1. Block source IP immediately
            2. Review affected accounts for compromise
            3. Enable MFA if not already active
            4. Preserve logs for investigation
        """,
        ("Redis", "Incident"): """
            Runbook: Redis Memory Pressure
            1. Review memory analysis in portal
            2. Identify large keys
            3. Consider scaling to higher tier
            4. Review TTL policies
        """,
    }
    
    for (svc_key, cat_key), runbook in runbooks.items():
        if svc_key.lower() in service.lower() and cat_key.lower() == category.lower():
            return runbook.strip()
    
    return f"No specific runbook found for {service}/{category}. Follow general incident response procedures."


@tool
def search_known_issues(service: str, keywords: str) -> str:
    """
    Search for known issues matching service and keywords.
    
    Args:
        service: The service name to search issues for.
        keywords: Keywords to search for in known issues.
    
    Returns:
        Known issue information if found.
    """
    known_issues = {
        "AKS": {
            "notready": "KI-2024-001: AKS nodes may enter NotReady due to kubelet memory leak in version 1.27.3. Mitigation: Upgrade to 1.27.5+",
            "eviction": "KI-2024-002: Pod eviction storms can occur with aggressive PDB settings. Review PodDisruptionBudgets.",
        },
        "APIM": {
            "latency": "KI-2024-010: Latency spikes observed when policy expressions contain complex XML parsing. Simplify policies.",
        },
        "Redis": {
            "memory": "KI-2024-015: Redis 6.0 has known memory fragmentation issues. Consider Redis 7.0 upgrade.",
        },
    }
    
    for svc_key, issues in known_issues.items():
        if svc_key.lower() in service.lower():
            for kw, issue in issues.items():
                if kw.lower() in keywords.lower():
                    return issue
    
    return f"No known issues found for {service} with keywords: {keywords}"


@tool(approval_mode="always_require")
def restart_service(service: str) -> str:
    """
    Restart a service. DANGEROUS ACTION - requires approval.
    
    Args:
        service: The service name to restart.
    
    Returns:
        Confirmation message after restart.
    """
    # This is a mock - no actual restart happens
    return f"[MOCK] Service '{service}' has been restarted successfully. Recovery time: ~2 minutes."


@tool(approval_mode="always_require")
def open_sev1_bridge(incident_id: str, customer: str) -> str:
    """
    Open a Sev1 bridge call. DANGEROUS ACTION - requires approval.
    
    Args:
        incident_id: The incident ID to open bridge for.
        customer: The customer name.
    
    Returns:
        Bridge call details.
    """
    # Mock bridge creation
    return f"[MOCK] Sev1 bridge opened for {incident_id}. Customer: {customer}. Bridge ID: BR-{incident_id}-001. Dial-in: +1-800-555-0123"
