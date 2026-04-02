# MindPulse Blog 🧠

> AI-powered blog that **researches, writes, and SEO-optimizes** posts automatically using a 4-agent pipeline.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/harsh686/mindpulse-blog)

---

## How It Works

When you run the generator, 4 specialized AI agents work in sequence:

```
1. 🔍 Research Agent    → gathers key points, stats, trends on your topic
2. 📋 Strategy Agent   → creates a concise 3-4 section outline (500-800 words)
3. ✍️  Writer Agent     → writes intro, each section, conclusion, and CTA
4. 📈 SEO Agent        → optimizes title, slug, meta description, keywords
```

Each post is saved as `.md` + `.json` in `generated_posts/`, then displayed by the Flask web server.

---

## Quick Start (GitHub Codespaces — No Local Install)

**1.** Click **"Open in GitHub Codespaces"** above  
**2.** Wait ~2 min for the environment to build  
**3.** In the terminal:

```bash
# Copy the config template
cp .env.example .env

# Open .env and add your API key (see below for where to get one)
nano .env
```

**4.** Generate a blog post:
```bash
python blog_generator.py
```

**5.** View the blog in your browser:
```bash
python web_showcase.py
# → Codespaces auto-opens a preview at localhost:5000
```

---

## API Key Setup

You need **one** of these (all have free tiers):

| Provider | Where to get key | Speed | Quality |
|----------|-----------------|-------|----------|
| **NVIDIA Build** ⭐ | [build.nvidia.com](https://build.nvidia.com) → any model → "Get API Key" | Fast | Excellent (Llama 4 Maverick) |
| **Google Gemini** | [aistudio.google.com](https://aistudio.google.com/app/apikey) | Fast | Excellent |
| **Groq** | [console.groq.com/keys](https://console.groq.com/keys) | Very fast | Good |
| **OpenAI** | [platform.openai.com](https://platform.openai.com) | Fast | Excellent (paid) |

Add your key to `.env`:

```bash
# For NVIDIA (recommended — free)
NVIDIA_API_KEY=nvapi-your-key-here

# Or for Google Gemini
# GOOGLE_API_KEY=your-key-here

# Or for Groq
# GROQ_API_KEY=your-key-here
```

> ⚠️ Never commit your `.env` file — it's already in `.gitignore`.

---

## Local Setup

```bash
git clone https://github.com/harsh686/mindpulse-blog.git
cd mindpulse-blog

pip install -r requirements.txt

cp .env.example .env
# Edit .env and add your API key

python blog_generator.py   # generate a post
python web_showcase.py     # view at http://localhost:5000
```

---

## Project Structure

```
mindpulse-blog/
├── blog_generator.py     # Core: 4-agent AI pipeline
├── web_showcase.py       # Flask web server (blog UI)
├── auto_scheduler.py     # Auto-generate posts on a schedule
├── trend_monitor.py      # Monitor trending topics
│
├── templates/            # HTML templates (Jinja2)
│   ├── index.html        # Blog homepage (post grid)
│   └── post.html         # Individual post page
│
├── static/
│   └── style.css         # Dark-mode blog stylesheet
│
├── generated_posts/      # Your AI-written blog posts (.md + .json)
├── api/index.py          # WSGI entry point
│
├── .devcontainer/        # GitHub Codespaces config
├── .env.example          # API key template
├── requirements.txt      # Python dependencies
└── .gitignore
```

---

## Auto-Publishing (Optional)

To auto-generate posts on a schedule using GitHub Actions, add your API key as a repository secret:

```
Settings → Secrets and variables → Actions → New repository secret
Name: NVIDIA_API_KEY
Value: nvapi-your-key-here
```

The `.github/workflows/daily-blog.yml` workflow will then run automatically.

---

## Tech Stack

- **[Marvin](https://www.askmarvin.ai/)** — Multi-agent AI orchestration
- **Flask** — Web server
- **Pydantic** — Structured data models for AI output
- **python-dotenv** — Environment config
