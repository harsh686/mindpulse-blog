"""
AI Blog Post Generator using Marvin
A multi-agent system that orchestrates specialized AI agents to research,
plan, write, and optimize blog posts.

Uses FREE LLM APIs: Google Gemini or Groq
"""

import marvin
from pydantic import BaseModel, Field
from datetime import datetime
from pathlib import Path
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from dotenv import dotenv_values


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


def get_model_config():
    """
    Detect which LLM to use. Priority:
      1. GOOGLE key in .env (Gemini)
      2. GROQ key in .env
      3. GOOGLE env var
      4. GROQ env var
      5. OPENAI env var (if present)
    """
    # Read .env values if present and normalize keys (strip BOM if present)
    raw_env = dotenv_values(".env") if Path(".env").exists() else {}
    env_values = { (k.lstrip('\ufeff') if isinstance(k, str) else k): v for k, v in raw_env.items() }

    # 1. Prefer Google Gemini from .env
    if env_values.get("GOOGLE_API_KEY"):
        google_key = env_values.get("GOOGLE_API_KEY")
        if google_key:
            os.environ["GOOGLE_API_KEY"] = google_key
        print("\ud83e\udd16 Using: Google Gemini (Free & Fast)")
        print("\ud83d\udce6 Model: gemini-2.0-flash\n")
        return "gemini/gemini-2.0-flash"

    # 2. Try GROQ from .env
    if env_values.get("GROQ_API_KEY"):
        groq_key = env_values.get("GROQ_API_KEY")
        if groq_key:
            os.environ["GROQ_API_KEY"] = groq_key
        groq_model = env_values.get("GROQ_MODEL") or os.getenv("GROQ_MODEL") or "llama-3.3-70b-versatile"
        print("\ud83e\udd16 Using: Groq (Free & Fast) \u2014 chosen from .env")
        print(f"\ud83d\udce6 Model: {groq_model}\n")
        return f"groq/{groq_model}"

    # 3. Then GOOGLE from environment
    if os.getenv("GOOGLE_API_KEY"):
        print("\ud83e\udd16 Using: Google Gemini (Free & Fast) \u2014 from environment")
        print("\ud83d\udce6 Model: gemini-2.0-flash\n")
        return "gemini/gemini-2.0-flash"

    # 4. Then GROQ from environment
    if os.getenv("GROQ_API_KEY"):
        groq_model = os.getenv("GROQ_MODEL") or "llama-3.3-70b-versatile"
        print("\ud83e\udd16 Using: Groq (Free & Fast) \u2014 chosen from environment")
        print(f"\ud83d\udce6 Model: {groq_model}\n")
        return f"groq/{groq_model}"

    # 5. Fall back to OpenAI if provided
    if env_values.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY"):
        openai_key = env_values.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
        if openai_key:
            os.environ["OPENAI_API_KEY"] = openai_key
        print("\ud83e\udd16 Using: OpenAI GPT \u2014 detected API key")
        print("\ud83d\udce6 Model: GPT-4o Mini\n")
        return "openai:gpt-4o-mini"

    # Nothing available
    raise ValueError(
        "\u274c No supported API key found. Please add one to your .env:\n"
        "  \u2022 GOOGLE_API_KEY (Gemini - free): https://aistudio.google.com/app/apikey\n"
        "  \u2022 GROQ_API_KEY (free): https://console.groq.com/keys\n"
    )


# Get the model string
MODEL = get_model_config()

