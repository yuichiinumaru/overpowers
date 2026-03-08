import sys
import markdown
import os

def convert_md_to_html(input_path, output_path=None):
    if not os.path.exists(input_path):
        print(f"Error: File {input_path} not found.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Using 'extra' for tables, 'codehilite' for syntax highlighting, and 'toc' for table of contents
    html = markdown.markdown(text, extensions=['extra', 'codehilite', 'toc'])

    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + '.html'

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Converted {input_path} to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_md_to_html.py <input_file> [output_file]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        convert_md_to_html(input_file, output_file)
