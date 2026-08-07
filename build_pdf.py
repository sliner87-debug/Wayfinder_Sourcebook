import markdown
import os
from playwright.sync_api import sync_playwright
from pypdf import PdfReader
import sys

def build_pdf():
    input_file = "Wayfinder_Sourcebook.md"
    output_pdf = "Wayfinder_Sourcebook_V3.pdf"
    
    print("Reading markdown...")
    with open(input_file, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    print("Converting to HTML with TOC...")
    md_text = "<div class='cover-page'>\n\n# Wayfinder Corsair Sourcebook\n\n</div>\n\n## Table of Contents\n[TOC]\n\n" + md_text
    
    html_content = markdown.markdown(md_text, extensions=['toc', 'tables', 'fenced_code'])
    
    css = """
    <style>
        /* CRITICAL FIX: Removed body margin/padding which causes Chromium 1-page collapse bugs */
        body {
            font-family: "Georgia", serif;
            color: #2c2725;
            line-height: 1.6;
        }
        h1, h2, h3 {
            font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif;
            color: #8b0000;
            border-bottom: 1px solid #8b0000;
            padding-bottom: 5px;
        }
        h1 {
            page-break-before: always;
            font-size: 2.5em;
            text-align: center;
            margin-top: 50px;
        }
        .cover-page h1 {
            page-break-before: auto;
            margin-top: 300px;
            border-bottom: none;
            font-size: 4em;
        }
        h2 { font-size: 1.8em; margin-top: 30px; }
        h3 { font-size: 1.4em; border-bottom: none; }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            font-size: 0.9em;
            /* CRITICAL FIX: Ensure no constraints on table rendering */
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #8b0000;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2e6d9;
        }
        a {
            color: #8b0000;
            text-decoration: none;
        }
        .toc {
            padding: 20px;
            border: 2px solid #8b0000;
            border-radius: 5px;
            margin-bottom: 40px;
        }
        .toc ul {
            list-style-type: none;
            padding-left: 20px;
        }
        .toc li {
            margin-bottom: 5px;
        }
        blockquote {
            border-left: 10px solid #8b0000;
            margin: 1.5em 10px;
            padding: 0.5em 10px;
            font-style: italic;
        }
        img {
            max-width: 100%;
            height: auto;
        }
        pre {
            background-color: #2c2725;
            color: #fdf6e3;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: Consolas, monospace;
        }
    </style>
    """
    
    full_html = f"<html><head><meta charset='utf-8'>{css}</head><body>{html_content}</body></html>"
    
    html_file = "temp_render.html"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
        
    print("Launching playwright to render PDF V3...")
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            file_url = "file:///" + os.path.abspath(html_file).replace('\\', '/')
            page.goto(file_url, wait_until="networkidle")
            
            page.pdf(
                path=output_pdf,
                format="Letter",
                print_background=True,
                margin={"top": "1in", "bottom": "1in", "left": "1in", "right": "1in"},
                display_header_footer=True,
                header_template="<div></div>",
                footer_template="<div style='font-size: 10px; width: 100%; text-align: center; font-family: Georgia, serif;'>Page <span class='pageNumber'></span></div>",
                tagged=True,
                outline=True
            )
            browser.close()
        print(f"PDF successfully rendered to {output_pdf}")
        
        # Self-Verification check
        reader = PdfReader(output_pdf)
        pages = len(reader.pages)
        print(f"VERIFICATION: PDF has {pages} pages.")
        if pages < 10:
            print("ERROR: PDF collapsed into single page!")
            sys.exit(1)
            
    except Exception as e:
        print(f"Error during rendering: {e}")
        sys.exit(1)
    finally:
        if os.path.exists(html_file):
            os.remove(html_file)

if __name__ == "__main__":
    build_pdf()
