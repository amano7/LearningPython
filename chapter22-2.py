import re
class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if len(strs) == 0 or strs[0] == "":
            return ""
        prefix = ""
        try:
            for i in range(1, len(strs[0]) + 1):
                prefix = strs[0][0:i]
                un_match = False
                for pf_source in strs:
                    if pf_source[0:i] != prefix:
                        un_match = True
                        raise Exception
        except Exception:
            if un_match or len(prefix) > 1:
                prefix = prefix[0:-1]
        return prefix

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    print(s.longestCommonPrefix(["a"]))
    print(s.longestCommonPrefix(["c", "c"]))
    print(s.longestCommonPrefix(["aa", "aa"]))

