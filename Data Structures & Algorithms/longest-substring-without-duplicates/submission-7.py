class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        L = 0
        chars = set()

        for R in range(len(s)):
            if s[R] in chars:
                while s[R] in chars:
                    chars.remove(s[L])
                    L += 1

            chars.add(s[R])
            res = max(res, (R - L)+1)

        return res

        