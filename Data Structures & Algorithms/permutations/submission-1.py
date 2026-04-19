class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(i : int) -> None:
            if i >= len(nums):
                return [[]]

            curPerm = dfs(i+1)

            res = []
            for p in curPerm:
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    res.append(pCopy)

            return res


        return dfs(0)
        


        