a = [0, 2, 6, 7]

while True:
  i = input("Number? ( quit = q ) :")
  if i == "q":
    break
  try:
    i = int(i)
  except ValueError:
    print("数字を入れてください!")
  if i in a:
    print("あたり! ")
  else:
    print("はずれ!")
