# 🚀 Autonomous Blog Generation System

## Overview

A fully autonomous AI-powered blog generation system that:
- 🔍 **Discovers trending topics** by analyzing internet trends and human conversations
- ✍️ **Generates blog posts automatically** using multi-agent AI orchestration
- 🌐 **Showcases posts beautifully** with an aesthetic web interface
- ⏰ **Runs on autopilot** with flexible scheduling options

Inspired by thoughtful content creators like Kelly.today, this system creates deeply personal, relatable reflections on modern life.

---

## ✨ Features

### 1. **Trend Monitor Agent** (`trend_monitor.py`)
- Analyzes current social conversations and human struggles
- Identifies emotionally resonant topics people are dealing with
- Focuses on universal experiences: relationships, mental health, personal growth
- Thinks like thoughtful Medium/Substack writers

### 2. **Autonomous Scheduler** (`auto_scheduler.py`)
- Generate blogs on-demand or on schedule
- Daily, weekly, or custom interval automation
- Fully automatic: discovers topic → generates post → saves to showcase
- No manual input required!

### 3. **Beautiful Web Showcase** (`web_showcase.py`)
- Modern, aesthetic interface (Substack/Medium style)
- Responsive design with beautiful typography
- Post cards with hover effects
- Full post view with elegant reading experience
- Tags, metadata, and reading time estimates

### 4. **Multi-Agent Blog Generator** (`blog_generator.py`)
- 4 specialized AI agents working together
- Free API support (Google Gemini/Groq)
- Structured output (Markdown + JSON)
- SEO optimized content

---

## 🎯 Quick Start

### Option 1: Generate ONE Post Now (Autonomous)

```powershell
# Discover trending topic and generate blog automatically
python auto_scheduler.py
# Choose option 1: Generate ONE blog post NOW
```

### Option 2: View Your Beautiful Blog Showcase

```powershell
# Start the web server
python web_showcase.py

# Open browser to: http://localhost:5000
```

### Option 3: Set Up Daily Automation

```powershell
# Run the scheduler
python auto_scheduler.py
# Choose option 2: Schedule DAILY generation (every day at 9:00 AM)
```

---

## 📋 Detailed Usage

### Manual Workflow (Step by Step)

**Step 1: Discover Trending Topic**
```powershell
python trend_monitor.py
```
- AI analyzes current trends
- Identifies emotionally resonant topic
- Saves to `trend_logs/` folder
- Example output: "the art of setting boundaries without guilt"

**Step 2: Generate Blog Post**
```powershell
python blog_generator.py
```
- Enter the topic (or press Enter to be prompted)
- Choose tone: Casual and Friendly (option 2)
- Wait 2-3 minutes for generation
- Post saved to `generated_posts/` folder

**Step 3: View on Website**
```powershell
python web_showcase.py
```
- Browse to http://localhost:5000
- See your beautiful blog posts
- Click any post to read full content

### Autonomous Workflow (Set It and Forget It!)

**Run the Auto Scheduler:**
```powershell
python auto_scheduler.py
```

**Choose Your Mode:**
```
1. Generate ONE blog post NOW
   → Runs immediately, discovers topic + generates post

2. Schedule DAILY generation (every day at 9:00 AM)
   → Runs every day automatically

3. Schedule WEEKLY generation (every Monday at 9:00 AM)
   → Runs every Monday automatically

4. Custom interval (every N hours)
   → You choose: every 6 hours, 12 hours, etc.
```

**What Happens Automatically:**
1. 🔍 Trend Monitor discovers what people are struggling with
2. 🎨 Selects appropriate tone (casual & friendly by default)
3. ✍️ Blog Generator creates full post with 4 AI agents
4. 💾 Saves Markdown + JSON to `generated_posts/`
5. 🌐 Post automatically appears on web showcase!

---

## 🎨 The Tone & Style

The system is configured to match the thoughtful, relatable style of your inspiration images:

**Tone Characteristics:**
- ✨ Casual and friendly (conversational, approachable)
- 💭 Deeply personal yet universally relatable
- 🌱 Reflective and thought-provoking
- 💙 Empathetic to real human struggles

**Topic Examples:**
- "discomfort is the price you pay for a fulfilling life"
- "the quiet grief of outgrowing friendships"
- "when productivity culture makes you forget how to rest"
- "learning to be okay with being misunderstood"
- "social comparison is driving us to despair—it doesn't have to"

