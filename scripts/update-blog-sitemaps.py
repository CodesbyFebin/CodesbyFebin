#!/usr/bin/env python3
"""
Update sitemaps and feed to include all 100 blog posts
"""

import json
from datetime import datetime

# Load blog posts
with open('/home/user/CodesbyFebin/data/blog-posts.json', 'r') as f:
    data = json.load(f)
    posts = data['posts']

# ============================================================
# Update sitemap.xml
# ============================================================

sitemap_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">

  <!-- Main pages -->
  <url>
    <loc>https://codesbyfebin.vercel.app/portfolio-complete.html</loc>
    <lastmod>2025-10-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>

  <url>
    <loc>https://codesbyfebin.vercel.app/blog/</loc>
    <lastmod>2025-10-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
  </url>

  <!-- Blog posts (100 articles) -->
'''

for post in sorted(posts, key=lambda p: p['date'], reverse=True):
    date = post['date'].split('T')[0]
    sitemap_xml += f'''  <url>
    <loc>https://codesbyfebin.vercel.app/blog/posts/{post['slug']}.html</loc>
    <lastmod>{date}</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.8</priority>
  </url>
'''

sitemap_xml += '''
  <url>
    <loc>https://codesbyfebin.vercel.app/feed.xml</loc>
    <lastmod>2025-10-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>

</urlset>
'''

with open('/home/user/CodesbyFebin/sitemap.xml', 'w') as f:
    f.write(sitemap_xml)

print(f"✓ Updated sitemap.xml with {len(posts)} blog URLs")

# ============================================================
# Update sitemap.json for AI crawlers
# ============================================================

sitemap_json_data = {
    "$schema": "https://codesbyfebin.vercel.app/sitemap.json",
    "site": {
        "name": "CodesbyFebin",
        "url": "https://codesbyfebin.vercel.app",
        "description": "AI infrastructure, verifiable compute with STARK proofs, and sovereign self-hosted systems. 100+ articles and guides.",
        "language": "en",
        "feed": "https://codesbyfebin.vercel.app/feed.xml",
        "blog": "https://codesbyfebin.vercel.app/blog/",
        "llms": "https://codesbyfebin.vercel.app/llms.txt"
    },
    "sitemaps": [
        {
            "url": "https://codesbyfebin.vercel.app/portfolio-complete.html",
            "type": "website",
            "title": "CodesbyFebin — AI Infrastructure & Verifiable Compute",
            "lastModified": "2025-10-03",
            "priority": 1.0,
            "tags": ["portfolio", "systems", "open-source"]
        },
        {
            "url": "https://codesbyfebin.vercel.app/blog/",
            "type": "collection",
            "title": "Blog — 100+ Technical Articles",
            "lastModified": "2025-10-03",
            "priority": 0.95,
            "items": len(posts),
            "tags": ["articles", "tutorials", "guides", "case-studies"]
        }
    ]
}

# Add individual blog posts to sitemap.json
for post in sorted(posts, key=lambda p: p['id'])[:50]:  # Top 50 high-traffic
    sitemap_json_data["sitemaps"].append({
        "url": f"https://codesbyfebin.vercel.app/blog/posts/{post['slug']}.html",
        "type": "article",
        "title": post['title'],
        "category": post['category'],
        "lastModified": post['date'].split('T')[0],
        "priority": 0.85,
        "tags": post.get('tags', [])
    })

with open('/home/user/CodesbyFebin/sitemap.json', 'w') as f:
    json.dump(sitemap_json_data, f, indent=2)

print(f"✓ Updated sitemap.json with top 50 blog articles")

# ============================================================
# Create comprehensive Atom feed
# ============================================================

feed_xml = '''<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>CodesbyFebin — 100+ Technical Articles</title>
  <subtitle>Deep dives into STARK proofs, self-hosted systems, AI infrastructure, and open-source engineering.</subtitle>
  <link href="https://codesbyfebin.vercel.app/blog/"/>
  <link rel="self" href="https://codesbyfebin.vercel.app/feed.xml"/>
  <id>https://codesbyfebin.vercel.app/blog/</id>
  <updated>{}</updated>
  <author>
    <name>Febin Francis</name>
    <email>codesbyfebin@gmail.com</email>
    <uri>https://codesbyfebin.vercel.app</uri>
  </author>
  <rights>© 2025 Febin Francis. All rights reserved.</rights>

'''.format(datetime.now().isoformat() + 'Z')

for post in sorted(posts, key=lambda p: p['date'], reverse=True):
    feed_xml += f'''  <entry>
    <title>{post['title']}</title>
    <link href="https://codesbyfebin.vercel.app/blog/posts/{post['slug']}.html"/>
    <id>https://codesbyfebin.vercel.app/blog/posts/{post['slug']}</id>
    <published>{post['date']}</published>
    <updated>{post['date']}</updated>
    <category term="{post['category']}"/>
    <category term="{post.get('type', 'Article')}"/>
    {(''.join([f'<category term="{tag}"/>' for tag in post.get('tags', [])]))}
    <summary>{post['excerpt']}</summary>
    <content type="html"><![CDATA[
      <p><strong>Category:</strong> {post['category']}</p>
      <p><strong>Read time:</strong> {post['readTime']} minutes</p>
      <p><strong>Difficulty:</strong> {post['difficulty']}</p>
      <p>{post['excerpt']}</p>
      <p><a href="https://codesbyfebin.vercel.app/blog/posts/{post['slug']}.html">Read full article →</a></p>
    ]]></content>
    <author>
      <name>{post['author']}</name>
    </author>
  </entry>

'''

feed_xml += '</feed>'

with open('/home/user/CodesbyFebin/feed.xml', 'w') as f:
    f.write(feed_xml)

print(f"✓ Created comprehensive feed.xml with all {len(posts)} blog articles")

