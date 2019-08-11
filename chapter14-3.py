class CompareObj:
    def __init__(self, a, b):
        self.aObj = a
        self.bObj = b
    def Comp(self):
        if self.aObj is self.bObj:
            return True
        else:
            return False

if __name__ == '__main__':
    d1 = CompareObj("20", "2")
    print(f"d1 = {d1.Comp()}")





