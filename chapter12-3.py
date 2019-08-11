import math as ms

class Triangle:
    def __init__(self, b, h):
        self.baseLength = b
        self.height = h

    def area(self):
        ans = self.baseLength * self.height / 2
        return ans

if __name__ == "__main__":
    a = Triangle(60,50)
    print(a.area())
