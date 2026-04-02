"""
AI Blog Post Generator using Marvin
A multi-agent system that orchestrates specialized AI agents to research,
plan, write, and optimize blog posts.

Supported APIs (set ONE in .env):
  - NVIDIA Build  → NVIDIA_API_KEY  (Recommended: Free, fast, Llama 4 Maverick)
  - Google Gemini → GOOGLE_API_KEY
  - Groq          → GROQ_API_KEY
  - OpenAI        → OPENAI_API_KEY
"""

import marvin
from pydantic import BaseModel, Field
from datetime import datetime
from pathlib import Path
import json
import os
from dotenv import load_dotenv, dotenv_values

# Load environment variables
load_dotenv()


class BlogPost(BaseModel):
    """Structured blog post with metadata"""
    title: str = Field(description="Catchy, SEO-friendly title")
    slug: str = Field(description="URL-friendly slug")
    meta_description: str = Field(description="SEO meta description (150-160 chars)")
    keywords: list[str] = Field(description="SEO keywords")
    introduction: str = Field(description="Engaging introduction paragraph")
    sections: list[dict[str, str]] = Field(description="List of {heading, content} sections")
    conclusion: str = Field(description="Compelling conclusion")
    call_to_action: str = Field(description="Clear CTA for readers")
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())


class ResearchFindings(BaseModel):
    """Research output from the research agent"""
    key_points: list[str] = Field(description="Main points to cover")
    statistics: list[str] = Field(description="Relevant statistics and data")
    trending_topics: list[str] = Field(description="Current trending aspects")
    target_audience: str = Field(description="Who should read this")
    sources: list[str] = Field(description="Reference sources")


class SectionOutline(BaseModel):
    """A single section in the outline"""
    title: str = Field(description="Section title/heading")
    description: str = Field(description="Brief description of what this section covers")


class ContentOutline(BaseModel):
    """Detailed content outline"""
    working_title: str
    hook: str = Field(description="Opening hook to grab attention")
    main_sections: list[SectionOutline] = Field(description="Section titles with brief descriptions")
    key_takeaways: list[str]


NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"
NVIDIA_MODEL   = "meta/llama-4-maverick-17b-128e-instruct"


def get_model_config():
    """
    Detect which LLM provider to use and configure environment.
    Priority: NVIDIA → Google → Groq → OpenAI
    """
    raw_env = dotenv_values(".env") if Path(".env").exists() else {}
    # Strip BOM characters from keys if present
    env = {(k.lstrip('\ufeff') if isinstance(k, str) else k): v for k, v in raw_env.items()}

    # ── 1. NVIDIA Build (Llama 4 Maverick) ──────────────────────────────────
    nvidia_key = env.get("NVIDIA_API_KEY") or os.getenv("NVIDIA_API_KEY")
    if nvidia_key:
        # Point the OpenAI SDK (used by marvin) to NVIDIA's endpoint
        os.environ["OPENAI_API_KEY"]   = nvidia_key
        os.environ["OPENAI_BASE_URL"]  = NVIDIA_BASE_URL
        print("\U0001f7e2 Using: NVIDIA Build — Llama 4 Maverick (Free)")
        print(f"\U0001f4e6 Model: {NVIDIA_MODEL}\n")
        return f"openai:{NVIDIA_MODEL}"

    # ── 2. Google Gemini ─────────────────────────────────────────────────────
    google_key = env.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if google_key:
        os.environ["GOOGLE_API_KEY"] = google_key
        print("\U0001f916 Using: Google Gemini (Free & Fast)")
        print("\U0001f4e6 Model: gemini-2.0-flash\n")
        return "gemini/gemini-2.0-flash"

    # ── 3. Groq ───────────────────────────────────────────────────────────────
    groq_key = env.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
    if groq_key:
        os.environ["GROQ_API_KEY"] = groq_key
        groq_model = env.get("GROQ_MODEL") or os.getenv("GROQ_MODEL") or "llama-3.3-70b-versatile"
        print("\U0001f916 Using: Groq (Free & Fast)")
        print(f"\U0001f4e6 Model: {groq_model}\n")
        return f"groq/{groq_model}"

    # ── 4. OpenAI fallback ───────────────────────────────────────────────────
    openai_key = env.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
    if openai_key:
        os.environ["OPENAI_API_KEY"] = openai_key
        print("\U0001f916 Using: OpenAI GPT-4o Mini")
        print("\U0001f4e6 Model: gpt-4o-mini\n")
        return "openai:gpt-4o-mini"

    raise ValueError(
        "\u274c No API key found. Add one of these to your .env file:\n"
        "  \u2022 NVIDIA_API_KEY  (Recommended — Free): https://build.nvidia.com\n"
        "  \u2022 GOOGLE_API_KEY  (Free): https://aistudio.google.com/app/apikey\n"
        "  \u2022 GROQ_API_KEY    (Free): https://console.groq.com/keys\n"
        "  \u2022 OPENAI_API_KEY  (Paid): https://platform.openai.com\n"
    )


