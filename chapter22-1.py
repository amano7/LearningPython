class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {
            'M':1000,
            'CM':900,
            'D':500,
            'CD':400,
            'C':100,
            'XC':90,
            'L':50,
            'XL':40,
            'X':10,
            'IX':9,
            'V':5,
            'IV':4,
            'I':1,
            '0':0
        }
        s = s + '0'
        ans = []
        for i, j in zip(s, s[1:]):
            if rom[i] < rom[j]:
                temp = - rom[i]
            else:
                temp = rom[i]
            ans.append(temp)
            print(str(temp) + i)
        return sum(ans)

if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("IV"))
    print(s.romanToInt("IX"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))
