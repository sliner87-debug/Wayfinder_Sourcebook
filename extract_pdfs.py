import os
from pypdf import PdfReader

dir_path = r'C:\Users\sline\.gemini\antigravity\brain\71eebdba-156e-4791-9c62-0b087d491afb\.user_uploaded'

def extract_pdf_to_md(pdf_filename, md_filename, title):
    pdf_path = os.path.join(dir_path, pdf_filename)
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return
        
    reader = PdfReader(pdf_path)
    text = f"# {title}\n\n"
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            # Clean up the ChatGPT Exporter footers
            lines = page_text.split('\n')
            clean_lines = [line for line in lines if not line.strip().startswith('Powered by ChatGPT Exporter')]
            text += '\n'.join(clean_lines) + '\n\n'
            
    out_path = os.path.join(r'h:\Antigravity\Ahoy Matey\Wayfinder_Sourcebook', md_filename)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Extracted {pdf_filename} to {md_filename}")

extract_pdf_to_md('media__1785498960453.pdf', '13_Production_Audits.md', 'Production Audits')
extract_pdf_to_md('media__1785498969560.pdf', '14_World_Development_Report.md', 'World Development Report')
