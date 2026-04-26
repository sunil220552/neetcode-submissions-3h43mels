class Solution:
    def climbStairs(self, n: int) -> int:

        import functools

        @functools.lru_cache(maxsize=None)
        def helper(n: int) -> int:
            if n <= 2:
                return n

            return helper(n-1) + helper(n-2)
        return helper(n)