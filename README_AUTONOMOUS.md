# 🌟 Autonomous AI Blog Generation System

> An AI-powered system that discovers trending topics, generates thoughtful blog posts, and showcases them on a beautiful website — completely automatically.

![Status](https://img.shields.io/badge/status-production%20ready-brightgreen)
![Python](https://img.shields.io/badge/python-3.11+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ What This Does

This isn't just a blog generator. It's a **fully autonomous content creation system** that:

1. **🔍 Discovers Trends** - AI analyzes what people are struggling with emotionally and identifies resonant topics
2. **✍️ Writes Blog Posts** - 4 specialized AI agents collaborate to create thoughtful, in-depth content
3. **🌐 Showcases Beautifully** - Displays posts on an aesthetic web interface (Substack/Medium style)
4. **⏰ Runs on Autopilot** - Schedule daily, weekly, or custom generation intervals

**Inspired by thoughtful creators like Kelly.today**, this system generates deeply personal, relatable content about modern life's challenges.

---

## 🎯 Quick Start (3 Commands)

```powershell
# 1. Discover a trending topic
python trend_monitor.py

# 2. Generate a blog post automatically
echo "1" | python auto_scheduler.py

# 3. View your beautiful blog
python web_showcase.py
# Open: http://localhost:5000
```

✅ **That's it!** Your first autonomous blog post is ready.

---

## 🚀 Features

### 1. **Trend Monitor Agent**
- Analyzes current social conversations and cultural moments
- Identifies emotionally resonant topics people are dealing with
- Focuses on universal human experiences (relationships, mental health, growth)
- Avoids generic self-help — finds deeply personal angles

**Example discovered topics:**
- "the quiet exhaustion of maintaining a cheerful facade while feeling overwhelmed"
- "finding peace when productivity feels like your worth"
- "why rest feels guilty when you're wired for achievement"
- "the discomfort of choosing yourself first"

### 2. **Multi-Agent Blog Generator**
- **Research Specialist**: Finds key points, statistics, credible sources
- **Content Strategist**: Creates compelling outline with 4-6 sections
- **Professional Writer**: Writes engaging, thoughtful content
- **SEO Optimizer**: Crafts titles, meta descriptions, keywords

**Output:**
- 2000-3000 word in-depth articles
- Structured sections with examples and insights
- SEO-optimized metadata
- Both Markdown (.md) and JSON formats

### 3. **Beautiful Web Showcase**
- Modern, responsive design (mobile/tablet/desktop)
- Elegant typography (Crimson Text + Inter fonts)
- Post cards with smooth hover effects
- Full reading view with proper spacing
- Reading time estimates and metadata
- Tag display and navigation

### 4. **Autonomous Scheduler**
- **One-time generation**: Generate a post on demand
- **Daily automation**: New post every day at 9 AM
- **Weekly automation**: Fresh content every Monday
- **Custom intervals**: Every N hours (your choice)

---

## 📸 Screenshots

### Home Page - Post Grid
```
┌────────────────────────────────────────────────────┐
│          Thoughts & Reflections                    │
│   Exploring life's quiet truths and moments        │
└────────────────────────────────────────────────────┘

┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Beautiful   │  │ Card-based  │  │ Grid layout │
│ post cards  │  │ design with │  │ responsive  │
│ with hover  │  │ titles and  │  │ and modern  │
│ effects     │  │ excerpts    │  │ styling     │
└─────────────┘  └─────────────┘  └─────────────┘
```

### Individual Post View
- Clean, readable typography
- Elegant serif fonts for body text
- Proper spacing and rhythm
- Tags and metadata
- Call-to-action at the end

---

## 📦 Installation

### Prerequisites
- Python 3.11+
- Free Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Setup

```powershell
# 1. Clone or download this project
cd altro

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API key to .env file
# Create/edit .env and add:
GOOGLE_API_KEY=your_api_key_here

# 4. Test the system
python trend_monitor.py
```

---

## 🎮 Usage

### Method 1: Quick Launch Menu (Easiest)

```powershell
.\launch.ps1
```

Choose from:
1. Generate one post now
2. View web showcase
3. Set up automation
4. Discover topics only
5. Manual generation

### Method 2: Individual Scripts

#### Discover Trending Topics
```powershell
python trend_monitor.py
```
- AI analyzes current trends
- Identifies emotionally resonant topic
- Logs to `trend_logs/` folder

#### Generate Blog Post (Autonomous)
```powershell
python auto_scheduler.py
# Choose option 1: Generate ONE blog post NOW
```
- Discovers topic automatically
- Selects tone (casual & friendly)
- Generates full blog post
- Saves to `generated_posts/`

#### View Web Showcase
```powershell
python web_showcase.py
# Open: http://localhost:5000
```
- Beautiful blog interface
- Responsive design
- All generated posts displayed

#### Set Up Automation
```powershell
python auto_scheduler.py
# Choose option 2: Daily at 9:00 AM
# Or option 3: Weekly on Mondays
# Or option 4: Custom interval
```

---

## 📁 Project Structure

```
altro/
├── 📄 Core Scripts
│   ├── trend_monitor.py          # AI trend discovery
│   ├── blog_generator.py         # Multi-agent content creation
│   ├── auto_scheduler.py         # Autonomous scheduler
│   └── web_showcase.py           # Beautiful web interface
│
├── 🎨 Web Interface
│   ├── templates/
│   │   ├── index.html            # Home page (post grid)
│   │   └── post.html             # Individual post view
│   └── static/css/
│       └── style.css             # Beautiful modern styling
│
├── 📝 Generated Content
│   ├── generated_posts/
│   │   ├── slug.md               # Markdown format
│   │   └── slug.json             # JSON metadata
│   └── trend_logs/
│       └── trend_log_YYYYMM.json # Discovery history
│
├── 🚀 Quick Launch
│   ├── launch.ps1                # PowerShell launcher
│   └── launch.bat                # Batch launcher
│
├── 📚 Documentation
│   ├── README.md                 # This file
│   ├── QUICKSTART.md             # 5-minute guide
│   ├── AUTONOMOUS_GUIDE.md       # Complete documentation
│   ├── START_HERE.md             # Original guide
│   └── ...other docs
│
└── ⚙️ Configuration
    ├── .env                      # API keys (keep private!)
    ├── .env.example              # Template
    ├── requirements.txt          # Python dependencies
    └── .gitignore                # Git ignore rules
```

---

## 🎨 Customization

### Change Writing Tone

Edit `auto_scheduler.py` line 53:
```python
tone_map = {
    "professional and informative": "1",
    "casual and friendly": "2",           # ← Default
    "enthusiastic and inspiring": "3",
    "authoritative and expert-level": "4"
}
```

### Change Trend Focus

Edit `trend_monitor.py` agent instructions:
```python
instructions="""...
Focus on:
- Your specific interests here
- Topics you want to explore
- Your target audience struggles
...
"""
```

### Customize Website Design

Edit `static/css/style.css`:
```css
:root {
    --bg-primary: #fafaf8;      /* Page background */
    --accent: #0066cc;           /* Links, buttons */
    --font-serif: 'Your Font';   /* Heading font */
}
```

### Change Scheduling

Edit `auto_scheduler.py`:
```python
# Change from 9 AM to 6 PM
schedule.every().day.at("18:00").do(generate_blog_post_automatically)

# Every 6 hours
schedule.every(6).hours.do(generate_blog_post_automatically)
```

---

## 🌟 Example Workflow

### Daily Content Creator

**Setup Once:**
```powershell
python auto_scheduler.py
# Choose option 2: Daily at 9:00 AM
# Leave terminal running
```

**What Happens Automatically:**
- 9:00 AM: AI discovers trending topic
- 9:01 AM: Multi-agent system generates blog post
- 9:04 AM: Post saved and visible on website
- Next day: Repeat!

### Weekly Content Batch

**Every Monday:**
```powershell
python auto_scheduler.py
# Choose option 3: Weekly on Mondays
```

**Result:**
- Fresh content every week
- No manual work required
- Consistent publishing schedule

---

## 💡 Tips & Best Practices

### 1. **Generate 3-5 Posts Before Launching Website**
Build up a content library first:
```powershell
python auto_scheduler.py  # Option 1
python auto_scheduler.py  # Option 1
python auto_scheduler.py  # Option 1
```

### 2. **Review First Few Posts**
Check tone and quality match your preferences, then let it run autonomous.

### 3. **Check Trend Logs**
See what topics are being discovered:
```powershell
# View: trend_logs/trend_log_202511.json
```

### 4. **Backup Your Posts**
Generated content is valuable — back up `generated_posts/` folder regularly.

### 5. **Monitor API Usage**
- Google Gemini Free: 1,500 requests/day, 60/min
- Each blog post ≈ 10-15 requests
- Can generate ~100 posts/day on free tier

---

## 🔧 Troubleshooting

### "No API key found"
→ Create `.env` file with: `GOOGLE_API_KEY=your_key`

### "Emoji encoding errors"
→ Use `launch.ps1` instead of running directly (handles UTF-8)

### "Posts not showing on website"
→ Check `generated_posts/` has both .md and .json files

### "Schedule not running"
→ Keep terminal window open (or use Windows Task Scheduler)

### "Import errors"
→ Run: `pip install -r requirements.txt`

---

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute getting started guide
- **[AUTONOMOUS_GUIDE.md](AUTONOMOUS_GUIDE.md)** - Complete system documentation
- **[API_COMPARISON.md](API_COMPARISON.md)** - Free API options comparison
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Multi-agent system design

---

## 🎯 Use Cases

### Personal Blog
- Generate thoughtful reflections daily
- Build a library of insightful content
- Share on Medium, Substack, your website

### Content Marketing
- Consistent blog publishing schedule
- SEO-optimized articles
- Trending topics automatically discovered

### Newsletter
- Weekly or daily content for subscribers
- Emotionally resonant topics
- Thoughtful, engaging writing

### Social Media
- Extract quotes from generated posts
- Share insights across platforms
- Drive traffic to full articles

---

## 🌐 Deployment Options

### Local Development
```powershell
python web_showcase.py
# Access at: http://localhost:5000
```

### Windows Service (24/7 Background)
```powershell
# Using NSSM (Non-Sucking Service Manager)
nssm install BlogAutomation python.exe auto_scheduler.py
nssm start BlogAutomation
```

### Production Server
- Deploy Flask app with Gunicorn/uWSGI
- Use Nginx as reverse proxy
- Set up systemd service for scheduler
- Configure SSL with Let's Encrypt

---

## 🤝 Contributing

This is a complete, production-ready system. Feel free to:
- Fork and customize for your needs
- Add new AI agents
- Enhance the web interface
- Create new scheduling options

---

## 📄 License

MIT License - Feel free to use commercially or personally

---

## 🙏 Acknowledgments

**Inspired by:**
- Kelly.today (thoughtful, relatable content style)
- Substack/Medium (clean, elegant design)
- ControlFlow/Marvin (multi-agent orchestration)

**Built with:**
- Marvin 3.0 (AI agent framework)
- Pydantic AI (type-safe AI interactions)
- Google Gemini (free LLM API)
- Flask (web framework)

---

## 📞 Support

**Having issues?**
1. Check documentation files
2. Review `trend_logs/` for discovery history
3. Verify API key in `.env` file
4. Test each component individually

---

## 🚀 Get Started Now

```powershell
# Generate your first autonomous blog post!
python auto_scheduler.py
# Choose option 1

# View it on your beautiful website
python web_showcase.py
# Open: http://localhost:5000
```

**Your AI-powered blog awaits! ✨**

---

Made with ❤️ and AI • Fully autonomous • Production ready
