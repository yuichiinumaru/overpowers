#!/bin/bash
# Generate a basic sitemap.xml for static HTML files
TARGET=${1:-.}
BASE_URL=${2:-"https://example.com"}

echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
echo "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">"

find "$TARGET" -name "*.html" -type f | while read file; do
    # Remove leading ./
    clean_path=${file#./}
    # Create url entry
    echo "  <url>"
    echo "    <loc>${BASE_URL}/${clean_path}</loc>"
    echo "    <lastmod>$(date -r "$file" +%Y-%m-%d)</lastmod>"
    echo "    <changefreq>weekly</changefreq>"
    if [ "$clean_path" == "index.html" ]; then
        echo "    <priority>1.0</priority>"
    else
        echo "    <priority>0.8</priority>"
    fi
    echo "  </url>"
done

echo "</urlset>"
