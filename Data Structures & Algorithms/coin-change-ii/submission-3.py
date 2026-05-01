import functools
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @functools.lru_cache(maxsize=None)
        def helper(i:int, curSum:int) -> int:
            if curSum == amount:
                return 1

            if i == len(coins):
                return 0

            res = helper(i+1, curSum)

            if curSum + coins[i] <= amount:
                res += helper(i, curSum + coins[i])

            return res

        return helper(0, 0)
        