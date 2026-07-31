import sys
sys.stdout.reconfigure(encoding='utf-8')
filepath = r"E:\My Drive\hoyMatey\ChatGPT-Captain's Techniques Integration - Copy.txt"

try:
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    responses = []
    for i, line in enumerate(lines):
        if line.startswith('## Response:'):
            responses.append(i)
            
    print(f'Found {len(responses)} responses.')
    for r in responses:
        print(f'--- Response at line {r} ---')
        for j in range(r+2, min(r+10, len(lines))):
            if lines[j].strip() and not lines[j].startswith('Thought for') and not lines[j].startswith(':::writing'):
                print(lines[j].strip()[:100])
except Exception as e:
    print('Error:', e)
