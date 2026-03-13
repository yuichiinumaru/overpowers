#!/usr/bin/env python3
import sys

def generate_skip_link():
    code = """
/* CSS */
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #000;
  color: #fff;
  padding: 8px;
  text-decoration: none;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}

/* React Component */
function SkipLink() {
  return (
    <a href="#main-content" className="skip-link">
      Skip to main content
    </a>
  );
}

/* Usage in Layout */
function Layout({ children }) {
  return (
    <>
      <SkipLink />
      <header>...</header>
      <main id="main-content" tabIndex={-1}>
        {children}
      </main>
    </>
  );
}
"""
    print(code)

if __name__ == "__main__":
    generate_skip_link()
