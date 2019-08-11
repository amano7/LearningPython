class apple:
  def __init__(self, w, c, f, s):
    self.weight = w
    self.color = c
    self.madeFrom = f
    self.sweet = s

if __name__ == "__main__":
  a = apple(50, "green", "青森", 35)
  print(a.madeFrom)
