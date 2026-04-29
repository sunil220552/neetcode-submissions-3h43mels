import functools
class Solution:
    
    def lastStoneWeightII(self, stones: List[int]) -> int:

        target = sum(stones) // 2


        ## Problem framing. 
        # We are dividing the stones into two equal halves. Let's say if both groups have an equal number of weights, then we know we can smash them together so that we are left with zero weight. 
        # If we cannot divide them into a group of two of equal weights, then we can use the closest subset. We can use a subset whose weight is closest to the target but less than the target. Let's call it max weight. 
        # Target minus max weight will be the remaining weight. 

        ## Recursion Definition 
        # helper(i: int, curSum: 0) -> int: returns the maximum weight of stones closest to target sum from subset stones[i:]

        ## Base case. 
        # If index reaches the end of the list, return the current sum we have. 
        @functools.lru_cache(maxsize=None)
        def helper(i: int, curSum: int) -> int:

            if i == len(stones):
                return curSum 

            res = helper(i+1, curSum)

            if curSum + stones[i] <= target:
                res = max(res, helper(i+1, curSum + stones[i]))

            return res

        best_sum = helper(0, 0)

        return sum(stones) - 2 * best_sum 

        