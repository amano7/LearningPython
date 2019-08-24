class Square:
    histry = []
    def __init__(self, l):
        self.length = l
        self.histry.append(l)
    def Area(self):
        ans = self.length * 4
        return ans

if __name__ == "__main__":
    d1 = Square(10)
    d2 = Square(30)
    d3 = Square(50)

    print(f"d1 = {d1.Area()}")
    print(f"d2 = {d2.Area()}")
    print(f"d3 = {d3.Area()}")
    print(f"histry = {Square.histry}")




