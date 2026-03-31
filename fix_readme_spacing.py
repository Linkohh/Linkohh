import re

with open('README.md', 'r') as f:
    content = f.read()

# Replace all occurrences of width 14 with width 7
new_content = re.sub(
    r'&nbsp;<img src="\./assets/separator\.svg" width="14" alt="_" />&nbsp;',
    r'&nbsp;<img src="./assets/separator.svg" width="7" alt="_" />&nbsp;',
    content
)

with open('README.md', 'w') as f:
    f.write(new_content)


