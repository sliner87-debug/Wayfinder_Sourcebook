import re
import glob

def convert_items(content):
    def item_replacer(match):
        header = match.group(1)
        meta = match.group(2)
        desc = match.group(3)
        
        # Remove attunement
        meta = re.sub(r'\(requires attunement[^)]*\)', '', meta, flags=re.IGNORECASE).strip()
        meta = meta.replace(', *', '*').replace(',*', '*')
        
        additions = "- **Caster Level (CL):** 5th\n- **Aura:** Moderate magic\n- **Market Price:** 5,000 gp\n- **Construction Requirements:** Craft Wondrous Item"
        return f"{header}\n{meta}\n{additions}\n{desc}"
        
    pattern = re.compile(r'(### [^\n]+)\n(\*[^\n]+\*)\n(.*?(?=\n### |\Z))', re.DOTALL)
    
    new_content = pattern.sub(item_replacer, content)
    return new_content

files = glob.glob("h:/Antigravity/Ahoy Matey/Wayfinder_Sourcebook/3[89]*.md")
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    original = content
    content = convert_items(content)
        
    if content != original:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
