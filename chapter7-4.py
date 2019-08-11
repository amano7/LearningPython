a = [0, 2, 6, 7]

while True:
  i = input("Number? ( quit = q ) :")
  if i == "q":
    break
  try:
    answer = int(i)
  except ValueError:
    print("数字を入れてください!")
    continue
  if answer in a:
    print("あたり! ")
  else:
    print("はずれ!")
