class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import functools
        @functools.lru_cache(None)
        def helper(i: int, amount: int) -> int:
            if amount == 0:
                return 0
            if i == len(coins):
                return float('inf')

            res = helper(i+1, amount)

            if amount - coins[i] >= 0:
                res = min(res, 1 + helper(i, amount - coins[i]))

            return res 

        ans = helper(0, amount)
        return ans if ans != float('inf') else -1