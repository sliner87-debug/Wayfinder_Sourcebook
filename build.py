import os

files = [
    "01_Campaign_Framework.md",
    "02_Starting_Origins.md",
    "03_Races_and_Transformations.md",
    "04_The_Wayfinder_Class.md",
    "05a_Captains_Techniques_Rules.md",
    "05b_Least_Techniques.md",
    "05c_Lesser_Techniques.md",
    "05d_Greater_Techniques.md",
    "05e_Legendary_Techniques.md",
    "06_Campaign_Engines.md",
    "07_DMs_Guide.md",
    "08_Player_Guide.md",
    "09_DM_Integration.md",
    "10_DM_Appendix.md",
    "11_Progression_Charts.md",
    "12_Visual_Production_Plan.md",
    "13_Production_Audits.md",
    "14_World_Development_Report.md",
    "15_Glossary_and_Index.md",
    "16_Publication_Readiness_Review.md",
    "17_Captains_Techniques_Completion_Report.md",
    "18_World_Atlas.md",
    "19_The_Crimson_Dominion.md",
    "20_The_Grand_Merchant_Consortium.md",
    "21_The_Drowned_Silk_Houses.md",
    "22_The_Free_Captains_Alliance.md",
    "23_The_Spirit_Keepers.md",
    "24_The_Independent_Salvagers.md"
]

combined = "# Wayfinder Corsair Campaign Setting & Rulebook\n\n"
for f in files:
    with open(f, "r", encoding="utf-8") as file:
        combined += file.read() + "\n\n---\n\n"

with open("Wayfinder_Sourcebook.md", "w", encoding="utf-8") as f:
    f.write(combined)

print("Markdown combined successfully.")
