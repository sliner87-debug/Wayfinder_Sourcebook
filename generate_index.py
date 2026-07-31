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
    
    blocks = content.split('### ')
    for block in blocks[1:]:
        lines = block.split('\n')
        name = lines[0].strip()
        if name:
            techniques.append(name)

techniques.sort()

out_path = os.path.join(r'h:\Antigravity\Ahoy Matey\Wayfinder_Sourcebook', '15_Glossary_and_Index.md')

with open(out_path, 'w', encoding='utf-8') as out:
    out.write("# Chapter 15: Glossary and Master Index\n\n")
    
    out.write("## Glossary of Terms\n\n")
    out.write("- **Captain's Technique:** A magical or extraordinary ability granted by the Wayfinder class, representing the captain's mastery over their vessel, crew, and the elements.\n")
    out.write("- **Living Ship:** The Wayfinder's magical vessel, progressing in power alongside the captain. Upgrades via Tiers (Driftwood, Captain's, Legendary, Mythic, Path-Maker).\n")
    out.write("- **Navigator Spirit:** A spectral entity or manifestation of the sea's will that guides the Wayfinder.\n")
    out.write("- **Shattered Expanse:** The primary setting for the campaign, an ocean dotted with ruins, impossible geography, and shifting magical tides.\n")
    out.write("- **Tier:** The power scaling system for Captain's Techniques and Vessels. The four Technique Tiers are Least, Lesser, Greater, and Legendary.\n\n")
    
    out.write("## Master Technique Index\n\n")
    out.write("The following is an alphabetical index of every Captain's Technique available in the sourcebook.\n\n")
    
    for t in techniques:
        out.write(f"- {t}\n")

print("Generated 15_Glossary_and_Index.md")
