"""
Quick example demonstrating the blog generator capabilities
"""

from blog_generator import generate_blog_post, save_blog_post

# Generate a blog post programmatically
blog_post = generate_blog_post(
    topic="How AI is Revolutionizing Content Creation",
    tone="professional yet friendly"
)

# Save it
save_blog_post(blog_post)

# Access the structured data
print(f"\nGenerated: {blog_post.title}")
print(f"Word count: {blog_post.word_count}")
print(f"Keywords: {', '.join(blog_post.keywords)}")