**Content Style:**
- Opens with relatable hook
- Explores emotional nuances
- Shares insights without preaching
- Ends with gentle encouragement
- 2000-3000 words, in-depth exploration

---

## 📁 Project Structure

```
altro/
├── blog_generator.py        # Multi-agent blog generation
├── trend_monitor.py         # AI trend discovery agent
├── auto_scheduler.py        # Autonomous scheduling system
├── web_showcase.py          # Beautiful web interface
├── requirements.txt         # Python dependencies
├── .env                     # API keys (GOOGLE_API_KEY)
│
├── generated_posts/         # Your generated blog posts
│   ├── post-slug.md         # Markdown version
│   └── post-slug.json       # JSON metadata
│
├── trend_logs/              # Discovered trends log
│   └── trend_log_202511.json
│
├── templates/               # Web interface templates
│   ├── index.html           # Home page (post grid)
│   └── post.html            # Individual post view
│
└── static/css/              # Styling
    └── style.css            # Beautiful modern design
```

---

## 🎯 How It Works (Under the Hood)

### Trend Discovery Process

1. **AI Analysis**: The Trend Monitor agent thinks like a thoughtful content creator
2. **Current Context**: Considers today's date, seasonal themes, cultural moments
3. **Human Struggles**: Identifies what people are genuinely dealing with
4. **Emotional Resonance**: Chooses topics that make readers feel seen
5. **Topic Selection**: Returns 5-12 word phrase (e.g., "why rest feels guilty in hustle culture")

### Blog Generation Process

1. **Research Phase**: Agent researches topic, finds key points, trends
2. **Strategy Phase**: Agent creates content outline with 4-6 sections
3. **Writing Phase**: Agent writes introduction, sections, conclusion, CTA
4. **SEO Phase**: Agent optimizes title, meta description, keywords
5. **Output**: Saves beautifully formatted Markdown + structured JSON

### Web Showcase Features

- **Home Page**: Grid of post cards with hover effects
- **Post View**: Full post with elegant typography
- **Responsive**: Looks great on mobile, tablet, desktop
- **Reading Time**: Calculates estimated reading time
- **Tags**: Shows keywords as clickable tags
- **Typography**: Serif headings (Crimson Text) + Sans body (Inter)

---

## ⚙️ Configuration

### API Keys (.env file)

```bash
# Google Gemini (Free - 1500 requests/day)
GOOGLE_API_KEY=your_key_here

# Groq (Free backup - 14,400 requests/day)
GROQ_API_KEY=your_key_here
```

### Scheduling Times

Edit `auto_scheduler.py` to change default times:

```python
# Daily at 9 AM
schedule.every().day.at("09:00").do(generate_blog_post_automatically)

# Change to 6 PM
schedule.every().day.at("18:00").do(generate_blog_post_automatically)

# Every 6 hours
schedule.every(6).hours.do(generate_blog_post_automatically)
```

### Tone Preferences

The system defaults to "casual and friendly" (like your inspiration). To change:

Edit `auto_scheduler.py` line 53:
```python
tone_map = {
    "professional and informative": "1",
    "casual and friendly": "2",           # ← Default
    "enthusiastic and inspiring": "3",
    "authoritative and expert-level": "4"
}
```

---

## 🚀 Installation

```powershell
# 1. Install dependencies
pip install -r requirements.txt

# 2. Add your API key to .env
# Get free key: https://makersuite.google.com/app/apikey

# 3. Test the trend monitor
python trend_monitor.py

# 4. Test blog generation (manual)
python blog_generator.py

# 5. Start autonomous generation!
python auto_scheduler.py
```

---

## 💡 Usage Examples

### Example 1: Morning Routine Automation

```powershell
# Set up daily 9 AM generation
python auto_scheduler.py
# Choose option 2

# Leave computer running
# Every morning at 9 AM: new blog post appears!
```

### Example 2: Weekend Content Batch

```powershell
# Generate 3 posts in a row
python auto_scheduler.py
# Choose option 1 (three times)

# Start web showcase
python web_showcase.py

# Browse all posts at http://localhost:5000
```

### Example 3: Discover Topic, Write Later

