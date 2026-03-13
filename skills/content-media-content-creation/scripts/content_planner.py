#!/usr/bin/env python3
import sys

def get_blog_template():
    return """# [Headline]
## TL;DR
**[Key Insight]**

## Introduction
[Hook the reader, state primary keyword]

## [Subheading 1]
[Core idea + evidence]

## [Subheading 2]
[Core idea + examples]

## Conclusion
[Summary + Call to Action]

## Meta Description
[Under 160 chars]
"""

def get_social_template():
    return """[Attention Grabbing Hook]

[Point 1]
[Point 2]

[CTA: comment/share]

#hashtags
"""

def get_email_template():
    return """Subject: [Curiosity/Value]
Preheader: [Complements subject line]

---
[Visual Anchor / Hero Line]

[Content Block 1]
[Content Block 2]

[Primary CTA Button]

---
[Unsubscribe/Socials]
"""

def plan_content(content_type):
    if content_type == "blog":
        print(get_blog_template())
    elif content_type == "social":
        print(get_social_template())
    elif content_type == "email":
        print(get_email_template())
    else:
        print(f"Unknown content type: {content_type}. Available: blog, social, email")

if __name__ == "__main__":
    c_type = sys.argv[1] if len(sys.argv) > 1 else "blog"
    plan_content(c_type)
