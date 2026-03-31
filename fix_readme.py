import re

with open('README.md', 'r') as f:
    content = f.read()

# Condense all <a> tags that contain an inner <img> tag across multiple lines
new_content = re.sub(r'<a([^>]*)>\s*<img([^>]*)>\s*</a>', r'<a\1><img\2></a>', content)

# Also condense self-closing <img> tags that might have trailing slashes 
new_content = re.sub(r'<a([^>]*)>\s*<img([^>]*)/>\s*</a>', r'<a\1><img\2/></a>', new_content)

# Replace occurrences of &nbsp;&nbsp; with the custom separator ONLY in the stats and pinned repos sections
# Let's just do it broadly for any &nbsp;&nbsp; that's inside a <p align="center"> block between links
new_content = re.sub(r'</a>\s*&nbsp;&nbsp;\s*<a', r'</a>\n  &nbsp;&nbsp;<img src="./assets/separator.svg" width="24" alt="_" />&nbsp;&nbsp;\n  <a', new_content)

with open('README.md', 'w') as f:
    f.write(new_content)