```powershell
# Just discover topics (save for later)
python trend_monitor.py
python trend_monitor.py
python trend_monitor.py

# Check trend_logs/ folder for ideas

# Later: generate blog with specific topic
python blog_generator.py
# Paste one of the discovered topics
```

---

## 🎨 Customization

### Change Web Design Colors

Edit `static/css/style.css`:

```css
:root {
    --bg-primary: #fafaf8;      /* Page background */
    --bg-secondary: #ffffff;     /* Card background */
    --text-primary: #1a1a1a;     /* Main text */
    --accent: #0066cc;           /* Links, buttons */
}
```

### Change Trend Focus

Edit `trend_monitor.py` instructions:

```python
instructions="""You are an expert trend analyst...

Focus on:
- Tech and startups  ← Add your focus
- Career transitions
- Remote work culture
...
"""
```

### Change Post Length

Edit `blog_generator.py` prompts:

```python
# Currently: "Write 3-4 well-developed paragraphs"
# Change to: "Write 5-6 detailed paragraphs with examples"
```

---

## 📊 Output Examples

### Generated Post Structure

**Markdown File** (`generated_posts/topic-slug.md`):
```markdown
---
title: The Art of Setting Boundaries Without Guilt
slug: boundaries-without-guilt
description: Learn to protect your energy and time...
keywords: [boundaries, self-care, people-pleasing]
---

# The Art of Setting Boundaries Without Guilt

[Full post content with sections, examples, insights]
```

**JSON File** (`generated_posts/topic-slug.json`):
```json
{
  "title": "The Art of Setting Boundaries Without Guilt",
  "slug": "boundaries-without-guilt",
  "meta_description": "Learn to protect your energy...",
  "keywords": ["boundaries", "self-care"],
  "word_count": 2347,
  "sections": [...]
}
```

**Web Showcase** (http://localhost:5000):
- Beautiful card on home page
- Click → Full post with elegant typography
- Tags, reading time, formatted date

---

## 🔧 Troubleshooting

### "No API key found"
→ Add `GOOGLE_API_KEY=your_key` to `.env` file

### "Scheduler not running"
→ Keep terminal window open (or use `nohup` on Linux/Mac)

### "Posts not showing on website"
→ Check `generated_posts/` folder has .md and .json files

### "Import error: no module named flask"
→ Run `pip install -r requirements.txt`

### "Trend monitor returns generic topics"
→ The AI is context-aware; results vary. Run multiple times for best topic.

---

## 🌟 What Makes This Special

1. **Truly Autonomous**: No manual topic research needed
2. **Emotionally Intelligent**: AI understands human struggles
3. **Beautiful Output**: Professional-grade web design
4. **Free to Run**: Uses free API tiers
5. **Flexible**: Run once, daily, weekly, or custom schedule
6. **Production Ready**: Complete system, not just a script

---

## 📝 Best Practices

1. **Run Trend Monitor First**: Test it a few times to see topic quality
2. **Review First Post**: Check tone/style matches your preference
3. **Start with Weekly**: Before going daily, test weekly generation
4. **Check Logs**: Monitor `trend_logs/` to see discovered topics
5. **Backup Posts**: Generated posts are valuable—back them up!
6. **Customize**: Tweak prompts and styling to match your voice

---

## 🎁 Bonus: Run as Windows Service

To run 24/7 in the background:

```powershell
# Install NSSM (Non-Sucking Service Manager)
# Download from: https://nssm.cc/download

# Create service
nssm install BlogAutomation "C:\Path\To\Python.exe" "C:\Path\To\auto_scheduler.py"

# Start service
nssm start BlogAutomation
```

---

## 🚀 Next Steps

1. **Test the system**:
   ```powershell
   python auto_scheduler.py
   # Choose option 1
   ```

2. **View your first post**:
   ```powershell
   python web_showcase.py
   # Browse to http://localhost:5000
   ```

3. **Set up automation**:
   ```powershell
   python auto_scheduler.py
   # Choose option 2 (daily) or 3 (weekly)
   ```

4. **Enjoy**! Your blog now writes itself 🎉

---

## 📞 Support

If you encounter issues:
1. Check `trend_logs/` for trend discovery logs
2. Check `generated_posts/` for output files
3. Review terminal output for error messages
4. Ensure API keys are valid and have quota remaining

---

**Happy Automated Blogging! ✨**

Your AI-powered content creation system is ready to go!
