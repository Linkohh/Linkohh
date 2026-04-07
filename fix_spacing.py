import sys

with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace major 40px section breaks with 25px breaks
text = text.replace('height="40"', 'height="25"')

# Replace minor 15px sub-section breaks with 5px breaks
text = text.replace('height="15"', 'height="5"')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(text)
