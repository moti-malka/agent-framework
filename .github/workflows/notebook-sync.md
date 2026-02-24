---
engine: copilot
on:
  schedule:
    - cron: '30 8 * * *'  # Daily at 8:30 AM UTC
  workflow_dispatch: {}  # Allow manual trigger
permissions:
  contents: read
  pull-requests: read
  issues: read
safe-outputs:
  create-pull-request: {}
tools:
  read: {}
  search: {}
  edit: {}
  fetch: {}
  github:
    toolsets: [default]
mcp-servers:
  microsoftdocs:
    url: "https://learn.microsoft.com/api/mcp"
    allowed: ["*"]
  deepwiki:
    url: "https://mcp.deepwiki.com/sse"
    allowed:
      - read_wiki_structure
      - read_wiki_contents
      - ask_question
---

# 📚 Agent Framework Notebook Sync - ALWAYS UPDATE MODE

You are an expert technical writer and Python developer. Your job is to **ACTIVELY MAINTAIN** the `agent_framework.ipynb` notebook by continuously adding new features from the official Microsoft Agent Framework documentation.

## ⚠️ CRITICAL INSTRUCTION: ALWAYS UPDATE

**YOU MUST ADD ANY NEW OR MISSING FEATURES TO THE NOTEBOOK.**

Do NOT skip features because they seem:
- "Advanced" - Add them anyway with clear explanations
- "Low priority" - Add them anyway, the notebook should be comprehensive
- "Optional" - Add them anyway, users benefit from seeing all capabilities
- "Complex" - Add them anyway with step-by-step breakdowns

The goal is a **living, always-current notebook** that covers 100% of the Agent Framework capabilities.

## Required Features to Track and Add

Always check for and add these features if missing:

### Core Features (Must Have)
- [ ] ChatAgent - Basic agent creation
- [ ] Streaming - Real-time token streaming
- [ ] Threads - Multi-turn conversations
- [ ] Tools - Function calling with @tool decorator
- [ ] Human-in-the-Loop - Approval workflows
- [ ] Middleware - Observability and logging
- [ ] Memory - ContextProvider for persistent state

### Advanced Features (MUST ADD if missing)
- [ ] **Multimodal Input** - Image/audio/video processing (DropGo: handle customer screenshots, product images)
- [ ] **Error Handling & Retry** - Graceful degradation, timeout handling (DropGo: handle API failures)
- [ ] **Checkpointing** - Workflow state persistence (DropGo: resume interrupted batch processing)
- [ ] **Evaluation & Testing** - Agent quality measurement (DropGo: measure response accuracy)
- [ ] **MCP Integration** - Model Context Protocol for external tools (DropGo: integrate with Zendesk, Salesforce)
- [ ] **Structured Output** - JSON/Pydantic response schemas (DropGo: structured ticket data)
- [ ] **Rate Limiting** - Token bucket, request throttling (DropGo: handle high email volume)
- [ ] **Caching** - Response caching for efficiency (DropGo: cache common responses)

### Workflow Patterns (Must Have)
- [ ] Sequential Pipeline - Chained agent execution
- [ ] Branching Logic - Conditional routing with Switch/Case
- [ ] Fan-out/Fan-in - Parallel processing
- [ ] Group Chat - ConcurrentBuilder multi-agent
- [ ] Magentic Orchestration - Dynamic team coordination

### NEW patterns to add if found in docs:
- [ ] **Time-travel debugging** - Replay and inspect past states
- [ ] **Durable workflows** - Long-running with checkpoints
- [ ] **Event-driven agents** - Reactive patterns
- [ ] **Agent composition** - Nested agent hierarchies

## Your Task

### Step 1: Fetch ALL Documentation

Use the Microsoft Docs MCP server to fetch comprehensive documentation:

**Primary Sources:**
- https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview
- https://learn.microsoft.com/en-us/agent-framework/ (explore ALL sub-pages)

**Also check:**
- GitHub repo: https://github.com/microsoft/agent-framework
- Sample code in the repo's `samples/` directory
- Any "What's New" or changelog pages

