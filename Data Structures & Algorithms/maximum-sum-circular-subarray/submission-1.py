class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:


        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(0, curSum) + n
            maxSum = max(curSum, maxSum)

        minSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = min(0, curSum) + n
            minSum = min(curSum, minSum)

        return max(maxSum, sum(nums)-minSum) if maxSum > 0 else maxSum
        