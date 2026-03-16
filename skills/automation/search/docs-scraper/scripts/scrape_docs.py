import os
import sys
import argparse
import asyncio
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import markdownify

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Error: playwright is not installed. Please run `uv pip install playwright` and `uv run playwright install chromium`", file=sys.stderr)
    sys.exit(1)

async def extract_content(page, selector=None):
    """Extracts the main HTML content from the page."""
    # Wait for network to be idle
    try:
        await page.wait_for_load_state("networkidle", timeout=15000)
    except Exception:
        pass # Ignore timeout if page mostly loaded

    if selector:
        try:
            content_handle = await page.wait_for_selector(selector, timeout=5000)
            if content_handle:
                return await content_handle.inner_html()
        except:
            print(f"Warning: Selector '{selector}' not found. Falling back to default heuristics.")

    # Heuristics for finding main content
    heuristics = ["article", "main", "[role='main']", "#content", ".content", ".markdown-body"]
    for s in heuristics:
        try:
            content_handle = await page.evaluate_handle(f"document.querySelector('{s}')")
            if content_handle and str(content_handle) != 'JSHandle@null':
                 html = await page.evaluate("(element) => element.innerHTML", content_handle)
                 if html and len(html.strip()) > 100:
                     return html
        except Exception:
            pass
    
    # Ultimate fallback: the whole body minus obviously bad elements
    try:
        html = await page.evaluate('''
            () => {
                const body = document.body.cloneNode(true);
                const toRemove = body.querySelectorAll('nav, footer, script, style, iframe, noscript, header, aside');
                toRemove.forEach(el => el.remove());
                return body.innerHTML;
            }
        ''')
        return html
    except Exception as e:
        print(f"Failed to extract body: {e}")
        return ""

async def extract_links(page, base_url):
    """Extracts all same-domain links from the page."""
    try:
        links = await page.evaluate('''() => {
            return Array.from(document.querySelectorAll('a[href]')).map(a => a.href);
        }''')
        
        valid_links = set()
        base_parsed = urlparse(base_url)
        base_netloc = base_parsed.netloc
        base_path = base_parsed.path

        for url in links:
            # Strip anchors
            url = url.split('#')[0]
            parsed = urlparse(url)
            
            # Check domain matches
            if parsed.netloc == base_netloc:
                # Ensure it's under the base path
                if parsed.path.startswith(base_path):
                    valid_links.add(url)
                    
        return list(valid_links)
    except Exception as e:
        print(f"Failed to extract links: {e}")
        return []

def get_save_path(url, base_url, output_dir):
    """Determines the local filesystem path for a given URL."""
    base_parsed = urlparse(base_url)
    parsed = urlparse(url)
    
    # Remove the base path to get relative structure
    rel_path = parsed.path
    if rel_path.startswith(base_parsed.path):
        rel_path = rel_path[len(base_parsed.path):]
    
    rel_path = rel_path.strip("/")
    
    if not rel_path:
        rel_path = "index"
        
    # Replace invalid chars cautiously
    safe_rel_path = rel_path.replace("..", "").replace("?", "_").replace("=", "_")
    
    if safe_rel_path.endswith("/"):
        safe_rel_path += "index"
        
    if not safe_rel_path.endswith(".md"):
        safe_rel_path += ".md"
        
    full_path = os.path.join(output_dir, safe_rel_path)
    return full_path

async def crawl(start_url, output_dir, max_depth, max_pages, selector, headless):
    visited = set()
    queue = [(start_url, 0)] # (url, depth)
    
    print(f"Starting crawl at: {start_url}")
    print(f"Output directory: {output_dir}")
    print(f"Max depth: {max_depth}, Max pages: {max_pages}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = await context.new_page()
        
        pages_crawled = 0
        
        while queue and pages_crawled < max_pages:
            current_url, depth = queue.pop(0)
            
            if current_url in visited:
                continue
                
            visited.add(current_url)
            
            if depth > max_depth:
                continue
                
            print(f"[{pages_crawled+1}/{max_pages}] Crawling (depth {depth}): {current_url}")
            
            try:
                response = await page.goto(current_url, wait_until="domcontentloaded", timeout=30000)
                if response and not response.ok:
                    print(f"  -> Error: Status HTTP {response.status}")
                    continue
                    
                # 1. Extract content
                html_content = await extract_content(page, selector)
                
                if html_content:
                    # Convert HTML to MD
                    md_content = markdownify.markdownify(html_content, heading_style="ATX", escape_asterisks=False)
                    
                    # Ensure title is present (rudimentary)
                    if not md_content.startswith("#"):
                        title = await page.title()
                        md_content = f"# {title}\n\n{md_content}"
                        
                    # Save file
                    save_path = get_save_path(current_url, start_url, output_dir)
                    os.makedirs(os.path.dirname(save_path), exist_ok=True)
                    
                    with open(save_path, "w", encoding="utf-8") as f:
                        f.write(md_content)
                    print(f"  -> Saved to {save_path}")
                else:
                    print("  -> Could not extract reasonable content.")
                
                # 2. Extract links and add to queue if depth allows
                if depth < max_depth:
                    links = await extract_links(page, start_url)
                    added = 0
                    for link in links:
                        if link not in visited and not any(l == link for l, d in queue):
                            queue.append((link, depth + 1))
                            added += 1
                    print(f"  -> Discovered {added} new links.")
                
                pages_crawled += 1
                
            except Exception as e:
                print(f"  -> Failed to process {current_url}: {e}")
                
        await browser.close()
        print(f"\nCrawling finished. Processed {pages_crawled} pages.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recursively crawl and scrape documentation sites using Playwright.")
    parser.add_argument("start_url", help="The root URL to start crawling from.")
    parser.add_argument("output_dir", help="Directory to save the Markdown files.")
    parser.add_argument("--max-depth", type=int, default=5, help="Maximum recursion depth.")
    parser.add_argument("--max-pages", type=int, default=500, help="Maximum number of pages to process globally.")
    parser.add_argument("--selector", type=str, help="Specific CSS selector to target for content extraction.")
    parser.add_argument("--no-headless", action="store_true", help="Run browser in non-headless mode (visible).")
    
    args = parser.parse_args()
    
    # We may need markdownify. Let's make sure it's installed via user instructions, or warn right away.
    try:
        import markdownify
    except ImportError:
        print("Error: markdownify is not installed. Please run `uv pip install markdownify`.", file=sys.stderr)
        sys.exit(1)
        
    asyncio.run(crawl(
        args.start_url, 
        args.output_dir, 
        args.max_depth, 
        args.max_pages, 
        args.selector, 
        not args.no_headless
    ))
