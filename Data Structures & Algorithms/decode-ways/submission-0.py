class Solution:
    def numDecodings(self, s: str) -> int:

        import functools
        @functools.lru_cache(maxsize=None)
        def helper(i: int) -> int:
            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            res = 0

            res = helper(i+1)

            if s[i] == "1" and i+1 < len(s):
                res += helper(i+2)

            if s[i] == "2" and i+1 < len(s) and s[i+1] in "0123456":
                res += helper(i+2)

            return res

        return helper(0)
        