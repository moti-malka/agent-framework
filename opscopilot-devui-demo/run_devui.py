#!/usr/bin/env python3
"""
OpsCopilot DevUI Demo Launcher

Run Instructions:
-----------------
1. Create and activate a virtual environment:
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

3. Set environment variables (choose one):
   
   Option A - Azure OpenAI:
     export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
     export AZURE_OPENAI_API_KEY="your-api-key"
     export AZURE_OPENAI_DEPLOYMENT="gpt-4o"  # optional, defaults to gpt-4o
   
   Option B - OpenAI:
     export OPENAI_API_KEY="your-api-key"
     export OPENAI_MODEL="gpt-4o"  # optional, defaults to gpt-4o

4. Run the DevUI:
   python run_devui.py

5. Open your browser to:
   http://localhost:8080

Usage in DevUI:
---------------
- Select "OpsCopilot Incident Triage" workflow
- Input an incident as JSON, for example:
  {
    "id": "INC-001",
    "title": "AKS Node NotReady",
    "description": "Kubernetes node aks-nodepool1-12345 entered NotReady state",
    "service": "AKS-Prod-West",
    "customer": "Contoso",
    "severity_hint": "High"
  }

- Or select one of the individual agents to test them directly

Features Demonstrated:
- Multi-agent workflow (classifier → enrichment → writer)
- Human-in-the-loop approval for dangerous actions
- Mock tools with @tool decorator
- Middleware logging
- Context provider (memory)
- Streaming workflow execution
"""

import asyncio
import nest_asyncio
from dotenv import load_dotenv

# Apply nest_asyncio to allow nested event loops (needed for some environments)
nest_asyncio.apply()

# Load environment variables from .env file
load_dotenv()


def main():
    """Main entry point for DevUI."""
    from agent_framework.devui import serve
    from opscopilot.workflow import build_workflow
    from opscopilot.agents import build_agents
    from opscopilot.mock_data import INCIDENTS
    
    print("🚀 Starting OpsCopilot DevUI Demo...")
    print("")
    
    # Build agents
    print("📦 Building agents...")
    agents = build_agents()
    
    # Build workflow
    print("🔧 Building workflow...")
    workflow = build_workflow(agents)
    
    # Print available test data
    print("")
    print("📋 Available test incidents:")
    for inc in INCIDENTS[:3]:  # Show first 3
        print(f"   - {inc.id}: {inc.title}")
    print(f"   ... and {len(INCIDENTS) - 3} more")
    print("")
    
    # Entities to register with DevUI
    entities = [
        workflow,
        agents["classifier"],
        agents["writer"],
        agents["qa"],
    ]
    
    print(f"✅ Registering {len(entities)} entities with DevUI:")
    for entity in entities:
        print(f"   - {entity.name} ({entity.id})")
    print("")
    
    # Start DevUI server
    print("🌐 Starting DevUI server...")
    print("   URL: http://localhost:8080")
    print("")
    print("=" * 50)
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    print("")
    
    serve(
        entities=entities,
        auto_open=True,
        host="0.0.0.0",
        port=8080,
    )


if __name__ == "__main__":
    main()
