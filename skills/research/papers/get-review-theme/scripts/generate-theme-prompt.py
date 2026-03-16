#!/usr/bin/env python3
import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate the review theme extraction prompt for an LLM.")
    parser.add_argument("--file", "-f", help="Path to a text file to analyze")
    parser.add_argument("--text", "-t", help="Direct text input to analyze")
    parser.add_argument("--format", choices=["text", "yaml", "json"], default="text", help="Desired output format")
    args = parser.parse_args()

    content = ""
    if args.file:
        if not os.path.exists(args.file):
            print(f"Error: File '{args.file}' not found.")
            sys.exit(1)
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
    elif args.text:
        content = args.text
    else:
        print("Error: Must provide either --file or --text.")
        sys.exit(1)

    prompt = f"""请分析以下内容，提取结构化综述主题。

【输入内容】
{content}

【输出要求】
按以下格式输出 (Format: {args.format})：

"""
    
    if args.format == "text":
        prompt += """主题：{一句话概括，中英文皆可，包含研究对象+核心问题/方法}
关键词：{5-10个英文关键词，使用标准学术术语，逗号或顿号分隔}
核心问题：{2-5个具体问题或挑战，逗号或顿号分隔}
"""
    elif args.format == "yaml":
        prompt += """topic: "{一句话概括，中英文皆可，包含研究对象+核心问题/方法}"
keywords:
  - "{英文关键词1}"
  - "{英文关键词2}"
core_questions:
  - "{具体问题1}"
  - "{具体问题2}"
"""
    elif args.format == "json":
        prompt += """{
  "topic": "{一句话概括，中英文皆可，包含研究对象+核心问题/方法}",
  "keywords": ["{英文关键词1}", "{英文关键词2}"],
  "core_questions": ["{具体问题1}", "{具体问题2}"]
}
"""

    prompt += """
【质量要求】
- 主题：简洁明确，包含研究对象+核心问题/方法，避免过于宽泛
- 关键词：英文，优先使用检索常用的标准术语（如 MeSH、ACM CCS）
- 核心问题：具体而非泛泛，反映领域内的真实挑战或科学问题
"""

    print(prompt)

if __name__ == "__main__":
    main()
