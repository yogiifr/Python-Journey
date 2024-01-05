import re

pattern = r"bread(eggs)*bread"

if re.match(pattern, "breadbread"):
    print("Match Foundt")