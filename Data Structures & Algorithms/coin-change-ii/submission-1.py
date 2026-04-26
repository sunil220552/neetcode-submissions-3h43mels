class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        import functools
        @functools.lru_cache(maxsize=None)
        def helper(i, rem)-> int:
            if rem == 0:
                return 1 
            if i == len(coins) or rem <= 0:
                return 0

            return helper(i+1, rem) + helper(i, rem-coins[i])

        return helper(0, amount)
                
        