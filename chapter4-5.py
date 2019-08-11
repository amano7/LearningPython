def f1(inp1):
  """
  引数をFloatに変換して返す
  変換できないときはエラー文字列を返す
  """
  try:
    ans = float(inp1)
  except (ValueError):
    ans = "Error: " + inp1
  return ans

inp1 = input("Number by String ?")
ans = f1(inp1)
print (ans)