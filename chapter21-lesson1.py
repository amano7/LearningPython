class Stack():
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        # last = len(self.items) - 1
        # return self.items[last]
        return self.items[-1]
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    stack = Stack()
    print("\n- create stack is_empty = {}\n".format(stack.is_empty()))
    stack.push(1)
    print("- stack.push(1); stack is_empty = {}\n".format(stack.is_empty()))
    item = stack.pop()
    print("- item = stack.pop(); item = {}".format(item))
    print("- stack.pop; stack is_empty = {}\n".format(stack.is_empty()))
    for i in range(0, 7):
        stack.push(i)
    print("- stack.push(0 to 7)")
    print("- stack.peek() = {}\n".format(stack.peek()))
    print("- stack.size() = {}\n".format(stack.size()))
    while stack.size():
        print("pop = {}".format(stack.pop()))

    stack_reverse = Stack()
    for c in "Hello":
        stack_reverse.push(c)
    reverse = ""
    while stack_reverse.size():
        reverse += stack_reverse.pop()
    print("Hello reverse = {}".format(reverse))



