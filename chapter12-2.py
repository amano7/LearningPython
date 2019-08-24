import math as ms

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        ans = self.radius ** 2 * ms.pi
        return ans

if __name__ == "__main__":
  a = Circle(50)
  print(a.area())
