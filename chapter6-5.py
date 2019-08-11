fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
# fox = fox[0: -2] + "."
print(fox)

# mid
print("- MID - 5文字目から7文字目")
print(fox[4:8])

# right
print("- RIGHT - 6文字目以降")
print(fox[5:])

# left
print("- LEFT - 5文字目まで")
print(fox[:5])

# len
print("- Length - 文字の長さ")
print(len(fox))