# Resolve model once at startup
MODEL = get_model_config()

# ── Agents ───────────────────────────────────────────────────────────────────

researcher = marvin.Agent(
    name="Research Specialist",
    model=MODEL,
    instructions="""You are an expert researcher who:
    - Finds current, relevant information on any topic
    - Identifies trending angles and fresh perspectives
    - Gathers statistics and credible data points
    - Understands target audience needs
    - Prioritizes accurate, up-to-date information

    Always provide comprehensive research with specific details."""
)

strategist = marvin.Agent(
    name="Content Strategist",
    model=MODEL,
    instructions="""You are a content strategy expert who:
    - Creates compelling but CONCISE blog post structures (3-4 sections max)
    - Designs reader-engaging narratives that are quick to read
    - Optimizes content flow for engagement
    - Crafts attention-grabbing hooks
    - Plans sections that build logically
    - Keeps total article to 500-800 words (2.5-4 min read)

    Focus on creating SHORT, punchy outlines. Quality over quantity."""
)

writer = marvin.Agent(
    name="Professional Writer",
    model=MODEL,
    instructions="""You are a skilled blog writer who:
    - Writes clear, engaging, conversational content in 500-800 words total
    - Uses active voice and concrete examples
    - Keeps content concise and impactful (2.5-4 minute read)
    - Breaks down complex topics simply
    - Adds personality while staying professional
    - IMPORTANT: Keep each section brief (1-2 short paragraphs max)

    Write naturally and engagingly, as if explaining to a smart friend."""
)

seo_optimizer = marvin.Agent(
    name="SEO Specialist",
    model=MODEL,
    instructions="""You are an SEO expert who:
    - Optimizes titles for click-through rate
    - Creates compelling meta descriptions (150-160 chars)
    - Identifies 5-8 high-value keywords
    - Ensures content is search-engine friendly
    - Balances SEO with readability"""
)


# ── Pipeline ──────────────────────────────────────────────────────────────────

