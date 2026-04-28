import functools
class Solution:
    
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)

        target = sum(nums) / 2

        ## Recursion definition. 
        # helper(i:int, curSum:int) returns true if we can sum up subset (curSum) of nums[i:] to a 
        # target value 
        ## Base case. 
        # if curSum == Target, return true. 
        # If curSum > Target or i >= len(nums), return false. 
        ## Explore 
        # Treat it as 0-1 nap-sack. Create all possible subsets. And evaluate if sum adds up to target
        @functools.lru_cache(maxsize=None)
        def helper(i:int, curSum:int) -> bool:

            if curSum == target:
                return True

            if i >= N or curSum > target:
                return False

            return helper(i+1, curSum) or helper(i+1, curSum+nums[i])

        return helper(0, 0)

        