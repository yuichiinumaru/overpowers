import argparse
import sys

def generate_config(colors, fonts):
    color_config = ""
    for c in colors:
        name, value = c.split(':')
        color_config += f"        '{name}': '{value}',\n"

    font_config = ""
    for f in fonts:
        name, value = f.split(':')
        font_config += f"        '{name}': ['{value}', 'sans-serif'],\n"

    config = f"""/** @type {{import('tailwindcss').Config}} */
module.exports = {{
  content: [
    "./app/**/*.{{js,ts,jsx,tsx,mdx}}",
    "./pages/**/*.{{js,ts,jsx,tsx,mdx}}",
    "./components/**/*.{{js,ts,jsx,tsx,mdx}}",
    "./src/**/*.{{js,ts,jsx,tsx,mdx}}",
  ],
  theme: {{
    extend: {{
      colors: {{
{color_config}      }},
      fontFamily: {{
{font_config}      }},
    }},
  }},
  plugins: [],
}}
"""
    return config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate tailwind.config.js.")
    parser.add_argument("--colors", nargs="+", help="Colors in key:value format.")
    parser.add_argument("--fonts", nargs="+", help="Fonts in key:value format.")
    args = parser.parse_args()

    config_content = generate_config(args.colors or [], args.fonts or [])
    print(config_content)
    
    with open("tailwind.config.js", "w") as f:
        f.write(config_content)
    print("Generated tailwind.config.js")
