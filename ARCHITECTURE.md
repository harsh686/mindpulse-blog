# 🏗️ System Architecture

## Multi-Agent Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                       USER INPUT                                 │
│  Topic: "The Future of AI in Healthcare"                        │
│  Tone: "Professional yet friendly"                              │
└───────────────────────┬─────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────┐
│                   MARVIN THREAD (Shared Context)                │
│  Maintains conversation history & context across all agents     │
└─────────────────────────┬───────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┬──────────────┐
        │                 │                 │              │
        ▼                 ▼                 ▼              ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  RESEARCH   │  │  STRATEGY   │  │   WRITER    │  │     SEO     │
│   AGENT     │  │   AGENT     │  │   AGENT     │  │   AGENT     │
├─────────────┤  ├─────────────┤  ├─────────────┤  ├─────────────┤
│ Speciality: │  │ Speciality: │  │ Speciality: │  │ Speciality: │
│  Research   │  │  Planning   │  │   Writing   │  │ Optimization│
│             │  │             │  │             │  │             │
│ Gathers:    │  │ Creates:    │  │ Produces:   │  │ Optimizes:  │
│ • Key pts   │  │ • Outline   │  │ • Intro     │  │ • Title     │
│ • Stats     │  │ • Hook      │  │ • Sections  │  │ • Meta desc │
│ • Trends    │  │ • Structure │  │ • Conclusion│  │ • Keywords  │
│ • Audience  │  │ • Takeaways │  │ • CTA       │  │ • Slug      │
└──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
       │                │                │                │
       │    Context     │    Context     │    Context     │
       │    Flows ──────┼────────────────┼────────────────┤
       │                │                │                │
       ▼                ▼                ▼                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    STRUCTURED OUTPUT                             │
│                                                                  │
│  BlogPost {                                                      │
│    title: "AI Healthcare: 5 Transformative Trends"             │
│    slug: "ai-healthcare-transformative-trends"                  │
│    meta_description: "Discover how AI is..."                    │
│    keywords: ["AI healthcare", "medical AI", ...]               │
│    introduction: "In the rapidly evolving..."                   │
│    sections: [                                                   │
│      {heading: "...", content: "..."},                          │
│      ...                                                         │
│    ],                                                            │
│    conclusion: "As we've explored...",                          │
│    call_to_action: "Ready to learn more?...",                   │
│    word_count: 1847                                             │
│  }                                                               │
└───────────────────────┬─────────────────────────────────────────┘
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
┌─────────────────┐           ┌─────────────────┐
│  MARKDOWN FILE  │           │   JSON FILE     │
├─────────────────┤           ├─────────────────┤
│ slug.md         │           │ slug.json       │
│                 │           │                 │
│ For publishing  │           │ For data/API    │
│ on blogs/CMS    │           │ use             │
└─────────────────┘           └─────────────────┘
```

## Agent Communication Flow

```
1. Research Phase
   User Topic ──> Research Agent ──> ResearchFindings
                                      │
                                      ├─ Key points
                                      ├─ Statistics  
                                      ├─ Trending topics
                                      └─ Target audience

2. Planning Phase  
   ResearchFindings ──> Strategy Agent ──> ContentOutline
                                            │
                                            ├─ Hook
                                            ├─ Sections
                                            └─ Key takeaways

3. Writing Phase
   ContentOutline + ResearchFindings ──> Writer Agent ──> Content
                                                          │
                                                          ├─ Introduction
                                                          ├─ Section 1
                                                          ├─ Section 2
                                                          ├─ ...
                                                          ├─ Conclusion
                                                          └─ CTA

4. Optimization Phase
   All Previous Context ──> SEO Agent ──> SEO Elements
                                          │
                                          ├─ Optimized title
                                          ├─ Meta description
                                          ├─ Keywords
                                          └─ URL slug

5. Assembly
   All Outputs ──> BlogPost Model ──> Files (MD + JSON)
```

## Why This Architecture?

### ✅ Separation of Concerns
Each agent has ONE job:
- Research agent doesn't worry about SEO
- Writer doesn't worry about research accuracy
- SEO specialist focuses only on optimization

### ✅ Reusability
- Swap agents easily (e.g., use different writer personalities)
- Add new agents without changing existing ones
- Test agents independently

### ✅ Quality Control
- Multiple specialized "experts" review different aspects
- Each step can be monitored and debugged
- Clear responsibility for each output component

### ✅ Scalability
- Add new agents (e.g., Image Generator, Social Media Agent)
- Parallel execution possible for independent tasks
- Easy to extend with new capabilities

## Comparison to Single-Agent Approach

### ❌ Single-Agent (Traditional)
```
User Prompt ──> Single Agent ──> Generic Output
```
Problems:
- One agent tries to do everything
- Inconsistent quality
- No specialization
- Hard to debug
- Can't optimize individual steps

### ✅ Multi-Agent (Our Approach)
```
User Prompt ──> Research ──> Strategy ──> Writing ──> SEO ──> Quality Output
```
Benefits:
- Specialized expertise at each step
- Consistent structure
- Easy to debug (know which agent failed)
- Can optimize each agent independently
- Professional-grade results

## Technology Stack

```
┌─────────────────────────────────────┐
│         Your Application            │
│       (blog_generator.py)           │
├─────────────────────────────────────┤
│          Marvin Framework           │ ← Multi-agent orchestration
├─────────────────────────────────────┤
│          Pydantic AI                │ ← Type-safe AI interactions
├─────────────────────────────────────┤
│      OpenAI / Anthropic API         │ ← LLM providers
└─────────────────────────────────────┘
```

## Data Flow

```
Input (String)
    ↓
Pydantic Models (Type-safe)
    ↓
Agent Processing (AI)
    ↓
Pydantic Validation (Ensures correct structure)
    ↓
Structured Output (BlogPost model)
    ↓
File Export (MD + JSON)
```

---

This architecture ensures **reliability**, **quality**, and **maintainability** while leveraging the power of multiple specialized AI agents! 🚀
