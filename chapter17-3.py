import re

text = """
The ghost that says boo haunts the loo.
"""

matches = re.findall(r".oo", text, re.I | re.M)

print(matches)

