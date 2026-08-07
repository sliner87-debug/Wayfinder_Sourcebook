import re
from pypdf import PdfReader

try:
    reader = PdfReader("Wayfinder_Sourcebook_V2.pdf")
    print(f"V2 PDF Pages: {len(reader.pages)}")
except Exception as e:
    print(f"Error reading PDF: {e}")

with open("Wayfinder_Sourcebook.md", 'r', encoding='utf-8') as f:
    text = f.read()

divs_open = text.count("<div")
divs_close = text.count("</div")
print(f"Markdown HTML check: <div count: {divs_open}, </div count: {divs_close}")

print("Checking for massive tables...")
tables = text.split("\n|")
print(f"Found ~{len(tables)} table rows in the raw markdown.")
