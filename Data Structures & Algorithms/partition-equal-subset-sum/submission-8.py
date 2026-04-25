class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2:
            return False

        target = sum(nums) // 2

        dp = [ [False] * (target+1) for _ in range(len(nums)+1)]

        for i in range(len(nums)+1):
            dp[i][0] = True

        for i in range(1, len(nums)+1):
            for s in range(1, target+1):
                dp[i][s] = dp[i-1][s]

                if nums[i-1] <= s:
                    dp[i][s] = dp[i][s] or dp[i-1][s-nums[i-1]]

        return dp[len(nums)][target]



        