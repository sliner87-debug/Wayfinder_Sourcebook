import re

def optimize_for_llm(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Markdown images: ![alt](url)
    content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
    
    # 2. Remove HTML image tags: <img ... >
    content = re.sub(r'<img[^>]*>', '', content)
    
    # 3. Remove other HTML structural tags that LLMs don't care about
    content = re.sub(r'<div[^>]*>', '', content)
    content = re.sub(r'</div>', '', content)
    
    # 4. Remove the TOC (Table of Contents) placeholder if pandoc added it, 
    # though it's likely just in the HTML output. But let's clean up any weird spacing.
    
    # 5. Collapse excessive newlines created by removing elements
    content = re.sub(r'\n{3,}', '\n\n', content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"LLM-Optimized Sourcebook generated at {output_file}")

if __name__ == "__main__":
    optimize_for_llm("Wayfinder_Sourcebook.md", "Wayfinder_Sourcebook_LLM_Optimized.md")
