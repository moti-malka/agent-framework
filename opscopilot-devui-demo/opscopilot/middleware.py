"""
Middleware for OpsCopilot demo.
Simple logging middleware for agents and tools.
"""
import time
from typing import Any
from agent_framework import (
    AgentMiddleware,
    FunctionMiddleware,
    AgentRunContext,
    FunctionContext,
    MiddlewareResult,
)


class LoggingAgentMiddleware(AgentMiddleware):
    """Logs agent invocation start/end with timing."""
    
    async def invoke(
        self,
        context: AgentRunContext,
        next_middleware: Any,
    ) -> MiddlewareResult:
        agent_name = context.agent.name if hasattr(context, 'agent') else "Unknown"
        messages_count = len(context.messages) if hasattr(context, 'messages') else 0
        
        print(f"\n{'='*50}")
        print(f"🤖 Agent START: {agent_name}")
        print(f"   Messages: {messages_count}")
        print(f"{'='*50}")
        
        start_time = time.time()
        
        try:
            result = await next_middleware(context)
            elapsed = time.time() - start_time
            
            print(f"\n{'='*50}")
            print(f"✅ Agent END: {agent_name}")
            print(f"   Elapsed: {elapsed:.2f}s")
            print(f"{'='*50}\n")
            
            return result
        except Exception as e:
            elapsed = time.time() - start_time
            print(f"\n{'='*50}")
            print(f"❌ Agent ERROR: {agent_name}")
            print(f"   Elapsed: {elapsed:.2f}s")
            print(f"   Error: {str(e)}")
            print(f"{'='*50}\n")
            raise


class LoggingFunctionMiddleware(FunctionMiddleware):
    """Logs tool/function invocations with args and results."""
    
    async def invoke(
        self,
        context: FunctionContext,
        next_middleware: Any,
    ) -> Any:
        func_name = context.function.name if hasattr(context, 'function') else "Unknown"
        args = context.args if hasattr(context, 'args') else {}
        
        print(f"\n  🔧 Tool CALL: {func_name}")
        print(f"     Args: {args}")
        
        start_time = time.time()
        
        try:
            result = await next_middleware(context)
            elapsed = time.time() - start_time
            
            # Truncate long results for readability
            result_str = str(result)
            if len(result_str) > 200:
                result_str = result_str[:200] + "..."
            
            print(f"  ✅ Tool RESULT: {func_name}")
            print(f"     Elapsed: {elapsed:.3f}s")
            print(f"     Result: {result_str}")
            
            return result
        except Exception as e:
            elapsed = time.time() - start_time
            print(f"  ❌ Tool ERROR: {func_name}")
            print(f"     Elapsed: {elapsed:.3f}s")
            print(f"     Error: {str(e)}")
            raise


def get_middleware_list() -> list:
    """Return the list of middleware to attach to agents."""
    return [
        LoggingAgentMiddleware(),
        LoggingFunctionMiddleware(),
    ]
