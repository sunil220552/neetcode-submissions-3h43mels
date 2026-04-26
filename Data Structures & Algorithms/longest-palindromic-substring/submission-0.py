class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPal = ""

        for i in range(len(s)):
            L, R = i, i

            oStr = ""

            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1

            oStr = s[L+1:R]

            L, R = i, i+1
            eStr = ""

            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1

            eStr = s[L+1:R]

            if len(oStr) > len(eStr) and len(oStr) > len(maxPal):
                maxPal = oStr
            elif len(eStr) >= len(oStr) and len(eStr) > len(maxPal):
                maxPal = eStr
            

        return maxPal