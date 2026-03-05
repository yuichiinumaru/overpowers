#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("Usage: python3 generate-xhs-post.py <job_title>")
    sys.exit(1)

job_title = sys.argv[1]
print(f"Generating Xiaohongshu recruitment post for: {job_title}")
post_content = f"""
🚀 【招聘】我们正在寻找顶尖的 {job_title}！

如果你热爱AI，渴望改变世界，欢迎加入我们！
📍 地点：远程/现场
💻 职位：{job_title}

🌟 核心要求：
- 极客精神
- 优秀的编码能力
- 拥抱AI

💡 投递方式：请私信或发送简历至...
#招聘 #AI #极客 #{job_title.replace(' ', '')}
"""
with open("xhs_post.md", "w") as f:
    f.write(post_content)
print("Post content saved to xhs_post.md")
