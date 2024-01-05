import re

string = "My name is Yogi, Hi i'm Yogi"
pattern = r"Yogi"
newstring = re.sub(pattern, "Rob", string)
print(newstring)