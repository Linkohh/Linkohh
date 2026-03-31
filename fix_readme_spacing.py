import re

with open('README.md', 'r') as f:
    content = f.read()

# Replace all occurrences of &nbsp;&nbsp; separator &nbsp;&nbsp; with a single &nbsp; and width 14
new_content = re.sub(
    r'&nbsp;&nbsp;<img src="\./assets/separator\.svg"\s+width="24"\s+alt="_"\s*/>&nbsp;&nbsp;',
    r'&nbsp;<img src="./assets/separator.svg" width="14" alt="_" />&nbsp;',
    content
)

with open('README.md', 'w') as f:
    f.write(new_content)

