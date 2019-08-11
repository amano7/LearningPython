import math as ms

class Data:
    def __init__(self,):
        self.nums = [1, 2, 3, 4, 5]

    def ChangeData(self, index, n):
        self.nums[index] = n

if __name__ == "__main__":
    d1 = Data()
    d2 = Data()
    d1.ChangeData(2, 100)
    d2.ChangeData(2, 500)
    print(f"d1 = {d1.nums}\nd2 = {d2.nums}")
