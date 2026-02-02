"""
Simple memory/context provider for OpsCopilot demo.
"""
import re
from typing import Any
from agent_framework import ContextProvider, AgentRunContext


class OpsMemory(ContextProvider):
    """
    Simple context provider that remembers:
    - preferred_language (default: hebrew)
    - last_customer (optional)
    - last_service (optional)
    
    Adds instructions on invoke and extracts context on completion.
    """
    
    def __init__(self):
        self.preferred_language: str = "hebrew"
        self.last_customer: str | None = None
        self.last_service: str | None = None
    
    async def invoking(self, context: AgentRunContext) -> str | None:
        """
        Called before agent runs. Returns context instructions.
        """
        instructions = []
        
        # Language preference
        if self.preferred_language.lower() == "hebrew":
            instructions.append("Respond in Hebrew when addressing the customer. Keep technical terms in English.")
        else:
            instructions.append(f"Respond in {self.preferred_language}. Keep answers concise.")
        
        # Add context about previous interactions
        if self.last_service:
            instructions.append(f"Context: Previous interaction involved service '{self.last_service}'.")
        
        if self.last_customer:
            instructions.append(f"Context: Previous customer was '{self.last_customer}'.")
        
        return " ".join(instructions) if instructions else None
    
    async def invoked(self, context: AgentRunContext, result: Any) -> None:
        """
        Called after agent runs. Extracts and stores context.
        """
        # Try to extract customer and service from the input messages
        if hasattr(context, 'messages'):
            for msg in context.messages:
                content = str(msg.content) if hasattr(msg, 'content') else str(msg)
                self._extract_context(content)
    
    def _extract_context(self, text: str) -> None:
        """Extract customer and service from text using simple patterns."""
        # Look for customer pattern
        customer_match = re.search(r'[Cc]ustomer[:\s]+([A-Za-z0-9_-]+)', text)
        if customer_match:
            self.last_customer = customer_match.group(1)
        
        # Look for service pattern
        service_match = re.search(r'[Ss]ervice[:\s]+([A-Za-z0-9_-]+)', text)
        if service_match:
            self.last_service = service_match.group(1)
    
    def set_language(self, language: str) -> None:
        """Update preferred language."""
        self.preferred_language = language
    
    def get_state(self) -> dict:
        """Return current memory state for debugging."""
        return {
            "preferred_language": self.preferred_language,
            "last_customer": self.last_customer,
            "last_service": self.last_service,
        }
    
    def clear(self) -> None:
        """Clear memory state."""
        self.last_customer = None
        self.last_service = None


# Global instance for sharing across agents
ops_memory = OpsMemory()


def get_ops_memory() -> OpsMemory:
    """Return the shared OpsMemory instance."""
    return ops_memory
