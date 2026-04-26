# Agent Framework Notebook - Comprehensive Gap Analysis
**Date**: 2026-04-26
**Analyzed By**: Automated Sync Process

## Executive Summary

The `agent_framework.ipynb` notebook is **COMPREHENSIVE** but missing **4 critical production features**:
1. ❌ **Checkpointing** - Workflow state persistence & recovery
2. ❌ **Evaluation & Testing** - Quality measurement & KPIs  
3. ❌ **Rate Limiting** - API throttling & cost control
4. ❌ **Caching** - Response caching & cost optimization

## Detailed Feature Coverage

### ✅ FULLY COVERED (17 Features)

#### Core Features (6/7)
- ✅ **Single Agent** (Section 1) - ChatAgent creation and basic usage
- ✅ **Streaming** (Section 2) - Token-by-token response streaming
- ✅ **Sessions/Threads** (Section 3) - Multi-turn conversations
- ✅ **Tools** (Section 4) - Function calling with @tool decorator
- ✅ **Human-in-the-Loop** (Section 8) - Approval workflows
- ✅ **Middleware** (Section 9) - Observability and logging

#### Advanced Features (5/8)
- ✅ **Multimodal Input** (Section 5) - Image processing (DataContent/UriContent)
- ✅ **Structured Output** (Section 6) - Pydantic models & JSON schemas
- ✅ **MCP Integration** (Section 7) - Model Context Protocol tools
- ✅ **Error Handling & Retry** (Section 10) - Exponential backoff middleware
- ✅ **Memory** (Section 11) - BaseContextProvider for persistent state

#### Workflows (5/5)
- ✅ **Sequential** (Section 12) - Chain multiple agents
- ✅ **Concurrent** (Section 13) - Parallel fan-out/fan-in  
- ✅ **Group Chat** (Section 14) - Round-robin + AI orchestrator
- ✅ **Magentic** (Section 15) - Lead agent directs team
- ✅ **Handoff** (Section 16) - Dynamic agent-to-agent transfer

### ❌ MISSING FEATURES (4 Critical)

#### 1. Checkpointing (CRITICAL)
**Status**: Not covered
**Priority**: ⚠️ HIGH - Required for production workflows
**Story Integration**: Section 12.5 (between Sequential and Concurrent)

**DropGo Scenario**: 
> "Black Friday email surge: 10,000 emails need processing overnight. At 3AM, server crashes at email #6,847. WITHOUT checkpointing, we start over from email #1. WITH checkpointing, we resume from #6,847."

**Features to Cover**:
- `FileCheckpointStorage` for local development
- `CosmosCheckpointStorage` for production (Azure Cosmos DB)
- `workflow.checkpoints` to list saved checkpoints
- `workflow.run(checkpoint_id=...)` to resume from checkpoint
- Automatic checkpoint creation at superstep boundaries
- State serialization (executor state, messages, requests)

**Sample Code Needed**:
``````python
from agent_framework import FileCheckpointStorage, WorkflowBuilder

# Enable checkpointing
storage = FileCheckpointStorage("./checkpoints")
workflow = (
    WorkflowBuilder(start_executor=classifier, checkpoint_storage=storage)
    .add_edge(classifier, drafter)
    .add_edge(drafter, reviewer)
    .build()
)

# Initial run - crashes at step 2
async for event in workflow.run("Process 10K emails"):
    if event.type == "output":
        print(event.data)

# Resume from checkpoint after crash
checkpoints = await storage.list_checkpoints(workflow_name=workflow.name)
latest = sorted(checkpoints, key=lambda c: c.timestamp, reverse=True)[0]

async for event in workflow.run(checkpoint_id=latest.checkpoint_id):
    if event.type == "output":
        print("✅ Resumed from checkpoint!")
``````

**Production Version (Azure Cosmos DB)**:
``````python
from azure.identity.aio import DefaultAzureCredential
from agent_framework_azure_cosmos import CosmosCheckpointStorage

async with CosmosCheckpointStorage(
    endpoint="https://dropgo.documents.azure.com:443/",
    credential=DefaultAzureCredential(),
    database_name="agent-framework",
    container_name="workflow-checkpoints",
) as storage:
    workflow = WorkflowBuilder(..., checkpoint_storage=storage).build()
    async for event in workflow.run("Process emails"):
        ...
``````

**Documentation References**:
- https://learn.microsoft.com/agent-framework/workflows/checkpoints
- https://github.com/microsoft/agent-framework/tree/main/python/samples/03-workflows/checkpoint

