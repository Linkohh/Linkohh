import re

with open('README.md', 'r') as f:
    lines = f.readlines()

new_lines = []
in_tools_section = False

for i, line in enumerate(lines):
    # Check if we are in the zone where tools are defined
    # They are between "## Tools I Use" and "## Featured Work"
    
    if "## Tools I Use" in line:
        in_tools_section = True
    elif "## Featured Work" in line:
        in_tools_section = False

    if in_tools_section and line.strip().startswith('<a href=') and line.strip().endswith('</a>'):
        # Check if the NEXT line is also an <a> tag in this same block
        # If so, append the separator
        next_line_is_badge = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if next_line.startswith('<a href=') and next_line.endswith('</a>'):
                next_line_is_badge = True
                
        new_lines.append(line)
        if next_line_is_badge:
            new_lines.append('  &nbsp;&nbsp;<img src="./assets/separator.svg" width="24" alt="_" />&nbsp;&nbsp;\n')
    else:
        new_lines.append(line)

with open('README.md', 'w') as f:
    f.writelines(new_lines)

