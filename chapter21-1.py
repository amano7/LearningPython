stack = []
comments = "yesterday"
for c in comments:
    stack.append(c)
reverse = ""
while len(stack):
    reverse += stack.pop()
print("{} reverse = {}".format(comments, reverse))

