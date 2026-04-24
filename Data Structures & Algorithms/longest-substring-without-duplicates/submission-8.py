class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curChars = set()
        L, R = 0, 0

        res = 0

        while R < len(s):
            while s[R] in curChars:
                curChars.remove(s[L])
                L += 1

            curChars.add(s[R])

            res = max(res, len(curChars))
            R += 1

        return res


        