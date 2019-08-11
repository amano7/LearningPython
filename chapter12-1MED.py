class Apple:
    def __init__(self, s, c, h, a):
        self.santi = s
        self.color = c
        self.hinshu = h
        self.aji = a
        print("Created!")

import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * math.pi

c1 = Circle(2)
print(c1.area())
c3 = Circle(3)
print(c3.area())
