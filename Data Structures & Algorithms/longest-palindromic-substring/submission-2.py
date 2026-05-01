class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""

        LEN = len(s)

        for i in range(LEN):
            L, R = i, i
            while L >= 0 and R < LEN and s[L] == s[R]:
                L -= 1
                R += 1

            if len(s[L+1:R]) > len(res):
                res = s[L+1:R]

            L, R = i, i+1

            while L >= 0 and R < LEN and s[L] == s[R]:
                L -= 1
                R += 1

            if len(s[L+1:R]) > len(res):
                res = s[L+1:R]

        return res

            
        