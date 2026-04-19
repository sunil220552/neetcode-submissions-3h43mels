class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curCom = []

        def dfs(i: int) -> None:
            if sum(curCom) == target:
                res.append(curCom.copy())
                return
            
            if i >= len(nums) or sum(curCom) > target:
                return

            for j in range(i, len(nums)):
                curCom.append(nums[j])
                dfs(j)
                curCom.pop()

        dfs(0)
        return res


        