import re
import os

tier_files = [
    '05b_Least_Techniques.md',
    '05c_Lesser_Techniques.md',
    '05d_Greater_Techniques.md',
    '05e_Legendary_Techniques.md'
]

techniques = {'Least': [], 'Lesser': [], 'Greater': [], 'Legendary': []}

for f in tier_files:
    path = os.path.join(r'h:\Antigravity\Ahoy Matey\Wayfinder_Sourcebook', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    blocks = content.split('### ')
    for block in blocks[1:]:
        lines = block.split('\n')
        name = lines[0].strip()
        cat = ''
        tier = ''
        
        for line in lines:
            if line.startswith('**Category:**'):
                cat = line.split('**Category:**')[1].strip()
            elif line.startswith('**Tier:**'):
                tier = line.split('**Tier:**')[1].strip()
                
        if tier in techniques:
            techniques[tier].append({'name': name, 'category': cat})

def get_tech(tier, cat_primary, cat_secondary):
    for t in techniques[tier]:
        if t['category'] == cat_primary:
            return t['name']
    for t in techniques[tier]:
        if t['category'] == cat_secondary:
            return t['name']
    return techniques[tier][0]['name'] if techniques[tier] else 'Unknown'

def build_player_guide():
    path = os.path.join(r'h:\Antigravity\Ahoy Matey\Wayfinder_Sourcebook', '08_Player_Guide.md')
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    replacements = {
        'Explorer Captain\n\nPending approved technique selections.': f'Explorer Captain\n\n- **Level 3 (Least):** {get_tech("Least", "Seamanship", "Hunter")}\n- **Level 6 (Lesser):** {get_tech("Lesser", "Seamanship", "Hunter")}\n- **Level 12 (Greater):** {get_tech("Greater", "Seamanship", "Mystic")}\n- **Level 18 (Legendary):** {get_tech("Legendary", "First Captain", "Seamanship")}',
        'Storm Captain\n\nPending approved technique selections.': f'Storm Captain\n\n- **Level 3 (Least):** {get_tech("Least", "Seamanship", "Mystic")}\n- **Level 6 (Lesser):** {get_tech("Lesser", "Seamanship", "Mystic")}\n- **Level 12 (Greater):** {get_tech("Greater", "Mystic", "Seamanship")}\n- **Level 18 (Legendary):** {get_tech("Legendary", "Seamanship", "Mystic")}',
        'Corsair Captain\n\nPending approved technique selections.': f'Corsair Captain\n\n- **Level 3 (Least):** {get_tech("Least", "Corsair", "Duelist")}\n- **Level 6 (Lesser):** {get_tech("Lesser", "Corsair", "Duelist")}\n- **Level 12 (Greater):** {get_tech("Greater", "Corsair", "Fleet")}\n- **Level 18 (Legendary):** {get_tech("Legendary", "Corsair", "First Captain")}',
        'Fleet Admiral\n\nPending approved technique selections.': f'Fleet Admiral\n\n- **Level 3 (Least):** {get_tech("Least", "Fleet", "First Captain")}\n- **Level 6 (Lesser):** {get_tech("Lesser", "Fleet", "First Captain")}\n- **Level 12 (Greater):** {get_tech("Greater", "Fleet", "First Captain")}\n- **Level 18 (Legendary):** {get_tech("Legendary", "First Captain", "Fleet")}',
        'Pirate King\n\nPending approved technique selections.': f'Pirate King\n\n- **Level 3 (Least):** {get_tech("Least", "First Captain", "Corsair")}\n- **Level 6 (Lesser):** {get_tech("Lesser", "First Captain", "Corsair")}\n- **Level 12 (Greater):** {get_tech("Greater", "First Captain", "Fleet")}\n- **Level 18 (Legendary):** {get_tech("Legendary", "First Captain", "Fleet")}',
        'Mystic Navigator\n\nPending approved technique selections.': f'Mystic Navigator\n\n- **Level 3 (Least):** {get_tech("Least", "Mystic", "Seamanship")}\n- **Level 6 (Lesser):** {get_tech("Lesser", "Mystic", "Seamanship")}\n- **Level 12 (Greater):** {get_tech("Greater", "Mystic", "Seamanship")}\n- **Level 18 (Legendary):** {get_tech("Legendary", "Mystic", "Seamanship")}',
        'Duelist Captain\n\nPending approved technique selections.': f'Duelist Captain\n\n- **Level 3 (Least):** {get_tech("Least", "Duelist", "Corsair")}\n- **Level 6 (Lesser):** {get_tech("Lesser", "Duelist", "Corsair")}\n- **Level 12 (Greater):** {get_tech("Greater", "Duelist", "Corsair")}\n- **Level 18 (Legendary):** {get_tech("Legendary", "Duelist", "First Captain")}'
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
        
build_player_guide()
print("Updated player guide.")
