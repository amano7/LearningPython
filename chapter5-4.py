men = {
  "height": 163,
  "favColor": "red",
  "favWriter": "田辺イエロウ"
}

# ans = int(input("height=1, favaret color=2, favaret writer=3 ?"))

# if ans == 1:
#   print(men["height"])
# elif ans == 2:
#   print(men["favColor"])
# elif ans == 3:
#   print(men["favWriter"])
# else:
#   print("Out of Qestion")

ans = input("height,favColor,favWriter ?")

if ans in men:
  print(men[ans])
