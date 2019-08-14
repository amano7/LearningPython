class Solution:
    def reverse(self, x: int) -> int:
        if -2**31 > x or x > 2**31 - 1:
            return 0
        elif x < 0:
            r = str(abs(x))[::-1]
            r = 0 - int(r)
        else:
            r = str(x)[::-1]
        r = int(r)
        if -2**31 > r or r > 2**31 - 1:
            return 0
        else:
            return int(r)

if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(1534236469))
    print(s.reverse(-123))
