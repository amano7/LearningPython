def f(inp1, inp2, inp3, opt1=1, opt2=2):
  """
  3個の引数と2個のオプショナル値
  """
  ans = int(inp1)+int(inp2)+int(inp3)+int(opt1)+int(opt2)
  return ans

inp1 = input("Number? : ")
inp2 = input("Number? : ")
inp3 = input("Number? : ")
inp4 = input("Number? : ")
inp5 = input("Number? : ")

ANS = f(inp1, inp2, inp3, inp4)
print(ANS)