# Create specialized agents with the configured model
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
    - Creates scannable content with good pacing
    - Writes at a 7th-9th grade reading level for accessibility
    - IMPORTANT: Keep each section brief (1-2 short paragraphs max)

    Write naturally and engagingly, as if explaining to a smart friend. Be concise."""
)

seo_optimizer = marvin.Agent(
    name="SEO Specialist",
    model=MODEL,
    instructions="""You are an SEO expert who:
    - Optimizes titles for click-through rate
    - Creates compelling meta descriptions
    - Identifies high-value keywords
    - Ensures content is search-engine friendly
    - Balances SEO with readability

    Make content discoverable without sacrificing quality."""
)


def generate_blog_post(topic: str, tone: str = "professional yet friendly") -> BlogPost:
    """
    Generate a complete, high-quality blog post using multiple AI agents.

    Args:
        topic: The blog post topic
        tone: Writing tone (default: "professional yet friendly")

    Returns:
        BlogPost: Complete structured blog post
    """
    print(f"\n\ud83d\ude80 Starting AI Blog Post Generation")
    print(f"\ud83d\udcdd Topic: {topic}")
    print(f"\ud83c\udfa8 Tone: {tone}\n")

    # TASK 1: Research Phase
    print("\ud83d\udd0d Phase 1: Researching topic...")
    research = marvin.run(
        f"Research the topic '{topic}'. Find key points, statistics, trending angles, "
        f"target audience insights, and credible sources. Be thorough and current.",
        agents=[researcher],
        result_type=ResearchFindings
    )
    print(f"\u2705 Research complete: {len(research.key_points)} key points found\n")

    # TASK 2: Strategic Planning
    print("\ud83d\udccb Phase 2: Creating content outline...")
    outline = marvin.run(
        f"Create a SHORT blog post outline about '{topic}' with a {tone} tone. "
        f"Use research findings to structure 3-4 CONCISE main sections. Target: 500-800 words total.",
        agents=[strategist],
        result_type=ContentOutline,
        context={"research": research}
    )
    print(f"\u2705 Outline created: {outline.working_title}\n")

    # TASK 3: Content Writing
    print("\u270d\ufe0f  Phase 3: Writing blog post content...")

    # Write introduction
    introduction = marvin.run(
        f"Write a SHORT, engaging introduction for '{outline.working_title}'. "
        f"Hook: {outline.hook}. Make it 1-2 paragraphs ONLY. Be concise. "
        f"Tone: {tone}",
        agents=[writer],
        result_type=str,
        context={"outline": outline, "research": research}
    )

    # Write main sections
    sections = []
    for i, section in enumerate(outline.main_sections, 1):
        print(f"   Writing section {i}/{len(outline.main_sections)}: {section.title}")
        content = marvin.run(
            f"Write BRIEF content for section: {section.title}. "
            f"Brief: {section.description}. "
            f"Use 1 concrete example. Keep it SHORT. "
            f"Tone: {tone}",
            agents=[writer],
            result_type=str,
            context={"research": research, "previous_sections": sections}
        )
        # FIX: this line was incorrectly outdented (was outside the for loop)
        sections.append({"heading": section.title, "content": content})

    # Write conclusion
    conclusion = marvin.run(
        f"Write a SHORT conclusion (1 paragraph only). "
        f"End with one actionable insight. Be concise. Tone: {tone}",
        agents=[writer],
        result_type=str,
        context={"outline": outline, "sections": sections}
    )

    # Create call to action
    cta = marvin.run(
        f"Write a brief call-to-action. 1 sentence. Tone: {tone}",
        agents=[writer],
        result_type=str
    )

    print("\u2705 Content writing complete\n")

    # TASK 4: SEO Optimization
    print("\ud83d\udd0d Phase 4: Optimizing for SEO...")

    seo_title = marvin.run(
        f"Create an SEO-optimized title (max 60 chars) based on '{outline.working_title}'. "
        f"Make it click-worthy while accurately describing the content.",
        agents=[seo_optimizer],
        result_type=str
    )

    slug = marvin.run(
        f"Create a URL slug for the title: {seo_title}",
        agents=[seo_optimizer],
        result_type=str
    )

    meta_description = marvin.run(
        f"Write a meta description (150-160 chars) that summarizes the blog post and "
        f"encourages clicks. Use key points: {', '.join(outline.key_takeaways[:3])}",
        agents=[seo_optimizer],
        result_type=str
    )

    keywords = marvin.run(
        f"Identify 5-8 relevant SEO keywords for this blog post about '{topic}'",
        agents=[seo_optimizer],
        result_type=list[str]
    )

    print("\u2705 SEO optimization complete\n")

    # Assemble final blog post
    blog_post = BlogPost(
        title=seo_title,
        slug=slug,
        meta_description=meta_description,
        keywords=keywords,
        introduction=introduction,
        sections=sections,
        conclusion=conclusion,
        call_to_action=cta
    )

    return blog_post


def save_blog_post(blog_post: BlogPost, output_dir: str = "generated_posts"):
    """
    Save the blog post as Markdown and JSON files.

    Args:
        blog_post: The BlogPost to save
        output_dir: Directory to save files in
    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # Save as Markdown
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

    md_content += f"## Conclusion\n\n{blog_post.conclusion}\n\n"
    md_content += f"---\n\n**{blog_post.call_to_action}**\n"

    md_file = output_path / f"{blog_post.slug}.md"
    md_file.write_text(md_content, encoding="utf-8")

    # Save as JSON
    json_file = output_path / f"{blog_post.slug}.json"
    json_file.write_text(blog_post.model_dump_json(indent=2), encoding="utf-8")

    print(f"\ud83d\udcbe Blog post saved:")
    print(f"   \ud83d\udcc4 Markdown: {md_file}")
    print(f"   \ud83d\udcca JSON: {json_file}\n")


def main():
    """Main function to run the blog generator"""
    print("=" * 70)
    print("\ud83e\udd16 AI BLOG POST GENERATOR - Powered by Multi-Agent Orchestration")
    print("=" * 70)

    topic = input("\n\ud83d� What topic should I write about? ")

    tone_options = {
        "1": "professional and informative",
        "2": "casual and friendly",
        "3": "enthusiastic and inspiring",
        "4": "authoritative and expert-level"
    }

    print("\n\ud83c\udfa8 Choose a writing tone:")
    for key, value in tone_options.items():
        print(f"   {key}. {value.title()}")

    tone_choice = input("\nSelect (1-4) [default: 1]: ").strip() or "1"
    tone = tone_options.get(tone_choice, tone_options["1"])

    print("\n" + "=" * 70 + "\n")

    blog_post = generate_blog_post(topic, tone)
    save_blog_post(blog_post)

    print("=" * 70)
    print("\u2728 BLOG POST GENERATION COMPLETE!")
    print("=" * 70)
    print(f"\n\ud83d\udccc Title: {blog_post.title}")
    print(f"\ud83d� Slug: {blog_post.slug}")
    print(f"\ud83d\udcca Keywords: {', '.join(blog_post.keywords[:3])}...")
    print("\nYour blog post is ready to publish! \ud83c\udf89\n")


if __name__ == "__main__":
    main()
