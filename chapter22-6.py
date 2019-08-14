class Solution:
    def isValid(self, s: str) -> bool:

        bracket_bigin = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        bracket_stack = []
        for str_br in s:
            if str_br in bracket_bigin:
                bracket_stack.append(bracket_bigin[str_br])
            else:
                if len(bracket_stack) > 0 and bracket_stack[-1] == str_br:
                    bracket_stack.pop()
                else:
                    return False
        if len(bracket_stack) > 0:
            return False
        else:
            return True


if __name__ == "__main__":
    s = Solution()
    print(s.isValid(']'))
    print(s.isValid('['))
    print(s.isValid('()'))
    print(s.isValid('()[]{}'))
    print(s.isValid('(]'))
    print(s.isValid('([)]'))
    print(s.isValid('{[]}'))
