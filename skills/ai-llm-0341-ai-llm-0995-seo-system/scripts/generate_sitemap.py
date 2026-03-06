#!/usr/bin/env python3
import argparse
import os
import datetime
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

def create_sitemap(urls):
    urlset = Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    for url in urls:
        url_el = SubElement(urlset, "url")
        loc = SubElement(url_el, "loc")
        loc.text = url

        lastmod = SubElement(url_el, "lastmod")
        lastmod.text = current_date

        changefreq = SubElement(url_el, "changefreq")
        changefreq.text = "weekly"

        priority = SubElement(url_el, "priority")
        priority.text = "0.8" if url.count("/") <= 3 else "0.5"

    xml_string = tostring(urlset, 'utf-8')
    parsed_string = minidom.parseString(xml_string)
    return parsed_string.toprettyxml(indent="  ")

def main():
    parser = argparse.ArgumentParser(description="Generate a basic XML sitemap from a list of URLs.")
    parser.add_argument("--input", required=True, help="Text file containing one URL per line")
    parser.add_argument("--output", default="sitemap.xml", help="Output XML file path")

    args = parser.parse_args()

    try:
        with open(args.input, "r") as f:
            urls = [line.strip() for line in f if line.strip() and line.strip().startswith("http")]
    except FileNotFoundError:
        print(f"Error: Input file {args.input} not found.")
        return

    if not urls:
        print("No valid URLs found in the input file.")
        return

    xml_content = create_sitemap(urls)

    with open(args.output, "w") as f:
        f.write(xml_content)

    print(f"Successfully generated sitemap with {len(urls)} URLs at {args.output}")

if __name__ == "__main__":
    main()
