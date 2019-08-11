import math as ms

class Hexagon:
    def __init__(self, l1, l2, l3, l4, l5, l6):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4
        self.l5 = l5
        self.l6 = l6

    def calcurate_perimeter(self):
        ans = self.l1 +\
        self.l2 +\
        self.l3 +\
        self.l4 +\
        self.l5 +\
        self.l6
        return ans

if __name__ == "__main__":
    a = Hexagon(60, 50, 70, 60, 50, 70,)
    print(a.calcurate_perimeter())