---

#### 2. Evaluation & Testing (CRITICAL)
**Status**: Not covered
**Priority**: ⚠️ HIGH - Required for quality assurance
**Story Integration**: Section 17 (new section after Handoff)

**DropGo Scenario**:
> "Management asks: 'How do we know the AI agent is good?' We need KPIs: response relevance, task completion rate, tool accuracy. Run evaluations weekly to track quality trends."

**Features to Cover**:
- `LocalEvaluator` with built-in checks (fast, no API calls)
- `FoundryEvals` for cloud-based LLM-as-judge evaluation
- `evaluate_agent()` for single-agent evaluation
- `evaluate_workflow()` for multi-agent workflows
- Built-in checks: `keyword_check`, `tool_called_check`, `tool_call_args_match`
- Custom evaluator functions with `@evaluator` decorator
- Expected outputs and tool calls for validation

**Sample Code Needed**:
``````python
from agent_framework import (
    evaluate_agent, 
    LocalEvaluator, 
    keyword_check, 
    tool_called_check,
    evaluator
)
from agent_framework_azure_ai import FoundryEvals

# Define custom check
@evaluator
def is_helpful(response: str) -> bool:
    """Response must be at least 50 words."""
    return len(response.split()) >= 50

# Local evaluator (fast, no API costs)
local = LocalEvaluator(
    keyword_check("order", "refund"),  # Must mention key terms
    tool_called_check("get_order_status"),  # Must use correct tool
    is_helpful  # Custom check
)

# Cloud evaluator (LLM-as-judge)
foundry = FoundryEvals(
    project_client=foundry_client,
    model_deployment="gpt-4o",
    evaluators=[
        FoundryEvals.RELEVANCE,
        FoundryEvals.COHERENCE,
        FoundryEvals.TASK_ADHERENCE,
        FoundryEvals.TOOL_CALL_ACCURACY,
    ]
)

# Evaluate agent against test queries
test_queries = [
    "Where is my order #12345?",
    "I need a refund for a damaged product",
    "How do I track my shipment?",
]

results = await evaluate_agent(
    agent=support_agent,
    queries=test_queries,
    evaluators=[local, foundry],
    num_repetitions=3  # Run each query 3x to measure consistency
)

# Print results
print(f"Local Checks: {results[0].passed}/{results[0].total} passed")
print(f"Foundry Evals: {results[1].passed}/{results[1].total} passed")

# Access per-item details
for item in results[0].items:
    print(f"Query: {item.query}")
    print(f"  Score: {item.score:.2f} ({'PASS' if item.passed else 'FAIL'})")
    print(f"  Details: {item.details}")
``````

**Evaluation Metrics Dashboard** (markdown table):
| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Relevance | >80% | 87% | ✅ PASS |
| Task Completion | >90% | 92% | ✅ PASS |
| Tool Accuracy | >95% | 89% | ⚠️ NEEDS IMPROVEMENT |
| Response Time | <3s | 2.1s | ✅ PASS |

**Documentation References**:
- https://learn.microsoft.com/agent-framework/agents/evaluation
- https://github.com/microsoft/agent-framework/tree/main/python/samples/02-agents/evaluation

---

#### 3. Rate Limiting (IMPORTANT)
**Status**: Not covered
**Priority**: 🟡 MEDIUM - Important for cost control
**Story Integration**: Section 9.5 (insert after Middleware)

**DropGo Scenario**:
> "OpenAI allows 60 requests/minute on our tier. Black Friday surge = 200 emails/minute. Without rate limiting, we hit API errors and lose customers. WITH rate limiting, requests are queued and processed smoothly."

**Features to Cover**:
- Token bucket algorithm for rate limiting
- Request queuing when limit reached
- Middleware-based implementation
- Per-minute request tracking
- Configurable limits by API provider

**Sample Code Needed**:
``````python
import time
import asyncio
from collections import deque
from agent_framework import Middleware, Message

