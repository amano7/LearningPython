class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp_int = str(x)
        if str(x)[::-1] == temp_int:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))
