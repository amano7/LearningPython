import re

text = """
Arizona 479, 501, 870.
California 209, 213, 650.
"""

matches = re.findall("[0-9]{3}", text, re.I | re.M)

print(matches)

