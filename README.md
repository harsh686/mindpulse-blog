# AI Blog Post Generator 🤖✍️

A powerful multi-agent AI system that generates high-quality blog posts using specialized AI agents for research, strategy, writing, and SEO optimization.

## � 100% FREE - No Paid APIs Required!

Uses **Google Gemini** or **Groq** - both have generous free tiers with no credit card required!

## �🌟 Features

- **Multi-Agent Orchestration**: Specialized AI agents work together like a real content team
  - 🔍 **Research Specialist**: Gathers current information, statistics, and insights
  - 📋 **Content Strategist**: Creates engaging outlines and narrative structures  
  - ✍️ **Professional Writer**: Crafts clear, engaging content
  - 🔍 **SEO Specialist**: Optimizes for search engines and discoverability

- **Structured Output**: Generate blog posts with proper structure:
  - SEO-optimized titles and meta descriptions
  - Well-organized sections with headings
  - Engaging introduction and conclusion
  - Call-to-action
  - Keywords and metadata

- **Multiple Formats**: Saves posts as both Markdown (.md) and JSON (.json)

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- A FREE API key from Google Gemini or Groq (no credit card needed!)

### Automated Setup (Recommended - Windows)

Just run this one command:
```powershell
.\setup.ps1
```

The wizard will:
- ✅ Install all dependencies
- ✅ Help you get a free API key
- ✅ Configure everything
- ✅ Run the generator

### Manual Setup (Any OS)

1. **Install dependencies**:
```bash
pip install marvin python-dotenv google-generativeai groq
```

2. **Get a FREE API key** (choose one):
   - **Google Gemini** (recommended): https://makersuite.google.com/app/apikey
   - **Groq** (fast): https://console.groq.com/keys

3. **Set your API key**:
```bash
# Windows PowerShell
$env:GOOGLE_API_KEY="your-key-here"

# Linux/Mac
export GOOGLE_API_KEY="your-key-here"

# Or create .env file
echo "GOOGLE_API_KEY=your-key-here" > .env
```

4. **Run the generator**:
```bash
python blog_generator.py
```

👉 **Detailed setup:** See [FREE_SETUP.md](FREE_SETUP.md) for complete instructions

## 📖 Usage

1. Run the script:
   ```bash
   python blog_generator.py
   ```

2. Enter your blog topic when prompted:
   ```
   💭 What topic should I write about? The Future of AI in Healthcare
   ```

3. Choose a writing tone:
   ```
   🎨 Choose a writing tone:
      1. Professional and Informative
      2. Casual and Friendly
      3. Enthusiastic and Inspiring
      4. Authoritative and Expert-Level
   ```

4. Watch the magic happen! The system will:
   - Research your topic
   - Create an outline
   - Write the full blog post
   - Optimize for SEO

5. Find your generated blog post in the `generated_posts/` directory

## 📂 Output Structure

Generated files are saved in `generated_posts/`:

```
generated_posts/
├── future-of-ai-in-healthcare.md    # Markdown format for publishing
└── future-of-ai-in-healthcare.json  # Structured JSON data
```

### Markdown Format
Perfect for publishing on platforms like:
- Jekyll, Hugo, or other static site generators
- WordPress (import as HTML)
- Medium, Dev.to, Hashnode
- Custom blog systems

### JSON Format
Contains structured data:
```json
{
  "title": "The Future of AI in Healthcare: 5 Game-Changing Trends",
  "slug": "future-of-ai-in-healthcare",
  "meta_description": "Discover how AI is transforming healthcare...",
  "keywords": ["AI healthcare", "medical AI", ...],
  "sections": [...],
  "word_count": 1523
}
```

## 🎯 How It Works

The system uses **multi-agent orchestration** - multiple specialized AI agents working together in a coordinated workflow:

```
1. Research Agent
   └─> Gathers information, statistics, trending topics
       ↓
2. Strategy Agent  
   └─> Creates compelling outline and structure
       ↓
3. Writing Agent
   └─> Writes introduction, sections, conclusion
       ↓
4. SEO Agent
   └─> Optimizes title, meta description, keywords
       ↓
5. Final Blog Post ✨
```

All agents share context through a **Thread**, ensuring consistency and coherence.

## 🛠️ Customization

### Change the LLM Provider

Marvin supports multiple providers:

```python
from pydantic_ai.models.anthropic import AnthropicModel

# Use Claude instead of OpenAI
writer = marvin.Agent(
    name="Writer",
    model=AnthropicModel("claude-3-5-sonnet-latest"),
    instructions="..."
)
```

### Adjust Agent Instructions

Modify agent personalities in the code:

```python
writer = marvin.Agent(
    name="Professional Writer",
    instructions="""You are a skilled blog writer who:
    - Your custom instructions here
    - Add more guidelines
    - Modify the style
    """
)
```

### Change Output Length

Adjust section writing prompts:

```python
# For longer content
content = marvin.run(
    f"Write 5-7 well-developed paragraphs...",  # Changed from 3-4
    ...
)
```

## 📋 Example Output

Here's what a generated blog post looks like:

```markdown
---
title: 10 AI Trends That Will Shape 2025: A Complete Guide
slug: ai-trends-2025-complete-guide  
description: Explore the top 10 AI trends transforming industries in 2025...
keywords: AI trends, artificial intelligence 2025, machine learning...
---

# 10 AI Trends That Will Shape 2025: A Complete Guide

Artificial intelligence isn't just changing technology—it's reshaping how we live, 
work, and interact with the world around us...

## 1. Multimodal AI Models Go Mainstream

Content here...

## Conclusion

The AI landscape in 2025 promises unprecedented innovation...

---

**Ready to stay ahead of AI trends? Subscribe to our newsletter...**
```

## 🤖 Powered By

- **[Marvin](https://github.com/prefecthq/marvin)** - Multi-agent orchestration framework (successor to ControlFlow)
- **[Pydantic AI](https://ai.pydantic.dev/)** - Type-safe AI framework
- **[Google Gemini](https://ai.google.dev/)** - Free, powerful LLM (default)
- **[Groq](https://groq.com/)** - Lightning-fast free alternative

## 🎓 Why Multi-Agent Orchestration?

Traditional single-prompt blog generation often produces:
- Generic, surface-level content
- Inconsistent quality
- Poor structure
- Weak SEO

Our multi-agent approach:
- ✅ Specializes each step with expert agents
- ✅ Maintains context across the entire workflow
- ✅ Produces structured, consistent output
- ✅ Balances creativity with optimization

## 🔮 Future Enhancements

Possible improvements:
- [ ] Web scraping for real-time research
- [ ] Image generation for blog post visuals
- [ ] Competitor analysis integration
- [ ] Multi-language support
- [ ] Content calendar planning
- [ ] Social media post generation
- [ ] Interactive CLI with rich formatting

## 📝 License

MIT License - Feel free to use and modify!

## 🙏 Credits

Built with ❤️ using Marvin, the spiritual successor to ControlFlow.

---

**Ready to generate amazing blog posts? Get started now!** 🚀
