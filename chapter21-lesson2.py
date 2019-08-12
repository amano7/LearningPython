class Queue():
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    a_queue = Queue()
    print("\nqueue is_empty = {}".format(a_queue.is_empty()))
    for i in range(5):
        a_queue.enqueue(i)
    print("\nqueue size = {}\n".format(a_queue.size()))
    while a_queue.size():
        print("dequeue = {}".format(a_queue.dequeue()))