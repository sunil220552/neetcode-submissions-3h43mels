class Solution:
    def rob(self, nums: List[int]) -> int:

        import functools
        @functools.lru_cache(maxsize=None)
        def helper(i:int) -> int:
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            return max(helper(i-1), nums[i] + helper(i-2))

        return helper(len(nums)-1)
        