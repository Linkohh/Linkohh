import re

with open('README.md', 'r') as f:
    content = f.read()

# Find all <p align="center">...</p> blocks and compress them to a single line
def compress_match(m):
    inner = m.group(1)
    # Strip newlines and extra spaces
    inner = re.sub(r'\s*\n\s*', ' ', inner).strip()
    return f'<p align="center">\n  {inner}\n</p>'

# We use regex with re.DOTALL to find blocks
new_content = re.sub(r'<p align="center">(.*?)</p>', compress_match, content, flags=re.DOTALL)

with open('README.md', 'w') as f:
    f.write(new_content)

