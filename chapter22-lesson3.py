def plaindrome(word):
    word = word.lower()
    return word[::-1] == word

if __name__ == "__main__":
    print(plaindrome("Mother"))
    print(plaindrome("Mom"))
    print([1,2,5,4,3][::-1])
