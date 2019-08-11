
with open("pythonMemo.md", "r", encoding="UTF-8") as f:
  lines = f.read()
line = []
line = lines.split("\n")
for i in line:
  print("''''" + i.strip() + "''''")
