class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curPerm = []

        def dfs(nums: List[int]) -> None:
            if not nums:
                res.append(curPerm.copy())
                return

            for i in range(len(nums)):
                curPerm.append(nums[i])
                newNums = []
                for j in range(len(nums)):
                    if i == j:
                        continue
                    newNums.append(nums[j])
                dfs(newNums)
                curPerm.pop()

        dfs(nums)
        return res

                            