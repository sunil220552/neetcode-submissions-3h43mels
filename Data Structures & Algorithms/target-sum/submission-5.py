import functools
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @functools.lru_cache(maxsize=None)
        def helper(i:int, curSum:int) -> int:
            if i == len(nums) and curSum == target:
                return 1

            if i >= len(nums):
                return 0

            return helper(i+1, curSum + nums[i]) + helper(i+1, curSum -  nums[i])

        return helper(0, 0)
        