import argparse

def organize_context(start_blocks, middle_blocks, end_blocks):
    output = []
    
    if start_blocks:
        output.append("<!-- BEGIN HIGH-ATTENTION ZONE (START) -->")
        output.extend(start_blocks)
        output.append("<!-- END HIGH-ATTENTION ZONE (START) -->\n")
    
    if middle_blocks:
        output.append("<!-- BEGIN LOW-ATTENTION ZONE (MIDDLE) -->")
        output.extend(middle_blocks)
        output.append("<!-- END LOW-ATTENTION ZONE (MIDDLE) -->\n")
    
    if end_blocks:
        output.append("<!-- BEGIN HIGH-ATTENTION ZONE (END) -->")
        output.extend(end_blocks)
        output.append("<!-- END HIGH-ATTENTION ZONE (END) -->")
        
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description='Organize context blocks to mitigate lost-in-middle degradation.')
    parser.add_argument('--start', action='append', help='Blocks for the beginning (high priority)')
    parser.add_argument('--middle', action='append', help='Blocks for the middle (supporting context)')
    parser.add_argument('--end', action='append', help='Blocks for the end (critical summary)')
    parser.add_argument('--output', help='Output file path')

    args = parser.parse_args()

    # If user passed strings with newlines, we should treat them as multiple blocks if needed
    # but here we just take them as they are.
    
    result = organize_context(args.start or [], args.middle or [], args.end or [])

    if args.output:
        with open(args.output, 'w') as f:
            f.write(result)
        print(f"Context organized and written to {args.output}")
    else:
        print(result)

if __name__ == "__main__":
    main()
