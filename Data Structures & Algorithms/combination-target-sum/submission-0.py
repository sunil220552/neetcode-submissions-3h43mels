class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i: int, curSum = 0) -> None:
            if curSum == target:
                res.append(cur.copy())
                return

            if i >= len(nums) or curSum > target:
                return

            cur.append(nums[i])
            dfs(i, curSum + nums[i])

            cur.pop()
            dfs(i+1, curSum)

        dfs(0)
        return res

            
        