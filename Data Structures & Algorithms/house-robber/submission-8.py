import functools
class Solution:
    def rob(self, nums: List[int]) -> int:

        ## Recursion definition. 
        # helper(i) returns the value i can from from nums[:i+1] houses. 
        # If i is 3 value I can rob of 0, 1, 2, 3 house
        ## Base case 
        # if i is 0, nums[0] is the max value 
        # if i is 1, max(nums[0], nums[1]) if the max value
        ## Exploration 
        # max( nums[i] + helper(i-2), helper[i-1] )
        @functools.lru_cache(maxsize=None)
        def helper(i) -> int:

            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            return max(helper(i-2) + nums[i], helper(i-1))

        return helper(len(nums)-1)
        