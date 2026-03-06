import argparse

def structure_prompt(background, instructions, tool_guidance, output_desc):
    prompt = f"""<BACKGROUND_INFORMATION>
{background}
</BACKGROUND_INFORMATION>

<INSTRUCTIONS>
{instructions}
</INSTRUCTIONS>

<TOOL_GUIDANCE>
{tool_guidance}
</TOOL_GUIDANCE>

<OUTPUT_DESCRIPTION>
{output_desc}
</OUTPUT_DESCRIPTION>
"""
    return prompt

def main():
    parser = argparse.ArgumentParser(description='Structure a system prompt with XML-like tags.')
    parser.add_argument('--background', required=True, help='Background information')
    parser.add_argument('--instructions', required=True, help='Core instructions')
    parser.add_argument('--tools', required=True, help='Tool guidance')
    parser.add_argument('--output', required=True, help='Output description')
    parser.add_argument('--file', help='Output file path')

    args = parser.parse_args()

    result = structure_prompt(args.background, args.instructions, args.tools, args.output)

    if args.file:
        with open(args.file, 'w') as f:
            f.write(result)
        print(f"Prompt structured and written to {args.file}")
    else:
        print(result)

if __name__ == "__main__":
    main()
