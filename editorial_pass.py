import os
import glob
import re

directory = r'h:\Antigravity\Ahoy Matey\Wayfinder_Sourcebook'
md_files = glob.glob(os.path.join(directory, '*.md'))

replacements = [
    (r'\bCaptain Technique\b', "Captain's Technique"),
    (r'\bCaptain Techniques\b', "Captain's Techniques"),
    (r'\bFleetAdmiral\b', "Fleet Admiral"),
    (r'\bWayfinder Level\b', "Wayfinder level"),
]

for file_path in md_files:
    if os.path.basename(file_path) == 'Wayfinder_Sourcebook.md':
        continue # Ignore the compiled file
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = content
    for old, new in replacements:
        new_content = re.sub(old, new, new_content)
        
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
print("Editorial consistency pass completed.")
