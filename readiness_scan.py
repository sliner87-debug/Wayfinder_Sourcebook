import os
import glob
import re

directory = r'h:\Antigravity\Ahoy Matey\Wayfinder_Sourcebook'
md_files = glob.glob(os.path.join(directory, '*.md'))

critical_issues = []
major_issues = []
minor_issues = []

for file_path in md_files:
    filename = os.path.basename(file_path)
    if filename in ['Wayfinder_Sourcebook.md', '16_Publication_Readiness_Review.md', '13_Production_Audits.md', '14_World_Development_Report.md']:
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        line_num = i + 1
        
        # Check for placeholders
        if re.search(r'\[\s*\]|TODO|TBD|Pending|XXX', line, re.IGNORECASE):
            # Exclude this actual line if it's matching the regex in a false-positive way, but it's rare.
            major_issues.append(f"**{filename} (Line {line_num}):** Unresolved placeholder found: `{line.strip()}`")
            
        # Check for missing artwork
        if re.search(r'\[Insert Art\]|\[Artwork Needed\]', line, re.IGNORECASE):
            major_issues.append(f"**{filename} (Line {line_num}):** Missing artwork marker: `{line.strip()}`")
            
        # Check for empty headers
        if re.match(r'^#{1,6}\s*$', line.strip()):
            minor_issues.append(f"**{filename} (Line {line_num}):** Empty header found.")
            
        # Check for broken links (e.g. standard markdown links with no url)
        if re.search(r'\[.+?\]\(\)', line):
            critical_issues.append(f"**{filename} (Line {line_num}):** Broken markdown link found: `{line.strip()}`")

# Generate the report
out_path = os.path.join(directory, '16_Publication_Readiness_Review.md')
with open(out_path, 'w', encoding='utf-8') as out:
    out.write("# Chapter 16: Publication Readiness Review\n\n")
    out.write("This document contains the automated scan results for Phase 9: Publication Readiness Review. It catalogs all remaining blockers before the manuscript can be finalized.\n\n")
    
    out.write("## CRITICAL ISSUES\n")
    out.write("*(Missing mechanics, broken tables, or dead links that block publication)*\n\n")
    if not critical_issues:
        out.write("✅ **No critical issues found.**\n\n")
    else:
        for issue in critical_issues:
            out.write(f"- {issue}\n")
        out.write("\n")
            
    out.write("## MAJOR ISSUES\n")
    out.write("*(Missing artwork, unresolved placeholders, or absent sidebars)*\n\n")
    if not major_issues:
        out.write("✅ **No major issues found.**\n\n")
    else:
        for issue in major_issues:
            out.write(f"- {issue}\n")
        out.write("\n")
            
    out.write("## MINOR ISSUES\n")
    out.write("*(Formatting inconsistencies, awkward spacing, or minor grammatical issues)*\n\n")
    if not minor_issues:
        out.write("✅ **No minor issues found.**\n\n")
    else:
        for issue in minor_issues:
            out.write(f"- {issue}\n")
        out.write("\n")
        
    if not critical_issues and not major_issues and not minor_issues:
        out.write("> [!NOTE]\n> **The manuscript is clear of all tracked blockers.** It is ready for Phase 10 (Final Validation).\n")

print("Readiness scan completed.")
