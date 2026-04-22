class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}

        def helper(n: int) -> int:
            if n in mem:
                return mem[n]

            if n == 0:
                return 0
            elif n == 1:
                return nums[0]
            elif n == 2:
                return max(nums[0], nums[1])


            mem[n] = max(helper(n-1), nums[n-1] + helper(n-2))

            return mem[n]

        return helper(len(nums))
        