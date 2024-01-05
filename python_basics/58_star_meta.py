import re

pattern = r"eggs(bacon)*"
text = "eggs"
text1 = "eggsbacon"
text2 = "eggs"

if re.match(pattern, text):
    print("Match Found")

if re.match(pattern, text1):
    print("Match Found1")

if re.match(pattern, text2):
    print("Match Found2")