"""
Beautiful Web Showcase for Generated Blog Posts
Aesthetic, modern interface inspired by Substack/Medium
"""
from flask import Flask, render_template, send_from_directory
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
        # Skip if corresponding JSON doesn't exist
        json_file = md_file.with_suffix('.json')
        if not json_file.exists():
            continue
        
        # Load JSON metadata
        with open(json_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        # Load markdown content
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract first paragraph as excerpt
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
    
    # Sort by date (newest first)
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
    
    # Convert markdown to HTML
    html_content = render_markdown(post_data['content'])
    
    return render_template('post.html', 
                          post=post_data, 
                          content=html_content,
                          format_date=format_date)

@app.template_filter('markdown')
def markdown_filter(text):
    return render_markdown(text)

if __name__ == '__main__':
    print("=" * 70)
    print("🌐 AESTHETIC BLOG SHOWCASE")
    print("=" * 70)
    print()
    print("✨ Starting beautiful web interface...")
    print("🌍 Open your browser to: http://localhost:5000")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 70)
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)
