class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curSet = []

        def helper(i: int) -> None:
            if i == len(nums):
                res.append(curSet.copy())
                return
                
            curSet.append(nums[i])
            helper(i+1)
            
            curSet.pop()
            helper(i+1)
            
        helper(0)
        
        return res
        