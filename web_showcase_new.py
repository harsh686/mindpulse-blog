"""
Add sitemap and robots.txt routes to web_showcase
"""
from flask import Flask, render_template, send_from_directory, make_response
from pathlib import Path
import markdown
import json
from datetime import datetime
import re

app = Flask(__name__)

def get_all_posts():
    """Load all generated blog posts"""
    posts_dir = Path("generated_posts")
    posts = []
    
    if not posts_dir.exists():
        return posts
    
    for md_file in posts_dir.glob("*.md"):
        json_file = md_file.with_suffix('.json')
        if not json_file.exists():
            continue
        
        with open(json_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        excerpt = ""
        for line in lines:
            if line.strip() and not line.startswith('#') and not line.startswith('---'):
                excerpt = line.strip()
                if len(excerpt) > 200:
                    excerpt = excerpt[:200] + "..."
                break
        
        posts.append({
            'slug': metadata.get('slug', ''),
            'title': metadata.get('title', ''),
            'description': metadata.get('meta_description', ''),
            'excerpt': excerpt,
            'date': metadata.get('date', ''),
            'keywords': metadata.get('keywords', []),
            'content': content
        })
    
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts

def format_date(date_str):
    """Format ISO date to readable format"""
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime("%B %d, %Y")
    except:
        return date_str

def render_markdown(content):
    """Convert markdown to HTML"""
    return markdown.markdown(content, extensions=['extra', 'codehilite'])

@app.route('/')
def index():
    """Home page with all blog posts"""
    posts = get_all_posts()
    return render_template('index.html', posts=posts, format_date=format_date)

@app.route('/post/<slug>')
def post(slug):
    """Individual blog post page"""
    posts = get_all_posts()
    post_data = next((p for p in posts if p['slug'] == slug), None)
    
    if not post_data:
        return "Post not found", 404
    
    html_content = render_markdown(post_data['content'])
    
    return render_template('post.html', 
                          post=post_data, 
                          content=html_content,
                          format_date=format_date)

@app.route('/sitemap.xml')
def sitemap():
    """Generate dynamic sitemap"""
    posts = get_all_posts()
    
    sitemap_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://mindpulse.blog/</loc>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>'''
    
    for post in posts:
        sitemap_xml += f'''
    <url>
        <loc>https://mindpulse.blog/post/{post['slug']}</loc>
        <lastmod>{post['date'][:10]}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>'''
    
    sitemap_xml += '\n</urlset>'
    
    response = make_response(sitemap_xml)
    response.headers['Content-Type'] = 'application/xml'
    return response

@app.route('/robots.txt')
def robots():
    """Serve robots.txt"""
    return send_from_directory('static', 'robots.txt')

@app.template_filter('markdown')
def markdown_filter(text):
    return render_markdown(text)

if __name__ == '__main__':
    print("=" * 70)
    print("🌐 MINDPULSE - Daily Reflections on Life")
    print("=" * 70)
    print()
    print("✨ Starting web interface...")
    print("🌍 Open your browser to: http://localhost:5000")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 70)
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)
