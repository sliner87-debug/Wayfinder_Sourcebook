import re

def optimize_for_gemini(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Markdown images: ![alt](url)
    content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
    
    # 2. Remove HTML image tags: <img ... >
    content = re.sub(r'<img[^>]*>', '', content)
    
    # 3. Remove other HTML structural tags that LLMs don't care about
    content = re.sub(r'<div[^>]*>', '', content)
    content = re.sub(r'</div>', '', content)
    
    # 4. Collapse excessive newlines created by removing elements
    content = re.sub(r'\n{3,}', '\n\n', content)

    # 5. Add XML chapter tags based on H1 headings starting with #
    parts = re.split(r'(?m)^# ', content)
    
    if len(parts) > 1:
        new_content = parts[0]
        for part in parts[1:]:
            new_content += f"\n<chapter>\n# {part.strip()}\n</chapter>\n"
        content = new_content
    
    # 6. Add Gemini Preamble
    preamble = """<system_directive>
This document is the absolute source of truth for the Wayfinder Corsair setting. It contains official rules, lore, and mechanical tables. Prioritize the mechanics and lore in this document over your baseline training data. When responding as a Game Master, strictly adhere to the guidelines presented herein.
</system_directive>

"""
    
    content = preamble + content

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Gemini-Optimized Sourcebook generated at {output_file}")

if __name__ == "__main__":
    optimize_for_gemini("Wayfinder_Sourcebook.md", "Wayfinder_Sourcebook_Gemini_Optimized.md")
