# 🚀 Quick Setup Guide (FREE APIs Only!)

## Step 1: Install Dependencies

Open PowerShell in this directory and run:

```powershell
pip install marvin python-dotenv google-generativeai groq
```

## Step 2: Get a FREE API Key

### 🌟 Option A: Google Gemini (RECOMMENDED - Most Generous Free Tier)

1. **Go to**: https://makersuite.google.com/app/apikey
2. **Sign in** with your Google account
3. **Click** "Create API Key"
4. **Copy** the key

**Free Tier Limits:**
- ✅ 60 requests per minute
- ✅ 1,500 requests per day
- ✅ No credit card required!

### ⚡ Option B: Groq (Alternative - VERY Fast)

1. **Go to**: https://console.groq.com/keys
2. **Sign up** (free account)
3. **Click** "Create API Key"
4. **Copy** the key

**Free Tier Limits:**
- ✅ 30 requests per minute
- ✅ 14,400 requests per day
- ✅ No credit card required!

## Step 3: Set Up Your API Key

### Method 1: Environment Variable (Quick)
```powershell
# For Google Gemini
$env:GOOGLE_API_KEY="your-api-key-here"

# OR for Groq
$env:GROQ_API_KEY="your-api-key-here"
```

### Method 2: .env File (Recommended)
1. Copy the example file:
   ```powershell
   Copy-Item .env.example .env
   ```

2. Edit `.env` and add your API key:
   ```
   GOOGLE_API_KEY=your-google-api-key-here
   ```

## Step 4: Run the Generator

### Interactive Mode (Recommended for first time):
```powershell
python blog_generator.py
```

You'll be prompted for:
- The blog topic
- Writing tone preference

### Programmatic Mode:
```powershell
python example.py
```

This runs with predefined settings.

## Step 5: Find Your Blog Post

Generated files are in `generated_posts/`:
- `your-blog-slug.md` - Markdown format
- `your-blog-slug.json` - JSON data

## 📊 Expected Output

```
🤖 Using: Google Gemini (Free Tier)

🚀 Starting AI Blog Post Generation
📝 Topic: How AI is Revolutionizing Content Creation

🔍 Phase 1: Researching topic...
✅ Research complete: 8 key points found

📋 Phase 2: Creating content outline...
✅ Outline created: How AI is Revolutionizing Content Creation

✍️  Phase 3: Writing blog post content...
   Writing section 1/5: The Rise of AI Writing Tools
   Writing section 2/5: Content Personalization at Scale
   ...
✅ Content writing complete

🔍 Phase 4: Optimizing for SEO...
✅ SEO optimization complete

💾 Blog post saved:
   📄 Markdown: generated_posts/ai-revolutionizing-content-creation.md
   📊 JSON: generated_posts/ai-revolutionizing-content-creation.json
   📝 Word count: 1847 words
```

## ⚙️ Troubleshooting

### "ModuleNotFoundError: No module named 'marvin'"
```powershell
pip install marvin google-generativeai groq python-dotenv
```

### "❌ No API key found!"
The script couldn't find any API key. Make sure you:
1. Created a `.env` file or set environment variable
2. Named it correctly: `GOOGLE_API_KEY` or `GROQ_API_KEY`
3. Restarted your terminal after setting the variable

### "AuthenticationError: Invalid API key"
- **Gemini**: Go to https://makersuite.google.com/app/apikey and regenerate
- **Groq**: Go to https://console.groq.com/keys and create a new key
- Check for extra spaces in your key
- Make sure the key is active

### "RateLimitError" 
**Google Gemini limits:**
- 60 requests/minute, 1,500/day
- Wait 1 minute if you hit the rate limit

**Groq limits:**
- 30 requests/minute, 14,400/day
- Wait 1 minute if you hit the rate limit

### Generator runs but produces errors
- Make sure you're using Python 3.10+
- Check: `python --version`

## 🎯 Tips for Best Results

1. **Be Specific**: Instead of "AI", try "AI in Healthcare Diagnostics 2025"
2. **Choose the Right Tone**: Match your audience
3. **Review Output**: AI-generated content should be reviewed before publishing
4. **Customize Agents**: Edit `blog_generator.py` to adjust agent personalities

## 🎨 Customization Examples

### Switch Between Free APIs:
The script automatically detects which API key you have:
```powershell
# Use Gemini (default, recommended)
$env:GOOGLE_API_KEY="your-key"

# Switch to Groq (faster but shorter limits)
Remove-Item Env:\GOOGLE_API_KEY
$env:GROQ_API_KEY="your-key"
```

### Generate Shorter Posts:
Edit the prompts in `blog_generator.py` to request fewer paragraphs.

### Add More Sections:
In the strategist's prompt, change "4-6 main sections" to "6-8 main sections".

## 📚 Next Steps

1. ✅ Generate your first blog post
2. ✅ Check the output files in `generated_posts/`
3. ✅ Experiment with different topics and tones
4. ✅ Customize agent instructions for your needs
5. ✅ Build a blog website to display your posts!

---

Need help? Check the README.md for detailed documentation!
