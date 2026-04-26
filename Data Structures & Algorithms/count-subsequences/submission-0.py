class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        L1, L2 = len(s), len(t)

        import functools
        @functools.lru_cache(maxsize=None)
        def helper(i: int, j:int) -> int:
            if j == L2:
                return 1

            if i == L1:
                return 0

            res = helper(i+1, j)

            if s[i] == t[j]:
                res += helper(i+1, j+1)

            return res

        return helper(0, 0)
        