import re


pattern = r"eggs"

if re.match(pattern, "eggseeeggseggseggs"):
    print('Match found')
else:
    print("No match found")