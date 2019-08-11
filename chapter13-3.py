class Shape():
    def __init__(self):
        pass
    def what_am_i(self):
        print("I am a shape.")

class Square(Shape):
    def __init__(self,l):
        self.length = l

    def calculate_perimeter(self):
        ans = self.length * 4
        return ans
    def change_size(self, n):
        self.length += n

class Rectangle(Shape):
    def __init__(self,l,h):
        self.length = l
        self.height = h

    def calculate_perimeter(self):
        ans = self.length * 2 + self.height * 2
        return ans

if __name__ == "__main__":
    d1 = Square(100)
    d2 = Rectangle(400,100)
    print(f"d1 = {d1.calculate_perimeter()}")
    print(f"d2 = {d2.calculate_perimeter()}")
    d1.what_am_i()
    d2.what_am_i()


