import re
import sys

def consolidate_formatting(readme_path='README.md'):
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            text = f.read()

        # 1. Normalize large sections to 25px
        text = text.replace('height="40"', 'height="25"')

        # 2. Normalize minor sub-sections to 5px
        text = text.replace('height="15"', 'height="5"')

        # 3. Consolidate consecutive spacers (Cleanup operations from insert_separators)
        # This regex ensures we don't accidentally stack multiple spacers
        text = re.sub(r'(<p align="center"><img src="\./assets/spacer\.svg" height="\d+" /></p>\s*)+', 
                      r'<p align="center"><img src="./assets/spacer.svg" height="25" /></p>\n', 
                      text)

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(text)
            
        print("README.md successfully formatted and spaced.")
    except Exception as e:
        print(f"Error formatting README: {e}")

if __name__ == '__main__':
    consolidate_formatting()
