class Solution:
    def rob(self, nums: List[int]) -> int:

        mem = {}

        def solution(nums: List[int]) -> int:

            if len(nums) <= 2:
                return max(nums)

            key = tuple(nums)

            if key in mem:
                return mem[key]

            mem[key] = max( nums[0] + solution(nums[2:]), solution(nums[1:]))
            return mem[key]

        return solution(nums)

        