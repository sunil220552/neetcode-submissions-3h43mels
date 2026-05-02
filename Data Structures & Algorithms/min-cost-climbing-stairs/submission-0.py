import functools
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost.append(0)

        ## Recursion Definition 
        # helper(i:int) returns minimum cost to reach top of the staircase 
        # given strais cost[i:]
        @functools.lru_cache(maxsize=None)
        def helper(i:int) -> int:
            if i <= 1:
                return cost[i]

            return cost[i] + min(helper(i-1), helper(i-2))

        return helper(len(cost)-1)

        
        