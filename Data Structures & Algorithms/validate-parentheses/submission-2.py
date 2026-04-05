class Solution:
    def isValid(self, s: str) -> bool:
        dictPar = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for c in s:
            if c in ['(','{','[']:
                stack.append(c)
            else:
                if stack and dictPar[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return stack == []
        