class RateLimitMiddleware(Middleware):
    """Token bucket rate limiter - allows burst but enforces average rate."""
    
    def __init__(self, max_requests: int = 60, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.request_times = deque()
        self.lock = asyncio.Lock()
    
    async def before_run(self, agent, session, context, state):
        async with self.lock:
            now = time.time()
            
            # Remove requests older than the window
            while self.request_times and self.request_times[0] < now - self.window_seconds:
                self.request_times.popleft()
            
            # Check if we're at the limit
            if len(self.request_times) >= self.max_requests:
                # Calculate wait time
                oldest = self.request_times[0]
                wait_time = (oldest + self.window_seconds) - now
                
                print(f"⏳ Rate limit reached. Waiting {wait_time:.1f}s...")
                await asyncio.sleep(wait_time)
                
                # Re-check after waiting
                now = time.time()
                while self.request_times and self.request_times[0] < now - self.window_seconds:
                    self.request_times.popleft()
            
            # Record this request
            self.request_times.append(now)

# Apply rate limiter to agent
rate_limiter = RateLimitMiddleware(max_requests=60, window_seconds=60)
support_agent.middleware.append(rate_limiter)

# Test with burst of 100 requests
async def test_rate_limiting():
    tasks = []
    for i in range(100):
        task = support_agent.run(f"Email #{i}")
        tasks.append(task)
    
    results = await asyncio.gather(*tasks)
    print(f"✅ Processed {len(results)} emails with rate limiting")

await test_rate_limiting()
``````

**Metrics to Show**:
- Requests/minute before rate limiting: 200 → API errors
- Requests/minute after rate limiting: 60 → Smooth processing
- Queue wait time: Average 2.5s per request
- Cost savings: $0 (no failed requests to retry)

---

#### 4. Caching (IMPORTANT)
**Status**: Not covered
**Priority**: 🟡 MEDIUM - Important for cost optimization
**Story Integration**: Section 9.6 (insert after Rate Limiting)

**DropGo Scenario**:
> "'Where is my order?' gets asked 1,000 times per day for the same 50 popular orders. WITHOUT caching, we call the LLM 1,000 times = $50/day. WITH caching (5-minute TTL), we call it 144 times = $7.20/day. **Saves $12,600/year.**"

**Features to Cover**:
- Response caching with TTL (time-to-live)
- Cache key generation (hash of query)
- Cache hit/miss tracking
- Eviction policy (LRU or TTL-based)
- Middleware-based implementation
- Cost savings metrics

**Sample Code Needed**:
``````python
import hashlib
import time
from typing import Dict, Any, Optional
from agent_framework import Middleware, Message, Response

class CacheMiddleware(Middleware):
    """Cache agent responses with TTL to reduce LLM API costs."""
    
    def __init__(self, ttl_seconds: int = 300):
        self.ttl_seconds = ttl_seconds
        self.cache: Dict[str, tuple[Any, float]] = {}  # {cache_key: (response, timestamp)}
        self.hits = 0
        self.misses = 0
    
    def _cache_key(self, messages: list[Message]) -> str:
        """Generate cache key from message content."""
        content = "".join(msg.text for msg in messages)
        return hashlib.md5(content.encode()).hexdigest()
    
    def _is_fresh(self, timestamp: float) -> bool:
        """Check if cached response is still fresh."""
        return (time.time() - timestamp) < self.ttl_seconds
    
    async def before_run(self, agent, session, context, state):
        """Check cache before running agent."""
        messages = context.get("messages", [])
        cache_key = self._cache_key(messages)
        
        if cache_key in self.cache:
            response, timestamp = self.cache[cache_key]
            if self._is_fresh(timestamp):
                self.hits += 1
                state["cached_response"] = response
                state["cache_hit"] = True
                print(f"✅ Cache HIT (hit rate: {self.hit_rate:.1%})")
                return
        
        self.misses += 1
        state["cache_hit"] = False
    
    async def after_run(self, agent, session, context, state, response):
        """Store response in cache."""
        if not state.get("cache_hit", False):
            messages = context.get("messages", [])
            cache_key = self._cache_key(messages)
            self.cache[cache_key] = (response, time.time())
            print(f"💾 Cached response (cache size: {len(self.cache)})")
    
    @property
    def hit_rate(self) -> float:
        total = self.hits + self.misses
        return self.hits / total if total > 0 else 0.0

# Apply cache middleware
cache = CacheMiddleware(ttl_seconds=300)  # 5-minute TTL
support_agent.middleware.append(cache)

# Simulate repeated queries
popular_queries = [
    "Where is order #12345?",
    "How do I track my shipment?",
    "What's your refund policy?",
]

# First round - cache misses
for query in popular_queries * 3:
    await support_agent.run(query)

# Second round - cache hits
for query in popular_queries * 3:
    await support_agent.run(query)

print(f"\n📊 Cache Statistics:")
print(f"  Hit Rate: {cache.hit_rate:.1%}")
print(f"  Hits: {cache.hits}")
print(f"  Misses: {cache.misses}")
print(f"  Cache Size: {len(cache.cache)} entries")

# Cost analysis
cost_per_call = 0.05  # $0.05 per LLM call
calls_without_cache = cache.hits + cache.misses
calls_with_cache = cache.misses
saved_calls = calls_without_cache - calls_with_cache
savings = saved_calls * cost_per_call

print(f"\n💰 Cost Savings:")
print(f"  Calls without cache: {calls_without_cache}")
print(f"  Calls with cache: {calls_with_cache}")
print(f"  Saved calls: {saved_calls}")
print(f"  Cost savings: ${savings:.2f}")
``````

**Cost Savings Calculation**:
| Scenario | Daily Queries | Cache Hit Rate | LLM Calls | Cost/Day | Annual Cost |
|----------|---------------|----------------|-----------|----------|-------------|
| No Cache | 1,000 | 0% | 1,000 | $50.00 | $18,250 |
| With Cache (5min TTL) | 1,000 | 85% | 150 | $7.50 | $2,738 |
| **SAVINGS** | - | - | **850** | **$42.50** | **$15,512** |

---

## Summary of Required Changes

### Sections to Add
1. **Section 12.5**: Checkpointing (between Sequential and Concurrent workflows)
   - FileCheckpointStorage example
   - Resume from checkpoint demo
   - CosmosCheckpointStorage for production
   - State persistence explanation

2. **Section 17**: Evaluation & Testing (new section after Handoff)
   - LocalEvaluator with built-in checks
   - FoundryEvals cloud evaluation
   - evaluate_agent() usage
   - Metrics dashboard and interpretation

3. **Section 9.5**: Rate Limiting (insert after Middleware section)
   - Token bucket algorithm
   - Rate limiting middleware
   - Queue management
   - Burst handling

4. **Section 9.6**: Caching (insert after Rate Limiting)
   - Cache middleware with TTL
   - Cache hit/miss tracking
   - Cost savings calculation
   - LRU eviction policy

### Cell Count Impact
- Current cells: 96
- New cells to add: ~16 (4 sections × 4 cells average)
- **Final cell count: ~112 cells**

### Story Integration Points
| Feature | Cell Position | DropGo Scenario |
|---------|---------------|-----------------|
| Checkpointing | After cell 66 | "Black Friday batch processing with crash recovery" |
| Rate Limiting | After cell 48 | "Handling API rate limits during email surges" |
| Caching | After cell 48 | "Caching common responses to save $15K/year" |
| Evaluation | After cell 95 | "Measuring agent quality KPIs for management" |

---

## Implementation Verification Checklist

For each new section, verify:
- [ ] Markdown cell explains the feature in DropGo narrative
- [ ] Code cell contains working, runnable example
- [ ] Code uses DropGo scenarios (emails, orders, customers)
- [ ] Section integrates naturally into story progression
- [ ] No duplicate content with existing sections
- [ ] Code follows existing notebook style/patterns
- [ ] All imports are declared
- [ ] Examples show both basic and advanced usage

---

## Next Steps

1. ✅ Create detailed plan (this document)
2. ⏳ Add Checkpointing section (12.5)
3. ⏳ Add Evaluation section (17)
4. ⏳ Add Rate Limiting section (9.5)
5. ⏳ Add Caching section (9.6)
6. ⏳ Test all code examples run successfully
7. ⏳ Create Pull Request with comprehensive description
8. ⏳ Request review from notebook maintainers

**Estimated Time**: 4-6 hours to implement all sections with proper testing

---

## References

### Official Documentation
- **Checkpointing**: https://learn.microsoft.com/agent-framework/workflows/checkpoints
- **Evaluation**: https://learn.microsoft.com/agent-framework/agents/evaluation
- **Middleware**: https://learn.microsoft.com/agent-framework/agents/middleware/
- **Error Handling**: https://learn.microsoft.com/agent-framework/agents/middleware/exception-handling

### GitHub Samples
- **Checkpointing**: https://github.com/microsoft/agent-framework/tree/main/python/samples/03-workflows/checkpoint
- **Evaluation**: https://github.com/microsoft/agent-framework/tree/main/python/samples/02-agents/evaluation
- **Middleware**: https://github.com/microsoft/agent-framework/tree/main/python/samples/02-agents/middleware

### Related PRs
- (To be added after this PR is created)
