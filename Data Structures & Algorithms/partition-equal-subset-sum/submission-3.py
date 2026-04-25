class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums) 

        mem = {}


        def helper(i: int, curSum: int) -> bool:
            if i == len(nums):
                return False

            if (i, curSum) in mem:
                return mem[(i, curSum)]

            if (2 * curSum == total):
                return True

            mem[(i, curSum)] = helper(i+1, curSum) or helper(i+1, curSum+nums[i])
            return mem[(i, curSum)]

        return helper(0, 0)


        