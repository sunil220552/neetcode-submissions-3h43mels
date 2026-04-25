class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        mem = {}
        
        def helper(i, curSum):

            if (i, curSum) in mem:
                return mem[(i, curSum)]
            if i == len(nums):
                if curSum == target:
                    return 1
                else:
                    return 0

            mem[(i, curSum)] = helper(i+1, curSum + nums[i] ) + helper(i+1, curSum - nums[i])
            return mem[(i, curSum)]

        return helper(0, 0)
        