def generate_blog_post(topic: str, tone: str = "professional yet friendly") -> BlogPost:
    """Generate a complete blog post using 4 AI agents in sequence."""
    print(f"\n\U0001f680 Starting AI Blog Post Generation")
    print(f"\U0001f4dd Topic: {topic}")
    print(f"\U0001f3a8 Tone: {tone}\n")

    # Phase 1 — Research
    print("\U0001f50d Phase 1: Researching topic...")
    research = marvin.run(
        f"Research the topic '{topic}'. Find key points, statistics, trending angles, "
        f"target audience insights, and credible sources.",
        agents=[researcher],
        result_type=ResearchFindings
    )
    print(f"\u2705 Research complete: {len(research.key_points)} key points found\n")

    # Phase 2 — Outline
    print("\U0001f4cb Phase 2: Creating content outline...")
    outline = marvin.run(
        f"Create a SHORT blog post outline about '{topic}' with a {tone} tone. "
        f"Structure 3-4 CONCISE main sections. Target: 500-800 words total.",
        agents=[strategist],
        result_type=ContentOutline,
        context={"research": research}
    )
    print(f"\u2705 Outline created: {outline.working_title}\n")

    # Phase 3 — Write
    print("\u270d\ufe0f  Phase 3: Writing content...")
    introduction = marvin.run(
        f"Write a SHORT, engaging introduction for '{outline.working_title}'. "
        f"Hook: {outline.hook}. 1-2 paragraphs ONLY. Tone: {tone}",
        agents=[writer],
        result_type=str,
        context={"outline": outline, "research": research}
    )

    sections = []
    for i, section in enumerate(outline.main_sections, 1):
        print(f"   Writing section {i}/{len(outline.main_sections)}: {section.title}")
        content = marvin.run(
            f"Write BRIEF content for section '{section.title}'. "
            f"Brief: {section.description}. Use 1 concrete example. Keep it SHORT. Tone: {tone}",
            agents=[writer],
            result_type=str,
            context={"research": research, "previous_sections": sections}
        )
        sections.append({"heading": section.title, "content": content})

    conclusion = marvin.run(
        f"Write a SHORT conclusion (1 paragraph). End with one actionable insight. Tone: {tone}",
        agents=[writer],
        result_type=str,
        context={"outline": outline, "sections": sections}
    )
    cta = marvin.run(
        f"Write a brief call-to-action. 1 sentence. Tone: {tone}",
        agents=[writer],
        result_type=str
    )
    print("\u2705 Writing complete\n")

    # Phase 4 — SEO
    print("\U0001f50d Phase 4: SEO optimization...")
    seo_title = marvin.run(
        f"Create an SEO-optimized title (max 60 chars) for: '{outline.working_title}'.",
        agents=[seo_optimizer], result_type=str
    )
    slug = marvin.run(
        f"Create a URL slug for: {seo_title}",
        agents=[seo_optimizer], result_type=str
    )
    meta_description = marvin.run(
        f"Write a meta description (150-160 chars). Key points: {', '.join(outline.key_takeaways[:3])}",
        agents=[seo_optimizer], result_type=str
    )
    keywords = marvin.run(
        f"List 5-8 SEO keywords for a blog post about '{topic}'",
        agents=[seo_optimizer], result_type=list[str]
    )
    print("\u2705 SEO complete\n")

    return BlogPost(
        title=seo_title, slug=slug, meta_description=meta_description,
        keywords=keywords, introduction=introduction, sections=sections,
        conclusion=conclusion, call_to_action=cta
    )


def save_blog_post(blog_post: BlogPost, output_dir: str = "generated_posts"):
    """Save blog post as Markdown and JSON."""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    md_content = f"""---
title: {blog_post.title}
slug: {blog_post.slug}
description: {blog_post.meta_description}
keywords: {', '.join(blog_post.keywords)}
date: {blog_post.created_at}
---

# {blog_post.title}

{blog_post.introduction}

"""
    for section in blog_post.sections:
        md_content += f"## {section['heading']}\n\n{section['content']}\n\n"
    md_content += f"## Conclusion\n\n{blog_post.conclusion}\n\n---\n\n**{blog_post.call_to_action}**\n"

    slug = blog_post.slug
    (output_path / f"{slug}.md").write_text(md_content, encoding="utf-8")
    (output_path / f"{slug}.json").write_text(blog_post.model_dump_json(indent=2), encoding="utf-8")

    print(f"\U0001f4be Saved: generated_posts/{slug}.md + .json\n")


def main():
    print("=" * 60)
    print("\U0001f916 MINDPULSE — AI Blog Generator")
    print("=" * 60)

    topic = input("\n\U0001f4ac Topic to write about: ")

    tone_options = {
        "1": "professional and informative",
        "2": "casual and friendly",
        "3": "enthusiastic and inspiring",
        "4": "authoritative and expert-level"
    }
    print("\n\U0001f3a8 Writing tone:")
    for k, v in tone_options.items():
        print(f"  {k}. {v.title()}")
    tone_choice = input("\nSelect (1-4) [default: 1]: ").strip() or "1"
    tone = tone_options.get(tone_choice, tone_options["1"])

    print("\n" + "=" * 60 + "\n")

    blog_post = generate_blog_post(topic, tone)
    save_blog_post(blog_post)

    print("=" * 60)
    print("\u2728 DONE!")
    print(f"\U0001f4cc Title:    {blog_post.title}")
    print(f"\U0001f517 Slug:     {blog_post.slug}")
    print(f"\U0001f50d Keywords: {', '.join(blog_post.keywords[:3])}...")
    print("\n\u25b6 Now run: python web_showcase.py  to view it in browser\n")


if __name__ == "__main__":
    main()
