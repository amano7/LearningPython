def anagram(w1,w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

if __name__ == "__main__":
    print(anagram("Iceman","cinema"))
    print(anagram("leaf","tree"))
    print(sorted([1,2,5,4,3])[::-1])
