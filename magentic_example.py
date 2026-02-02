# Copyright (c) Microsoft. All rights reserved.

"""Magentic Orchestration Example: Startup Idea Analyzer.

This example demonstrates the Magentic orchestration pattern with specialized agents
that collaborate to analyze startup ideas from multiple perspectives:

1. Market Researcher - Analyzes market size, trends, and competition
2. Financial Analyst - Evaluates revenue potential, costs, and funding needs  
3. Tech Advisor - Assesses technical feasibility and implementation challenges
4. Magentic Manager - Dynamically coordinates the team based on task requirements

The Magentic manager maintains shared context, tracks progress, and adapts the workflow
in real-time - perfect for complex analysis where the solution path isn't known in advance.
"""

import asyncio
import json
import logging
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Awaitable, Callable, cast

from dotenv import load_dotenv

from agent_framework import (
    AgentRunContext,
    AgentRunUpdateEvent,
    ChatAgent,
    ChatMessage,
    MagenticBuilder,
    MagenticOrchestratorEvent,
    MagenticPlanReviewRequest,
    MagenticProgressLedger,
    RequestInfoEvent,
    WorkflowOutputEvent,
)
from agent_framework.azure import AzureOpenAIChatClient


# =============================================================================
# Markdown Discussion Logger Middleware
# =============================================================================

