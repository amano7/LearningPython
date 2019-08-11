def f1(inp1):
  """
  入力を2で割る
  """
  ans = int(inp1)/2
  return ans

def f2(inp1):
  """
  入力を4倍する
  """
  ans = int(inp1)*4
  return ans


inp1 = input("Number? : ")

ans1 = f1(inp1)

ans2 = f2(ans1)

print(ans2)
