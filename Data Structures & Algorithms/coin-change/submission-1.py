class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import functools
        # helper(i, curSum) return minimun number of coins needed to make curSum
        # given coins[i:]
        @functools.lru_cache(None)
        def helper(i:int, curSum: int) -> int:
            if curSum == amount:
                return 0
            if i == len(coins):
                return float("inf")

            dontUse = helper(i+1, curSum)

            use = float("inf")
            if curSum + coins[i] <= amount:
                use = 1 + helper(i, curSum + coins[i])

            return min(dontUse, use)

        res = helper(0, 0)

        return res if res != float('inf') else -1