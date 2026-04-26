class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.solution(nums[1:]), self.solution(nums[:-1]))


    def solution(self, nums: List[int]) ->int:
        if not nums: return 0
        memo = {}
        def helper(i: int) -> int:
            if i == 0:
                return nums[0]
            if i == 1: 
                return max(nums[0], nums[1])
            if i not in memo:
                memo[i] = max(helper(i-1), nums[i] + helper(i-2))
            return memo[i]

        return helper(len(nums)-1)