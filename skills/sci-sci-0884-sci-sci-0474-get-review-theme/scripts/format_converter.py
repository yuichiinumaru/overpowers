#!/usr/bin/env python3
"""
Helper script to format the review theme into standard text, yaml, or json.
"""
import json
import yaml
import argparse
import sys

def format_output(topic, keywords, core_questions, output_format='text'):
    data = {
        "topic": topic,
        "keywords": keywords,
        "core_questions": core_questions
    }

    if output_format == 'json':
        return json.dumps(data, indent=2, ensure_ascii=False)
    elif output_format == 'yaml':
        # Use allow_unicode to keep characters readable
        return yaml.dump(data, allow_unicode=True, sort_keys=False)
    else:
        # Default to text
        kw_str = "、".join(keywords)
        cq_str = "、".join(core_questions)
        return f"主题：{topic}\n关键词：{kw_str}\n核心问题：{cq_str}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Format review theme output")
    parser.add_argument("--topic", required=True, help="Review topic")
    parser.add_argument("--keywords", required=True, help="Comma-separated keywords")
    parser.add_argument("--questions", required=True, help="Comma-separated core questions")
    parser.add_argument("--format", choices=['text', 'json', 'yaml'], default='text', help="Output format")

    args = parser.parse_args()

    kw_list = [k.strip() for k in args.keywords.split(',')]
    q_list = [q.strip() for q in args.questions.split(',')]

    print(format_output(args.topic, kw_list, q_list, args.format))
