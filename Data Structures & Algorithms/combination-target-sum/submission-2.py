class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        curComb = []

        def helper(i:int) -> None:
            if i == len(nums):
                return

            if sum(curComb) > target:
                return

            if sum(curComb) == target:
                res.append(curComb.copy())
                return

            curComb.append(nums[i])
            helper(i)

            curComb.pop()
            helper(i+1)

        helper(0)
        return res

        





    
        