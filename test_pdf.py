import markdown
from playwright.sync_api import sync_playwright
import os

with open("Wayfinder_Sourcebook.md", 'r', encoding='utf-8') as f:
    md_text = f.read()

html_content = markdown.markdown(md_text, extensions=['tables'])

full_html = f"<html><body>{html_content}</body></html>"
with open("test.html", "w", encoding="utf-8") as f:
    f.write(full_html)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("file:///" + os.path.abspath("test.html").replace('\\', '/'), wait_until="networkidle")
    page.pdf(path="test1.pdf", format="Letter")
    browser.close()

from pypdf import PdfReader
reader = PdfReader("test1.pdf")
print(f"Test1 Pages: {len(reader.pages)}")
