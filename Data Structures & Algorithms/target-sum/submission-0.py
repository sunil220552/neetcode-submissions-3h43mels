class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def helper(i, curSum):
            if i == len(nums):
                if curSum == target:
                    return 1
                else:
                    return 0

            return helper(i+1, curSum + nums[i] ) + helper(i+1, curSum - nums[i])

        return helper(0, 0)
        