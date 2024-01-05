import re


pattern = r"eggs"
text = "baconeggseggeggsgegesggeggs"

if re.match(pattern, text):
    print('Match found')
else:
    print("No match found")

if re.search(pattern, text):
    print('Match found')
else:
    print("No match found")

print(re.findall(pattern, text))