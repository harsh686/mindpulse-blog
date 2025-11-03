# MindPulse - Automated Blog Platform

## 🚀 Deployment Guide

### Step 1: Push to GitHub

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit: MindPulse blog platform"

# Create new GitHub repository at github.com/new
# Then push:
git remote add origin https://github.com/YOUR_USERNAME/mindpulse.git
git branch -M main
git push -u origin main
```

### Step 2: Configure GitHub Secrets

Go to your repository → Settings → Secrets and variables → Actions

Add secret:
- Name: `GOOGLE_API_KEY`
- Value: Your Google Gemini API key

### Step 3: Deploy to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Vercel will auto-detect Flask
5. Add environment variable:
   - Key: `GOOGLE_API_KEY`
   - Value: Your API key
6. Click "Deploy"

### Step 4: Configure Custom Domain (Optional)

1. In Vercel dashboard → Your project → Settings → Domains
2. Add your domain (e.g., `mindpulse.blog`)
3. Follow Vercel's DNS instructions
4. SSL certificate auto-configured

### Step 5: Enable GitHub Actions

GitHub Actions will automatically:
- Run every day at 9 AM UTC
- Discover trending topic
- Generate blog post
- Commit to repository
- Trigger Vercel redeployment

Check: Repository → Actions tab

---

## 📋 Post-Deployment Checklist

- [ ] Vercel deployment successful
- [ ] Custom domain configured (if applicable)
- [ ] GitHub Actions running daily
- [ ] Newsletter form connected (update Formspree URL)
- [ ] Social sharing links working
- [ ] Google Analytics added (optional)
- [ ] First 3-5 posts generated manually
- [ ] Test responsive design on mobile

---

## 🔧 Maintenance

### Generate Post Manually

Trigger GitHub Action:
- Go to Actions → Daily Blog Generation → Run workflow

### Monitor Logs

- **GitHub Actions**: Check Actions tab for generation logs
- **Vercel**: Dashboard → Deployments for deploy logs

### Update Content Settings

Edit `blog_generator.py` to adjust:
- Word count (currently 500-800)
- Tone (currently "casual and friendly")
- Number of sections (currently 3-4)

---

## 📊 Analytics & Growth

### Recommended Tools

1. **Google Analytics**: Free traffic tracking
2. **Google Search Console**: SEO monitoring
3. **Formspree**: Newsletter signups (free tier: 50/month)
4. **Plausible/Fathom**: Privacy-focused analytics (paid)

### Setup Google Analytics

1. Create account at analytics.google.com
2. Get tracking ID
3. Add to `templates/index.html` before `</head>`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Newsletter Setup (Formspree)

1. Go to formspree.io
2. Create free account
3. Create new form
4. Copy form endpoint
5. Replace in templates:
   - `index.html`: Line with `formspree.io/f/your-form-id`
   - `post.html`: Same line

---

## 🎯 Growth Strategy

### Month 1: Foundation
- Generate 30 posts (daily automation)
- Submit to Google Search Console
- Share on personal social media
- Join relevant subreddits/communities

### Month 2: SEO
- Optimize meta descriptions
- Add internal linking
- Create pillar content
- Submit sitemap

### Month 3: Distribution
- Cross-post to Medium (with canonical tags)
- Share on LinkedIn
- Join personal growth communities
- Email list building

### Month 4+: Monetization
- Affiliate links (books, courses)
- Sponsored content
- Premium newsletter tier
- Digital products

---

## 🔍 SEO Optimization

### Automatic (Already Implemented)
✅ Meta descriptions
✅ Open Graph tags
✅ Keywords optimization
✅ Semantic HTML
✅ Mobile responsive
✅ Fast loading (Vercel CDN)

### Manual Additions

**Sitemap** (create `static/sitemap.xml`):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://yourdomain.com/</loc>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

**Robots.txt** (create `static/robots.txt`):
```
User-agent: *
Allow: /
Sitemap: https://yourdomain.com/sitemap.xml
```

---

## 💡 Pro Tips

1. **Consistency is key**: Daily publishing builds authority
2. **Email list first**: Own your audience
3. **Engage in comments**: Build community
4. **Cross-promote**: Share on multiple platforms
5. **Long-tail keywords**: Target specific emotional struggles
6. **Internal linking**: Connect related posts
7. **Guest posting**: Get backlinks
8. **Repurpose content**: Turn posts into threads, carousels
9. **Analytics review**: Weekly check what's working
10. **Iterate**: Improve based on data

---

## 🐛 Troubleshooting

### GitHub Action fails
- Check Actions tab for error logs
- Verify GOOGLE_API_KEY secret is set
- Check API quota (1,500 requests/day on free tier)

### Vercel deployment fails
- Check build logs in Vercel dashboard
- Verify all dependencies in requirements.txt
- Check environment variables are set

### Posts not generating
- Run locally first: `python auto_scheduler.py`
- Check trend_logs/ for discovery issues
- Verify API key is valid

### Website not updating
- Vercel auto-deploys on git push
- Check Deployments tab for status
- May take 1-2 minutes to propagate

---

## 📞 Support

**Documentation**:
- BRAND.md - Brand identity and strategy
- QUICKSTART.md - Getting started guide
- AUTONOMOUS_GUIDE.md - Complete system docs

**Generated Content**:
- `generated_posts/` - All blog posts
- `trend_logs/` - Topic discovery history

---

## 🎉 You're Live!

Your automated blog platform is now running 24/7:
- ✅ Discovers trending topics daily
- ✅ Generates thoughtful content
- ✅ Publishes automatically
- ✅ Optimized for SEO
- ✅ Mobile responsive
- ✅ Social sharing ready
- ✅ Newsletter signups

**Next steps**: Share your first posts and start building your audience! 🚀

---

Built with ❤️ • Powered by AI • Fully Autonomous
