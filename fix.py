import re
import glob
import math

def convert_monsters(content):
    # Find all monster blocks
    pattern = re.compile(r'(### .+?\n\*.*?\*\n- \*\*Armor Class:\*\* .*?\n- \*\*Hit Points:\*\* .*?\n- \*\*Speed:\*\* .*?\n- \*\*Challenge:\*\* .*?\n\n\*\*STR:\*\*.*?\n(?:- .*?\n)*(?:\n\*\*Traits:\*\*.*?\n(?:- .*?\n)*)?(?:\n\*\*Actions:\*\*.*?\n(?:- .*?\n)*)?(?:(?:\n\*\*Reactions:\*\*.*?\n(?:- .*?\n)*)?)(?:(?:\n\*\*Legendary Actions.*?\n(?:- .*?\n)*)?))', re.DOTALL)
    
    def replacer(match):
        block = match.group(1)
        
        # Extract STR, DEX, CON
        str_m = re.search(r'\*\*STR:\*\* (\d+)', block)
        dex_m = re.search(r'\*\*DEX:\*\* (\d+)', block)
        con_m = re.search(r'\*\*CON:\*\* (\d+)', block)
        if not str_m: return block
        
        st = int(str_m.group(1))
        dx = int(dex_m.group(1))
        co = int(con_m.group(1))
        
        # HD
        hp_m = re.search(r'\*\*Hit Points:\*\* \d+ \((\d+)d(\d+)(?: \+ (\d+))?\)', block)
        if hp_m:
            hd_c = int(hp_m.group(1))
            hd_s = int(hp_m.group(2))
            hp_b = int(hp_m.group(3)) if hp_m.group(3) else 0
        else:
            hd_c = 1
            hp_b = 0
            
        bab = math.floor(hd_c * 0.75)
        st_mod = math.floor((st - 10) / 2)
        dx_mod = math.floor((dx - 10) / 2)
        co_mod = math.floor((co - 10) / 2)
        
        size_m = re.search(r'\*(Tiny|Small|Medium|Large|Huge|Gargantuan)', block, re.IGNORECASE)
        sz = 0
        if size_m:
            s = size_m.group(1).lower()
            if s == 'tiny': sz = 2
            elif s == 'small': sz = 1
            elif s == 'large': sz = -1
            elif s == 'huge': sz = -2
            elif s == 'gargantuan': sz = -4
            
        cmb = bab + st_mod - sz
        cmd = 10 + bab + st_mod + dx_mod - sz
        
        ac_m = re.search(r'\*\*Armor Class:\*\* (\d+)(?: \((.*?)\))?', block)
        ac = 10
        ac_desc = ""
        if ac_m:
            ac = int(ac_m.group(1))
            if ac_m.group(2): ac_desc = " " + ac_m.group(2)
            
        tch = 10 + dx_mod + sz
        flt = ac - dx_mod
        
        # Replace AC
        new_ac_str = f"**Armor Class:** {ac}{ac_desc}, touch {tch}, flat-footed {flt}"
        block = re.sub(r'\*\*Armor Class:\*\* .*', new_ac_str, block, count=1)
        
        # Add CMB/CMD and Base Atk to STR line
        block = re.sub(r'(\*\*STR:\*\*.*?\n)', r'\1- **Base Atk:** +'+str(bab)+f' | **CMB:** +{cmb} | **CMD:** {cmd}\n- **Feats:** Toughness, Power Attack\n', block, count=1)
        
        return block

    return pattern.sub(replacer, content)


def convert_items(content):
    def item_replacer(match):
        header = match.group(1)
        meta = match.group(2)
        desc = match.group(3)
        
        # Remove attunement
        meta = re.sub(r'\(requires attunement[^)]*\)', '', meta, flags=re.IGNORECASE).strip()
        meta = meta.replace(', )', ')').replace(' )', ')')
        
        additions = "- **Caster Level (CL):** 5th\n- **Aura:** Moderate magic\n- **Market Price:** 5,000 gp\n- **Construction Requirements:** Craft Wondrous Item"
        return f"{header}\n{meta}\n{additions}\n{desc}"
        
    pattern = re.compile(r'(### .*?)\n(\*Wondrous item|Weapon|Armor|Ring.*?\*)\n(.*?)(?=\n### |\Z)', re.DOTALL)
    
    # Needs iterative replacement due to overlapping possibly
    new_content = pattern.sub(item_replacer, content)
    return new_content

files = glob.glob("h:/Antigravity/Ahoy Matey/Wayfinder_Sourcebook/3[5689]*.md")
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    original = content
    if "Magic_Items" in f or "Cursed_Artifacts" in f:
        content = convert_items(content)
    else:
        content = convert_monsters(content)
        
    if content != original:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
