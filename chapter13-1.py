class Square():
    def __init__(self,l):
        self.length = l

    def calculate_perimeter(self):
        ans = self.length * 4
        return ans

class Rectangle():
    def __init__(self,l,h):
        self.length = l
        self.height = h

    def calculate_perimeter(self):
        ans = self.length * 2 + self.height * 2
        return ans

if __name__ == "__main__":
    d1 = Square(100)
    d2 = Rectangle(300,400)

    print(f"d1 = {d1.calculate_perimeter()}\nd2 = {d2.calculate_perimeter()}")
