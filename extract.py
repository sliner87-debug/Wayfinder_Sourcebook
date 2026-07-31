import sys
sys.stdout.reconfigure(encoding='utf-8')
filepath = r"E:\My Drive\hoyMatey\ChatGPT-Captain's Techniques Integration - Copy.txt"

try:
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    def extract_section(start_line, filename):
        content = []
        for line in lines[start_line+2:]:
            if line.startswith('## Prompt:') or line.startswith('## Response:'):
                break
            content.append(line)
        with open(filename, 'w', encoding='utf-8') as out:
            out.writelines(content)
        print(f'Wrote {len(content)} lines to {filename}')

    extract_section(2599, '08_Player_Guide.md')
    extract_section(3572, '09_DM_Integration.md')
    extract_section(7171, '10_DM_Appendix.md')
    extract_section(14342, '11_Progression_Charts.md')
    extract_section(10468, '12_Visual_Production_Plan.md')
    
except Exception as e:
    print('Error:', e)
