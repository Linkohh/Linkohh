import re

with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Update welcome.svg version to force reload
text = re.sub(r'\./assets/welcome\.svg(\?v=\d+)?', './assets/welcome.svg?v=2', text)

# Replace the demolab link with local typing.svg
text = re.sub(r'https://readme-typing-svg\.demolab\.com([^\s"]+)', './assets/typing.svg?v=1', text)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(text)
