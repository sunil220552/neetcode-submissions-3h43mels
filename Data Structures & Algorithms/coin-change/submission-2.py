import functools
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        ## Recursive definition 
        # helper(i: int, curTotal: int) returns minimum number of coins required 
        # to complete the total given the current total and coins[i:]
        ## Base case
        ## If i == len(coins), return 0. We dont have any conins 
        ## if curTotal == amount, return 0. We don't need any more coins. 
        ## Exploration 
        # Explore the possible subset as an unbound knapsack. 
        @functools.lru_cache(maxsize=None)
        def helper(i: int, curTotal: int) -> int:

            if curTotal == amount:
                return 0
            
            if i == len(coins):
                return float('inf')



            res = helper(i+1, curTotal)

            use = float('inf')

            if curTotal + coins[i] <= amount:
                use = 1 + helper(i, curTotal + coins[i])

            return min(res, use)
        res = helper(0, 0) 
        return -1 if res == float('inf') else res    