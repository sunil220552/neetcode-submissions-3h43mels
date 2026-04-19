class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curSet = []

        nums.sort()

        def dfs(i: int) -> None:
            if i >= len(nums):
                res.append(curSet.copy())
                return

            curSet.append(nums[i])
            dfs(i+1)

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            curSet.pop()
            dfs(i+1)
            return res

        dfs(0)
        return res
        