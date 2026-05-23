class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * (2 * N)

        for i in range(len(nums)):
            res[i] = nums[i]
            res[i+ N] = nums[i]

        return res

        
        