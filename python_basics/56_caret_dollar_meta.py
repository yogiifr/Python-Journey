import re

pattern = r"^gr.y$"
text = "gray"
text2 = "grbp"
text3 = "grby"

if re.match(pattern , text):
    print("Match Found")

# Not found 
if re.match(pattern , text2):
    print("Match1")

if re.match(pattern , text3):
    print("Match2")