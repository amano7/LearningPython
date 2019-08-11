class Horse:
    def __init__(self,w,s,r):
        self.weight = w
        self.speed = s
        self.rider = r
class Rider:
    def __init__(self, w, h, g):
        self.weight = w
        self.height = h
        self.gender = g

if __name__ == "__main__":
    d1 = Rider(65,160,"male")
    d2 = Horse(400,40,d1)
    print(f"d1.gender = {d1.gender}")
    print(f"d2.rider.weight = {d2.rider.weight}")
    print(f"d2.speed = {d2.speed}")


