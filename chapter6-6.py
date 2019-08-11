import re

word = "A screaming comes across the sky."
word = re.sub("([a-z]+)", r"[\1]", word)
print(word)
