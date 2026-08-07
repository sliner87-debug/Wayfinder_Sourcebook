import markdown
import os
from playwright.sync_api import sync_playwright

def build_pdf():
    input_file = "Wayfinder_Sourcebook.md"
    output_pdf = "Wayfinder_Sourcebook_V1.pdf"
    
    print("Reading markdown...")
    with open(input_file, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    print("Converting to HTML with TOC...")
    # 'toc' extension generates anchor links and can insert a TOC if [TOC] is present.
    # We will inject [TOC] at the top of the document for the index.
    md_text = "# Wayfinder Corsair Sourcebook\n\n## Table of Contents\n[TOC]\n\n" + md_text
    
    html_content = markdown.markdown(md_text, extensions=['toc', 'tables', 'fenced_code'])
    
    css = """
    <style>
        body {
            font-family: "Georgia", serif;
            background-color: #fdf6e3;
            color: #2c2725;
            line-height: 1.6;
            margin: 0;
            padding: 40px;
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
        /* Except the very first H1 */
        h1:first-of-type {
            page-break-before: auto;
            margin-top: 0;
        }
        h2 { font-size: 1.8em; margin-top: 30px; }
        h3 { font-size: 1.4em; border-bottom: none; }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            font-size: 0.9em;
            background-color: white;
            box-shadow: 0 1px 3px rgba(0,0,0,0.2);
            page-break-inside: avoid;
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
        a:hover {
            text-decoration: underline;
        }
        .toc {
            background-color: #fffaf0;
            padding: 20px;
            border: 2px solid #8b0000;
            border-radius: 5px;
            margin-bottom: 40px;
            column-count: 1; /* For PDF reading, a single column TOC is often cleaner unless specified otherwise */
        }
        @media (min-width: 800px) {
            .toc {
                column-count: 2;
            }
        }
        .toc ul {
            list-style-type: none;
            padding-left: 20px;
        }
        .toc li {
            margin-bottom: 5px;
            page-break-inside: avoid;
        }
        blockquote {
            background: #f9f9f9;
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
        
    print("Launching playwright to render PDF...")
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
                margin={"top": "0.5in", "bottom": "0.5in", "left": "0.5in", "right": "0.5in"}
            )
            browser.close()
        print(f"PDF successfully rendered to {output_pdf}")
    except Exception as e:
        print(f"Error during rendering: {e}")
        print("Note: Ensure playwright browsers are installed by running: playwright install chromium")
    finally:
        if os.path.exists(html_file):
            os.remove(html_file)

if __name__ == "__main__":
    build_pdf()
