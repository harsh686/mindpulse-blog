# ⚡ START HERE - 3 Minute Setup

## 🎯 Your Mission: Generate Your First AI Blog Post

### ⏱️ Time Required: 3 minutes
### 💰 Cost: $0 (completely free!)
### 🎓 Skill Level: Beginner-friendly

---

## 📋 Step-by-Step (Copy & Paste)

### 1️⃣ Open PowerShell
Press `Windows Key + X`, then click **"Windows PowerShell"**

---

### 2️⃣ Navigate to Project Folder
```powershell
cd "c:\Users\Harshvardhan singh\Documents\Workspace\altro"
```

---

### 3️⃣ Run the Setup Wizard (Easiest Way!)
```powershell
.\setup.ps1
```

**The wizard will:**
- ✅ Install everything you need
- ✅ Help you get a free API key
- ✅ Configure the project
- ✅ Run the generator

**Just follow the prompts!**

---

## 🎬 What Will Happen

```
========================================
  AI Blog Post Generator - Setup Wizard
========================================

Step 1: Checking Python...
✅ Python 3.x found

Step 2: Installing dependencies...
✅ Dependencies installed successfully!

Step 3: Checking for API keys...
⚠️  No API key found!

Choose a FREE option:
  1. Google Gemini (Recommended)
  2. Groq (Fast & Free)

Select option (1 or 2): 1

🌐 Opening Google AI Studio...
(Browser opens to get your key)

Paste your Google Gemini API key here: [paste your key]
✅ API key saved to .env file

========================================
  ✨ Setup Complete!
========================================

Would you like to run the blog generator now? (y/n): y

🤖 Using: Google Gemini (Free Tier)

💭 What topic should I write about? 
```

---

## 🌟 If You Want Manual Setup

### Install Dependencies:
```powershell
pip install marvin python-dotenv google-generativeai groq
```

### Get Free API Key:
**Option 1: Google Gemini** (Recommended)
1. Go to: https://makersuite.google.com/app/apikey
2. Sign in with Google
3. Click "Create API Key"
4. Copy the key

**Option 2: Groq** (Alternative)
1. Go to: https://console.groq.com/keys
2. Sign up (free)
3. Create API key
4. Copy the key

### Set Your API Key:
```powershell
# For Gemini:
$env:GOOGLE_API_KEY="paste-your-key-here"

# OR for Groq:
$env:GROQ_API_KEY="paste-your-key-here"
```

### Run Generator:
```powershell
python blog_generator.py
```

---

## 🎯 Your First Blog Post

When the generator runs, you'll be asked:

### Question 1: Topic
```
💭 What topic should I write about?
> [Type your topic]
```

**Examples:**
- "How to Learn Python Programming in 2025"
- "10 Tips for Healthy Eating on a Budget"
- "The Ultimate Guide to Starting a YouTube Channel"
- "Understanding Cryptocurrency for Beginners"

### Question 2: Tone
```
🎨 Choose a writing tone:
   1. Professional and Informative
   2. Casual and Friendly
   3. Enthusiastic and Inspiring
   4. Authoritative and Expert-Level

Select (1-4):
```

**Choose:**
- `1` for business/technical blogs
- `2` for personal/lifestyle blogs
- `3` for motivational/self-help
- `4` for expert/niche content

---

## 🎉 What You'll Get

After 2-3 minutes, you'll have:

### In `generated_posts/` folder:
```
your-blog-slug.md       ← Ready to publish!
your-blog-slug.json     ← Structured data
```

### The Markdown file includes:
- ✅ SEO-optimized title
- ✅ Meta description
- ✅ Keywords
- ✅ Full blog post (1,500-2,000 words)
- ✅ Well-structured sections
- ✅ Introduction & conclusion
- ✅ Call-to-action

---

## ✅ Success Checklist

- [ ] PowerShell opened
- [ ] Navigated to project folder
- [ ] Ran `.\setup.ps1` or manual setup
- [ ] Got free API key (Gemini or Groq)
- [ ] Set API key in environment or .env
- [ ] Ran `python blog_generator.py`
- [ ] Entered topic and tone
- [ ] Generated first blog post
- [ ] Found files in `generated_posts/`

---

## 🆘 Having Issues?

### "Python not found"
Install Python 3.10+ from https://python.org

### "No API key found"
Make sure you:
1. Got a key from Google or Groq
2. Set it correctly: `$env:GOOGLE_API_KEY="your-key"`
3. Or created `.env` file with your key

### "ModuleNotFoundError"
Run: `pip install -r requirements.txt`

### "RateLimitError"
Wait 1 minute and try again. Free tier limits:
- Gemini: 60 requests/min
- Groq: 30 requests/min

### Script crashes
Make sure you're using Python 3.10 or higher:
```powershell
python --version
```

---

## 🎓 What's Next?

### After your first blog post:
1. ✅ Open the generated Markdown file
2. ✅ Review and edit if needed
3. ✅ Publish to your blog/website
4. ✅ Generate more posts!

### Learn more:
- 📖 [README.md](README.md) - Full documentation
- 🏗️ [ARCHITECTURE.md](ARCHITECTURE.md) - How it works
- 🆓 [API_COMPARISON.md](API_COMPARISON.md) - Compare free APIs
- 🎯 [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Complete overview

### Customize:
- Edit `blog_generator.py` to change agent personalities
- Adjust prompts for different content lengths
- Add new agents (images, social media, etc.)

---

## 💪 You've Got This!

The setup wizard makes it super easy. Just run:

```powershell
.\setup.ps1
```

And follow the prompts. In 3 minutes, you'll be generating professional blog posts! 🚀

---

**Need help? All documentation is in the project folder!**

- Quick start → This file
- Detailed setup → SETUP.md
- Free APIs → FREE_SETUP.md
- Full guide → README.md

**Ready? Let's go!** 🎉