class DiscussionLogger:
    """Logs agent discussions to a Markdown file in real-time."""
    
    def __init__(self, output_dir: str = "discussions"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.entries: list[dict] = []
        self.start_time: datetime | None = None
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.filepath = self.output_dir / f"discussion_{self.session_id}.md"
        self.task_description = ""
        self._initialized = False
        
    def _get_agent_emoji(self, agent_name: str) -> str:
        """Get emoji for agent based on name."""
        emojis = {
            "MarketResearcher": "🔍",
            "FinancialAnalyst": "💰",
            "TechAdvisor": "⚙️",
            "MagenticManager": "🎯",
            "Orchestrator": "📋",
            "FinalReport": "📊",
        }
        return emojis.get(agent_name, "🤖")
    
    def _get_agent_personality(self, agent_name: str) -> str:
        """Get personality description for agent."""
        personalities = {
            "MarketResearcher": "😰 Pessimist",
            "FinancialAnalyst": "🌈 Optimist",
            "TechAdvisor": "🤔 Skeptic",
            "MagenticManager": "💪 Mediator",
        }
        return personalities.get(agent_name, "")
    
    def initialize(self, task_description: str = ""):
        """Initialize the markdown file with header."""
        self.task_description = task_description
        self._initialized = True
        
        header = f"""# 🚀 Agent Discussion Log

**Session ID:** `{self.session_id}`  
**Started:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📝 Task

> {task_description[:500]}{'...' if len(task_description) > 500 else ''}

## 👥 Participants

| Agent | Role | Personality | Emoji |
|-------|------|-------------|-------|
| MarketResearcher | Market Research Specialist | 😰 Pessimist - sees risks everywhere | 🔍 |
| FinancialAnalyst | Financial Analyst | 🌈 Optimist - sees opportunity in everything | 💰 |
| TechAdvisor | Technical Advisor | 🤔 Skeptic - questions everything | ⚙️ |
| MagenticManager | Orchestrator / Manager | 💪 Mediator - must balance the team | 🎯 |

---

## 💬 Discussion Timeline

"""
        self.filepath.write_text(header, encoding="utf-8")
    
    def log_entry(self, agent_name: str, role: str, content: str, metadata: dict | None = None):
        """Log a discussion entry and append to file immediately."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "agent_name": agent_name,
            "role": role,
            "content": content,
            "metadata": metadata or {},
        }
        self.entries.append(entry)
        
        # Append to file immediately
        self._append_entry_to_file(entry)
    
    def _append_entry_to_file(self, entry: dict):
        """Append a single entry to the markdown file."""
        agent_name = entry["agent_name"]
        emoji = self._get_agent_emoji(agent_name)
        personality = self._get_agent_personality(agent_name)
        timestamp = datetime.fromisoformat(entry["timestamp"]).strftime("%H:%M:%S")
        content = entry["content"]
        
        lines = []
        
        # Format the entry header
        personality_str = f" *{personality}*" if personality else ""
        lines.append(f"### {emoji} **{agent_name}**{personality_str} <sub>({timestamp})</sub>")
        lines.append("")
        
        # Add content in a blockquote for better readability
        if content:
            content_lines = content.strip().split("\n")
            for line in content_lines:
                if line.strip():
                    lines.append(f"> {line}")
                else:
                    lines.append(">")
            lines.append("")
        
        lines.append("---")
        lines.append("")
        
        # Append to file
        with open(self.filepath, "a", encoding="utf-8") as f:
            f.write("\n".join(lines))
    
    def finalize(self):
        """Add summary section at the end of the file."""
        # Count per agent
        agent_counts = {}
        for entry in self.entries:
            name = entry["agent_name"]
            agent_counts[name] = agent_counts.get(name, 0) + 1
        
        summary = f"""
## 📊 Summary

- **Total Exchanges:** {len(self.entries)}
- **Agents Involved:** {len(set(e['agent_name'] for e in self.entries))}
- **Ended:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

### Participation by Agent

"""
        for agent, count in sorted(agent_counts.items(), key=lambda x: -x[1]):
            emoji = self._get_agent_emoji(agent)
            summary += f"- {emoji} **{agent}**: {count} message(s)\n"
        
        with open(self.filepath, "a", encoding="utf-8") as f:
            f.write(summary)
        
        return self.filepath


# Global discussion logger instance
discussion_logger: DiscussionLogger | None = None


def create_discussion_middleware(logger: DiscussionLogger, agent_name: str):
    """Create a middleware function that logs agent discussions."""
    
    async def discussion_logging_middleware(
        context: AgentRunContext,
        next: Callable[[AgentRunContext], Awaitable[None]],
    ) -> None:
        """Middleware that logs agent messages to the discussion log."""
        
        # Log input messages
        input_text = ""
        for msg in context.messages:
            if hasattr(msg, "text") and msg.text:
                input_text += msg.text + "\n"
        
        # Log that the agent is processing
        logger.log_entry(
            agent_name=agent_name,
            role="processing",
            content=input_text.strip() if input_text else "(Processing...)",
            metadata={"input_messages_count": len(context.messages)},
        )
        
        # Execute the agent
        start_time = time.time()
        await next(context)
        elapsed = time.time() - start_time
        
        # Log the response (captured from context after execution)
        # Note: The actual response is streamed, so we capture what we can
        logger.log_entry(
            agent_name=agent_name,
            role="response",
            content=f"(Completed in {elapsed:.2f}s)",
            metadata={"elapsed_seconds": elapsed},
        )
    
    return discussion_logging_middleware

# Load environment variables from .env file
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def get_azure_chat_client():
    """Create an Azure OpenAI chat client using environment variables."""
    return AzureOpenAIChatClient(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
        api_version=os.getenv("API_VERSION", "2025-01-01-preview"),
    )


def create_specialized_agents(logger: DiscussionLogger | None = None):
    """Create the specialized agents for startup analysis."""
    
    # Market Research Specialist - PESSIMIST personality
    market_researcher = ChatAgent(
        name="MarketResearcher",
        description="Expert in market research - VERY pessimistic, sees risks and problems everywhere",
        instructions="""You are a PESSIMISTIC Market Research Specialist. You have a negative outlook and always focus on risks, problems, and reasons why things will fail.
        
        YOUR PERSONALITY:
        - You are deeply skeptical and always assume the worst
        - You focus heavily on competition, market saturation, and barriers
        - You often say things like "I've seen this fail before", "The market is brutal", "Competition will crush this"
        - You question optimistic assumptions and demand proof
        - You highlight every possible risk and downside
        
        YOUR ANALYSIS MUST INCLUDE:
        1. Why the market might be smaller than expected
        2. Strong competitors that will fight back aggressively
        3. Market timing problems and barriers to entry
        4. Customer segments that are hard to reach or convince
        5. Historical examples of similar ideas that failed
        
        Be thorough in your pessimism. Challenge every positive assumption.
        The manager will need to work hard to get balanced insights from you.""",
        chat_client=get_azure_chat_client(),
        middleware=[create_discussion_middleware(logger, "MarketResearcher")] if logger else None,
    )
    
    # Financial Analyst - OPTIMIST personality  
    financial_analyst = ChatAgent(
        name="FinancialAnalyst", 
        description="Expert in financial modeling - VERY optimistic, sees opportunity everywhere",
        instructions="""You are an OPTIMISTIC Financial Analyst. You have a very positive outlook and see massive financial opportunity in everything.
        
        YOUR PERSONALITY:
        - You are extremely enthusiastic and see billion-dollar potential everywhere
        - You use aggressive growth assumptions and best-case scenarios
        - You often say things like "This could be huge!", "The revenue potential is massive!", "Investors will love this!"
        - You downplay costs and risks, focusing on upside
        - You compare everything to successful unicorns
        
        YOUR ANALYSIS MUST INCLUDE:
        1. Aggressive revenue projections with hockey-stick growth
        2. Why unit economics will be amazing at scale
        3. How costs will decrease dramatically over time
        4. Why investors will throw money at this opportunity
        5. Comparisons to successful companies (even if stretches)
        
        Be enthusiastically optimistic. Paint the rosiest financial picture.
        The manager will need to work hard to get realistic numbers from you.""",
        chat_client=get_azure_chat_client(),
        middleware=[create_discussion_middleware(logger, "FinancialAnalyst")] if logger else None,
    )
    
    # Technical Advisor - SKEPTIC personality
    tech_advisor = ChatAgent(
        name="TechAdvisor",
        description="Expert in technology - Very skeptical, questions everything technically",
        instructions="""You are a SKEPTICAL Technical Advisor. You question every technical claim and demand deep justification.
        
        YOUR PERSONALITY:
        - You are highly skeptical of "simple" solutions
        - You always ask "but have you considered...?" and "what about edge cases?"
        - You often say things like "This is harder than it looks", "The devil is in the details", "I've seen this go wrong"
        - You focus on technical debt, scaling problems, and hidden complexity
        - You question whether AI/ML claims are realistic
        
        YOUR ANALYSIS MUST INCLUDE:
        1. Technical challenges that are being underestimated
        2. Why the timeline is probably too optimistic
        3. Scaling problems that will emerge
        4. Security and reliability concerns
        5. Why the team size estimate is probably wrong
        
        Be technically rigorous and skeptical. Don't accept hand-wavy technical claims.
        The manager will need to work hard to get constructive technical guidance from you.""",
        chat_client=get_azure_chat_client(),
        middleware=[create_discussion_middleware(logger, "TechAdvisor")] if logger else None,
    )
    
    # Magentic Manager - MEDIATOR who must balance the difficult team
    manager_agent = ChatAgent(
        name="MagenticManager",
        description="Orchestrator that must balance a difficult team with conflicting personalities",
        instructions="""You are the lead analyst coordinating a DIFFICULT team of specialists with strong conflicting personalities:
        
        - MarketResearcher: PESSIMIST - always sees doom and gloom, focuses on risks
        - FinancialAnalyst: OPTIMIST - unrealistically positive, inflates projections  
        - TechAdvisor: SKEPTIC - questions everything, finds problems
        
        YOUR CHALLENGE:
        You must mediate between these extreme personalities to extract BALANCED, REALISTIC insights.
        
        YOUR APPROACH:
        1. When the pessimist is too negative, push back and ask for balanced view
        2. When the optimist is too rosy, demand realistic assumptions
        3. When the skeptic blocks progress, ask for constructive alternatives
        4. Synthesize conflicting views into actionable insights
        5. Call out when someone is being too extreme
        
        YOU MUST:
        - Acknowledge each specialist's concerns before redirecting
        - Ask follow-up questions to get past extreme positions
        - Challenge both overly negative AND overly positive views
        - Push for specific numbers and evidence, not just opinions
        - Produce a BALANCED final recommendation despite the team's biases
        
        This is a difficult team to manage. Show leadership and get results!""",
        chat_client=get_azure_chat_client(),
        middleware=[create_discussion_middleware(logger, "MagenticManager")] if logger else None,
    )
    
    return market_researcher, financial_analyst, tech_advisor, manager_agent


def build_magentic_workflow(
    market_researcher: ChatAgent,
    financial_analyst: ChatAgent,
    tech_advisor: ChatAgent,
    manager_agent: ChatAgent,
    enable_plan_review: bool = False,
):
    """Build the Magentic workflow with optional human-in-the-loop plan review."""
    
    builder = (
        MagenticBuilder()
        .participants([market_researcher, financial_analyst, tech_advisor])
        .with_manager(
            agent=manager_agent,
            max_round_count=15,  # Allow enough rounds for thorough analysis
            max_stall_count=3,   # Reset if stuck
            max_reset_count=2,   # Max resets before giving up
        )
    )
    
    if enable_plan_review:
        builder = builder.with_plan_review()
    
    return builder.build()


async def run_analysis_with_streaming(workflow, startup_idea: str, disc_logger: DiscussionLogger | None = None):
    """Run the startup analysis with streaming output."""
    
    print("\n" + "=" * 80)
    print("🚀 STARTUP IDEA ANALYZER - Magentic Orchestration Demo")
    print("=" * 80)
    print(f"\n📝 Analyzing startup idea...")
    if disc_logger:
        print(f"📄 Live log: {disc_logger.filepath}")
    print("-" * 80)
    
    # Initialize the markdown file
    if disc_logger:
        disc_logger.initialize(startup_idea)
    
    last_message_id: str | None = None
    output_event: WorkflowOutputEvent | None = None
    current_agent: str | None = None
    current_message_content: list[str] = []
    
    async for event in workflow.run_stream(startup_idea):
        if isinstance(event, AgentRunUpdateEvent):
            # Handle streaming agent responses
            message_id = event.data.message_id
            if message_id != last_message_id:
                # Save previous agent's message to logger (real-time write)
                if disc_logger and current_agent and current_message_content:
                    full_content = "".join(current_message_content)
                    disc_logger.log_entry(
                        agent_name=current_agent,
                        role="response",
                        content=full_content,
                    )
                    current_message_content = []
                
                if last_message_id is not None:
                    print("")  # New line after previous agent
                # Show which agent is speaking (minimal output)
                agent_icons = {
                    "MarketResearcher": "🔍",
                    "FinancialAnalyst": "💰",
                    "TechAdvisor": "⚙️",
                    "MagenticManager": "🎯",
                }
                icon = agent_icons.get(event.executor_id, "•")
                print(f"\n{icon} {event.executor_id}", end=" ", flush=True)
                last_message_id = message_id
                current_agent = event.executor_id
            
            # Capture streaming content
            chunk = str(event.data)
            current_message_content.append(chunk)
            # Minimal terminal output - just show agent is working
            print(".", end="", flush=True)
            
        elif isinstance(event, MagenticOrchestratorEvent):
            # Save any pending message before orchestrator event
            if disc_logger and current_agent and current_message_content:
                full_content = "".join(current_message_content)
                disc_logger.log_entry(
                    agent_name=current_agent,
                    role="response",
                    content=full_content,
                )
                current_message_content = []
                current_agent = None
            
            # Minimal terminal output for orchestrator events
            print(f"\n📋 [{event.event_type.name}]", end=" ", flush=True)
            if isinstance(event.data, MagenticProgressLedger):
                ledger_dict = event.data.to_dict()
                # Log orchestrator event to markdown
                if disc_logger:
                    disc_logger.log_entry(
                        agent_name="Orchestrator",
                        role="progress",
                        content=f"**Event Type:** {event.event_type.name}\n\n```json\n{json.dumps(ledger_dict, indent=2)}\n```",
                    )
            
        elif isinstance(event, WorkflowOutputEvent):
            # Save final pending message
            if disc_logger and current_agent and current_message_content:
                full_content = "".join(current_message_content)
                disc_logger.log_entry(
                    agent_name=current_agent,
                    role="response",
                    content=full_content,
                )
            output_event = event
    
    # Print final output
    if output_event:
        print("\n\n" + "=" * 80)
        print("📊 FINAL ANALYSIS REPORT")
        print("=" * 80)
        output_messages = cast(list[ChatMessage], output_event.data)
        final_output = output_messages[-1].text
        print(final_output)
        
        # Log final output
        if disc_logger:
            disc_logger.log_entry(
                agent_name="FinalReport",
                role="output",
                content=final_output,
            )
    
    # Finalize the discussion log
    if disc_logger:
        filepath = disc_logger.finalize()
        print(f"\n\n📄 Discussion log saved to: {filepath}")
    
    return output_event


async def run_analysis_with_plan_review(workflow, startup_idea: str):
    """Run analysis with human-in-the-loop plan review."""
    
    print("\n" + "=" * 80)
    print("🚀 STARTUP IDEA ANALYZER - With Human Plan Review")
    print("=" * 80)
    print(f"\n📝 Analyzing: {startup_idea}\n")
    print("-" * 80)
    
    pending_request: RequestInfoEvent | None = None
    pending_responses: dict[str, any] | None = None
    output_event: WorkflowOutputEvent | None = None
    
    while not output_event:
        # Either continue with responses or start fresh
        if pending_responses is not None:
            stream = workflow.send_responses_streaming(pending_responses)
        else:
            stream = workflow.run_stream(startup_idea)
        
        last_message_id: str | None = None
        
        async for event in stream:
            if isinstance(event, AgentRunUpdateEvent):
                message_id = event.data.message_id
                if message_id != last_message_id:
                    if last_message_id is not None:
                        print("\n")
                    agent_colors = {
                        "MarketResearcher": "🔍",
                        "FinancialAnalyst": "💰",
                        "TechAdvisor": "⚙️",
                        "MagenticManager": "🎯",
                    }
                    icon = agent_colors.get(event.executor_id, "•")
                    print(f"\n{icon} [{event.executor_id}]:", end=" ", flush=True)
                    last_message_id = message_id
                print(event.data, end="", flush=True)
                
            elif isinstance(event, RequestInfoEvent) and event.request_type is MagenticPlanReviewRequest:
                pending_request = event
                
            elif isinstance(event, WorkflowOutputEvent):
                output_event = event
        
        pending_responses = None
        
        # Handle plan review request
        if pending_request is not None:
            event_data = cast(MagenticPlanReviewRequest, pending_request.data)
            
            print("\n\n" + "=" * 60)
            print("🔔 PLAN REVIEW REQUEST")
            print("=" * 60)
            
            if event_data.current_progress is not None:
                print("\n📈 Current Progress:")
                print(json.dumps(event_data.current_progress.to_dict(), indent=2))
            
            print(f"\n📋 Proposed Plan:\n{event_data.plan.text}")
            print("\n" + "-" * 60)
            print("Enter feedback to revise, or press Enter to approve:")
            
            reply = await asyncio.get_event_loop().run_in_executor(None, input, "> ")
            
            if reply.strip() == "":
                print("✅ Plan approved.\n")
                pending_responses = {pending_request.request_id: event_data.approve()}
            else:
                print("📝 Plan revised with feedback.\n")
                pending_responses = {pending_request.request_id: event_data.revise(reply)}
            
            pending_request = None
    
    # Print final output
    if output_event:
        print("\n\n" + "=" * 80)
        print("📊 FINAL ANALYSIS REPORT")
        print("=" * 80)
        output_messages = cast(list[ChatMessage], output_event.data)
        final_output = output_messages[-1].text
        print(final_output)
    
    return output_event


# Example startup ideas to analyze
EXAMPLE_STARTUP_IDEAS = {
    "ai_code_review": """
    Startup Idea: AI-Powered Code Review Platform
    
    An AI-powered code review tool that automatically reviews pull requests,
    identifies bugs, security vulnerabilities, and suggests improvements.
    It integrates with GitHub, GitLab, and Bitbucket, and learns from team
    coding patterns to provide personalized suggestions.
    
    Target market: Software development teams (10-500 developers)
    Pricing model: $20/developer/month
    """,
    
    "sustainable_packaging": """
    Startup Idea: Sustainable Packaging Marketplace
    
    A B2B marketplace connecting e-commerce brands with sustainable packaging
    suppliers. The platform uses AI to recommend the most eco-friendly and
    cost-effective packaging options based on product dimensions and shipping
    requirements. Includes carbon footprint tracking and sustainability reports.
    
    Target market: D2C e-commerce brands, Shopify merchants
    Revenue model: 8% transaction fee + premium analytics subscription
    """,
    
    "mental_health_ai": """
    Startup Idea: AI Mental Health Companion for Workplaces
    
    A B2B mental wellness platform that provides employees with an AI companion
    for daily check-ins, stress management techniques, and escalation to human
    therapists when needed. Employers get anonymous aggregate analytics on
    team wellness trends.
    
    Target market: Companies with 100-5000 employees
    Pricing: $5/employee/month
    Differentiation: Proactive intervention based on behavioral patterns
    """,
}


async def main():
    """Main entry point for the Magentic orchestration demo."""
    
    print("\n🎯 Magentic Orchestration Demo: Startup Idea Analyzer")
    print("=" * 60)
    
    # Create discussion logger
    logger = DiscussionLogger(output_dir="discussions")
    print(f"📝 Discussion will be logged to: discussions/discussion_{logger.session_id}.md")
    
    # Create specialized agents with logging middleware
    market_researcher, financial_analyst, tech_advisor, manager = create_specialized_agents(logger)
    
    # Choose whether to enable plan review (human-in-the-loop)
    print("\nOptions:")
    print("1. Run analysis with streaming (automatic)")
    print("2. Run analysis with plan review (human-in-the-loop)")
    print("3. Exit")
    
    choice = input("\nSelect option (1-3): ").strip()
    
    if choice == "3":
        print("Goodbye!")
        return
    
    enable_plan_review = (choice == "2")
    
    # Select startup idea
    print("\nAvailable startup ideas:")
    for i, (key, _) in enumerate(EXAMPLE_STARTUP_IDEAS.items(), 1):
        print(f"{i}. {key.replace('_', ' ').title()}")
    print("4. Enter custom idea")
    
    idea_choice = input("\nSelect idea (1-4): ").strip()
    
    if idea_choice == "4":
        startup_idea = input("\nEnter your startup idea:\n> ")
    else:
        idea_keys = list(EXAMPLE_STARTUP_IDEAS.keys())
        idx = int(idea_choice) - 1 if idea_choice.isdigit() else 0
        idx = max(0, min(idx, len(idea_keys) - 1))
        startup_idea = EXAMPLE_STARTUP_IDEAS[idea_keys[idx]]
    
    # Build and run workflow
    workflow = build_magentic_workflow(
        market_researcher,
        financial_analyst,
        tech_advisor,
        manager,
        enable_plan_review=enable_plan_review,
    )
    
    if enable_plan_review:
        await run_analysis_with_plan_review(workflow, startup_idea)
    else:
        await run_analysis_with_streaming(workflow, startup_idea, logger)
    
    print("\n✅ Analysis complete!")


# =============================================================================
# Export workflow for DevUI discovery
# =============================================================================
def create_magentic_workflow():
    """Create the Magentic workflow for DevUI discovery."""
    market_researcher, financial_analyst, tech_advisor, manager = create_specialized_agents()
    return build_magentic_workflow(
        market_researcher,
        financial_analyst,
        tech_advisor,
        manager,
        enable_plan_review=False,
    )


# Export the workflow instance for DevUI
workflow = create_magentic_workflow()


if __name__ == "__main__":
    asyncio.run(main())