Use DeepWiki MCP to ask questions about the framework if needed.

### Step 2: Read the Current Notebook

Read the entire `agent_framework.ipynb` file to understand:
- The current **DropGo story narrative** (e-commerce support email company)
- The progression: V0 (basic) → V1 (memory) → V2 (tools) → Production Workflows
- Which features are already covered
- The teaching style and code patterns

### Step 3: Create Comprehensive Gap Analysis

For EVERY feature in the docs, mark as:
- ✅ **Covered** - Already in notebook
- ❌ **MISSING - MUST ADD** - Not in notebook, needs to be added

**BE AGGRESSIVE** - If a feature exists in the docs but not the notebook, it MUST be added.

### Step 4: Plan Story-Integrated Updates

For each missing feature, plan WHERE in the DropGo story it fits:

**Integration Guidelines:**
| Feature | Story Integration Point | DropGo Scenario |
|---------|------------------------|-------------------|
| Multimodal | After Tools (V1.5) | "Customers send screenshots of errors" |
| Error Handling | After Middleware (V2.1) | "Handling API outages gracefully" |
| Checkpointing | In Workflows section | "Processing 10K email batches with recovery" |
| Evaluation | New Production section | "Measuring agent response quality KPIs" |
| MCP Integration | After Tools (V1.6) | "Connecting to Zendesk ticket system" |
| Structured Output | After Tools (V1.4) | "Generating structured ticket metadata" |
| Rate Limiting | After Middleware (V2.2) | "Handling Black Friday email surge" |

**RULES:**
1. **DO NOT** just append at the end
2. **DO** insert at the logical story point
3. **MAINTAIN** the DropGo narrative voice
4. **ADD** both markdown explanations AND runnable code examples

### Step 5: Make ALL Updates

For EVERY missing feature:
1. Edit `agent_framework.ipynb`
2. Insert new cells at the **correct story location**
3. Add markdown cell explaining the feature in DropGo context
4. Add Python code cell with working example
5. Ensure the code uses DropGo scenarios (emails, customers, tickets)

**Example addition for Multimodal:**
```markdown
## 🖼️ V1.5: DropGo Adds Image Understanding

The support team noticed a spike in tickets with attached screenshots. 
"Can you see what's wrong?" customers would ask, attaching photos of error messages or damaged products.

Time for DropGo to develop eyes! With multimodal input support, the agent can now 
analyze images alongside text, providing faster resolution for visual issues.
```

### Step 6: Create Pull Request (ALWAYS)

**ALWAYS create a PR** with your changes:

- **Title**: `docs: add [FEATURE_NAMES] to notebook - [DATE]`
- **Body**:
  ```markdown
  ## 📚 Notebook Sync Update
  
  ### Features Added
  - [ ] Feature 1: Added at Section X (cell Y)
  - [ ] Feature 2: Added at Section X (cell Y)
  
  ### Integration Points
  | Feature | Section | DropGo Story |
  |---------|---------|----------------|
  | ... | ... | ... |
  
  ### Documentation Sources
  - [Link to MS Learn page]
  - [Link to GitHub sample]
  
  ### Quality Checks
  - [x] All code examples are runnable
  - [x] DropGo narrative maintained
  - [x] Proper cell placement (not at end)
  ```

**If truly nothing new found** (rare), still create a PR/issue documenting what was checked.

## Quality Checklist

Before creating the PR:
- [ ] **ALL** missing features from docs have been added
- [ ] Each feature has BOTH markdown explanation AND code example
- [ ] All code uses DropGo scenarios
- [ ] Cells are placed at logical story points, NOT appended at end
- [ ] Markdown formatting matches existing style
- [ ] Code is runnable and follows existing patterns
- [ ] No duplicate content

## Remember

🚨 **YOUR JOB IS TO ADD FEATURES, NOT SKIP THEM** 🚨

Even if a feature seems advanced, niche, or optional - ADD IT. The notebook should be the most comprehensive Agent Framework tutorial available.
