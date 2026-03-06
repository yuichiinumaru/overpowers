#!/usr/bin/env python3
import sys

def generate_css():
    """Generates standard brand CSS based on SKILL.md rules."""
    css = """/* Brand Guidelines CSS */
:root {
  --brand-primary: #1a73e8;
  --brand-secondary: #34a853;
  --brand-accent: #ea4335;
  --brand-dark: #202124;
  --brand-light: #f8f9fa;
  --brand-text: #3c4043;
  --brand-text-muted: #5f6368;

  /* Typography */
  --font-display: 'Product Sans', 'Google Sans', system-ui;
  --font-body: 'Roboto', 'Inter', -apple-system, sans-serif;
  --font-mono: 'Roboto Mono', 'Fira Code', monospace;

  /* Anthropic Fallback/Override Variables */
  --anthropic-dark: #141413;
  --anthropic-light: #faf9f5;
  --anthropic-mid-gray: #b0aea5;
  --anthropic-light-gray: #e8e6dc;
  --anthropic-accent-orange: #d97757;
  --anthropic-accent-blue: #6a9bcc;
  --anthropic-accent-green: #788c5d;

  /* Type scale */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;
  --text-4xl: 2.25rem;

  /* Spacing */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
}

body {
  font-family: var(--font-body);
  color: var(--brand-text);
  background-color: var(--brand-light);
  line-height: 1.6;
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-display);
  color: var(--brand-dark);
  font-weight: 500;
  margin-bottom: var(--space-4);
}

h1 { font-size: var(--text-4xl); }
h2 { font-size: var(--text-3xl); }
h3 { font-size: var(--text-2xl); }

.btn-primary {
  background: var(--brand-primary);
  color: white;
  padding: var(--space-2) var(--space-4);
  border-radius: 4px;
  font-family: var(--font-body);
  font-weight: 500;
  border: none;
  cursor: pointer;
}

.card {
  background: white;
  border: 1px solid var(--brand-light);
  border-radius: 8px;
  padding: var(--space-6);
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

a {
  color: var(--brand-primary);
  text-decoration: underline;
}

/* Anthropic Specific Utility Classes */
.text-anthropic-heading {
  font-family: 'Poppins', Arial, sans-serif;
  color: var(--anthropic-dark);
}

.text-anthropic-body {
  font-family: 'Lora', Georgia, serif;
  color: var(--anthropic-dark);
}
"""
    return css

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "brand-theme.css"
    with open(filepath, 'w') as f:
        f.write(generate_css())
    print(f"Generated brand CSS at {filepath}")
