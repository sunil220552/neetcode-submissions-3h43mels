class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def dfs(i: int) -> List[List[int]]:
            if i >= len(nums):
                return [[]]

            perms = dfs(i+1)
            res = []

            for p in perms:
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    res.append(pCopy)
                    if j < len(p) and p[j] == nums[i]:
                        break

            return res
        return dfs(0)