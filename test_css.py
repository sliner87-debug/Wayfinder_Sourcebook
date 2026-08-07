import markdown
from playwright.sync_api import sync_playwright
import os
from pypdf import PdfReader

def test_render(css_string, name):
    with open("Wayfinder_Sourcebook.md", 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    md_text = "<div class='cover-page'>\n\n# Wayfinder Corsair Sourcebook\n\n</div>\n\n## Table of Contents\n[TOC]\n\n" + md_text
    html_content = markdown.markdown(md_text, extensions=['toc', 'tables', 'fenced_code'])
    
    full_html = f"<html><head><meta charset='utf-8'><style>{css_string}</style></head><body>{html_content}</body></html>"
    with open(f"test_{name}.html", "w", encoding="utf-8") as f:
        f.write(full_html)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("file:///" + os.path.abspath(f"test_{name}.html").replace('\\', '/'), wait_until="networkidle")
        page.pdf(
            path=f"test_{name}.pdf", 
            format="Letter",
            margin={"top": "0.5in", "bottom": "0.75in", "left": "0.5in", "right": "0.5in"}
        )
        browser.close()
    
    reader = PdfReader(f"test_{name}.pdf")
    print(f"Test {name} Pages: {len(reader.pages)}")

# Test 1: Full CSS from V2
css_v2 = """
        body { font-family: "Georgia", serif; background-color: #fdf6e3; color: #2c2725; line-height: 1.6; margin: 0; padding: 40px; }
        h1, h2, h3 { font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif; color: #8b0000; border-bottom: 1px solid #8b0000; padding-bottom: 5px; }
        h1 { page-break-before: always; font-size: 2.5em; text-align: center; margin-top: 50px; }
        .cover-page h1 { page-break-before: auto; margin-top: 40vh; border-bottom: none; font-size: 4em; }
        h2 { font-size: 1.8em; margin-top: 30px; }
        h3 { font-size: 1.4em; border-bottom: none; }
        table { width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 0.9em; background-color: white; box-shadow: 0 1px 3px rgba(0,0,0,0.2); page-break-inside: auto; }
        tr { page-break-inside: avoid; page-break-after: auto; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #8b0000; color: white; }
        tr:nth-child(even) { background-color: #f2e6d9; }
        .toc { background-color: #fffaf0; padding: 20px; border: 2px solid #8b0000; border-radius: 5px; margin-bottom: 40px; column-count: 1; }
        .toc li { margin-bottom: 5px; page-break-inside: avoid; }
        blockquote { background: #f9f9f9; border-left: 10px solid #8b0000; margin: 1.5em 10px; padding: 0.5em 10px; font-style: italic; }
        img { max-width: 100%; height: auto; }
        pre { background-color: #2c2725; color: #fdf6e3; padding: 10px; border-radius: 5px; overflow-x: auto; page-break-inside: avoid; }
"""

# Test 2: CSS V2 but NO body padding/margin
css_no_body = css_v2.replace("margin: 0; padding: 40px;", "")

# Test 3: CSS V2 but NO tr page-break-inside avoid
css_no_tr = css_v2.replace("tr { page-break-inside: avoid; page-break-after: auto; }", "")

print("Running CSS diagnosis...")
test_render(css_v2, "v2")
test_render(css_no_body, "no_body_padding")
test_render(css_no_tr, "no_tr_break")
