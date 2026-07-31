import re
import os

tier_files = [
    '05b_Least_Techniques.md',
    '05c_Lesser_Techniques.md',
    '05d_Greater_Techniques.md',
    '05e_Legendary_Techniques.md'
]

techniques = []

for f in tier_files:
    path = os.path.join(r'h:\Antigravity\Ahoy Matey\Wayfinder_Sourcebook', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Split by ### Technique Name
    blocks = content.split('### ')
    for block in blocks[1:]:
        lines = block.split('\n')
        name = lines[0].strip()
        
        cat = ''
        tier = ''
        action = ''
        
        for line in lines:
            if line.startswith('**Category:**'):
                cat = line.split('**Category:**')[1].strip()
            elif line.startswith('**Tier:**'):
                tier = line.split('**Tier:**')[1].strip()
            elif line.startswith('**Action Type:**'):
                action = line.split('**Action Type:**')[1].strip()
                
        if name and cat and tier:
            techniques.append({
                'name': name,
                'category': cat,
                'tier': tier,
                'action': action
            })

# Generate 11_Progression_Charts.md
out_path = os.path.join(r'h:\Antigravity\Ahoy Matey\Wayfinder_Sourcebook', '11_Progression_Charts.md')

with open(out_path, 'w', encoding='utf-8') as out:
    out.write("# Chapter 11: Progression Charts\n\n")
    out.write("This chapter contains the finalized progression tables for Captain's Techniques.\n\n")
    
    out.write("## Captain's Technique Acquisition\n\n")
    out.write("| Wayfinder Level | Technique Acquired | Max Tier |\n")
    out.write("| --- | --- | --- |\n")
    out.write("| 3rd | 1st | Least |\n")
    out.write("| 6th | 2nd | Lesser |\n")
    out.write("| 9th | 3rd | Lesser |\n")
    out.write("| 12th | 4th | Greater |\n")
    out.write("| 15th | 5th | Greater |\n")
    out.write("| 18th | 6th | Legendary |\n\n")
    
    out.write("## Complete Technique Lookup\n\n")
    
    out.write("| Technique Name | Category | Tier | Action Type |\n")
    out.write("| --- | --- | --- | --- |\n")
    
    # Sort by Category, then Tier, then Name
    tier_order = {'Least': 1, 'Lesser': 2, 'Greater': 3, 'Legendary': 4}
    techniques.sort(key=lambda x: (x['category'], tier_order.get(x['tier'], 5), x['name']))
    
    for t in techniques:
        out.write(f"| {t['name']} | {t['category']} | {t['tier']} | {t['action']} |\n")

print("Generated 11_Progression_Charts.md successfully.")
