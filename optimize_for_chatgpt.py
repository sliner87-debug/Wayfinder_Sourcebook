import os

input_file = "Wayfinder_Sourcebook_LLM_Optimized.md"
output_file = "Wayfinder_Sourcebook_ChatGPT_Optimized.md"

header = """# WAYFINDER CORSAIR - KNOWLEDGE BASE
*(Instructions for ChatGPT: This file contains the complete lore, mechanics, and bestiary for the Wayfinder Corsair campaign setting. When the player asks a question or encounters a situation, use your retrieval tool to search this document for the relevant Chapter headers (e.g., "Chapter 30: The Bestiary"). Do not hallucinate Pathfinder 1e rules if they are explicitly modified in this document.)*

---

"""

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(header + content)

print(f"ChatGPT Optimized Sourcebook created at {output_file}")
