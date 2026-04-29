import functools

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:


        ## Recursion Definition 
        # helper(i: int, curWt: int, curProfit: int) returns the max profit we can make given 
        # curWt from weight[i:]

        @functools.lru_cache(maxsize=None)
        def helper(i: int, curWt: int)-> int:
            if i == len(profit):
                return 0

            res = helper(i+1, curWt)

            if curWt + weight[i] <= capacity:
                res = max(res, profit[i] + helper(i, curWt + weight[i]))

            return res

        return helper(0, 0)

        
