import re

with open("zen.txt", "r") as f:
    text = f.read()

matches = re.findall("dutch", text, re.I | re.M)

print(matches)

