class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(set(s)) == len(s):
            return len(s)

        res = 0
        L = 0
        chars = set()

        for R in range(len(s)):
            if s[R] in chars:
                res = max(res, R - L)

                while s[R] in chars:
                    chars.remove(s[L])
                    L += 1

            chars.add(s[R])

        res = max(res, len(s) - L)

        return res

        