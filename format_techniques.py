import re
import os

tier_mapping = {
    '05b_Least_Techniques.md': ('Least', 'Levels 1-5'),
    '05c_Lesser_Techniques.md': ('Lesser', 'Levels 6-11'),
    '05d_Greater_Techniques.md': ('Greater', 'Levels 12-17'),
    '05e_Legendary_Techniques.md': ('Legendary', 'Levels 18-20')
}

categories = ['Seamanship', 'Duelist', 'Corsair', 'Fleet', 'Hunter', 'Mystic', 'First Captain']

def format_technique(match, category, tier, level_band):
    name = match.group(1).strip()
    params = match.group(2).strip().split(',')
    effect = match.group(3).strip()
    
    action_type = params[0].strip() if len(params) > 0 else 'Standard Action'
    range_target = params[1].strip() if len(params) > 1 else 'Personal'
    duration = params[2].strip() if len(params) > 2 else 'Instantaneous'
    
    # Replace 'Reaction' with 'Immediate Action'
    if action_type.lower() == 'reaction':
        action_type = 'Immediate Action'
        
    saving_throw = 'None'
    if 'Will negates' in effect or 'Will save' in effect:
        saving_throw = 'Will'
    elif 'Reflex' in effect:
        saving_throw = 'Reflex'
    elif 'Fortitude' in effect:
        saving_throw = 'Fortitude'
        
    return f"""### {name}
**Technique Name:** {name}  
**Category:** {category}  
**Tier:** {tier}  
**Level Band:** {level_band}  
**Type:** Extraordinary  
**Action Type:** {action_type}  
**Range/Target:** {range_target}  
**Duration:** {duration}  
**Saving Throw:** {saving_throw}  
**Prerequisites:** None  

**Effect:**  
{effect}  

**Scaling:**  
None  

**Flavor Text:**  
*A display of the Wayfinder's growing mastery.*

"""

for f, (tier, level_band) in tier_mapping.items():
    path = os.path.join(r'h:\Antigravity\Ahoy Matey\Wayfinder_Sourcebook', f)
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
    out_lines = []
    current_cat = 'Seamanship' # Default
    
    for line in lines:
        if line.startswith('# Chapter'):
            out_lines.append(line + '\n')
            continue
            
        if line.startswith('## '):
            raw_cat = line[3:].replace(' Techniques', '').strip()
            # Map descriptive headers to actual categories
            if 'Seamanship' in raw_cat or 'Voyage' in raw_cat:
                current_cat = 'Seamanship'
            elif 'Duelist' in raw_cat or 'Combat and Quarterdeck' in raw_cat:
                current_cat = 'Duelist'
            elif 'Corsair' in raw_cat:
                current_cat = 'Corsair'
            elif 'Fleet' in raw_cat:
                current_cat = 'Fleet'
            elif 'Hunter' in raw_cat:
                current_cat = 'Hunter'
            elif 'Mystic' in raw_cat:
                current_cat = 'Mystic'
            elif 'First Captain' in raw_cat or 'Sovereignty' in raw_cat:
                current_cat = 'First Captain'
            out_lines.append(f"## {current_cat} Techniques\n\n")
            continue
            
        if line.startswith('**'):
            match = re.match(r'\*\*\d+\.\s+([^\(]+)\s*\((.*?)\):\*\*\s*(.*)', line.strip())
            if match:
                formatted = format_technique(match, current_cat, tier, level_band)
                out_lines.append(formatted)
            else:
                out_lines.append(line)
        else:
            if not line.strip() == '':
                out_lines.append(line)

    with open(path, 'w', encoding='utf-8') as file:
        file.writelines(out_lines)

print("Formatted all techniques successfully.")
