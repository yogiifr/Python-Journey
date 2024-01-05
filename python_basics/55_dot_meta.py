import re

pattern = r"gr.y"
text = "gray"

if re.match(pattern, text):
    print("Match Found")