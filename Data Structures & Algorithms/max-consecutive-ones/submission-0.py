class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur = 0

        for i in range(len(nums)):
            if i == 0 and nums[i] == 1:
                cur += 1
            else:
                if nums[i] == 1 and nums[i-1] == 1:
                    cur += 1
                elif nums[i] == 1:
                    cur = 1

            res = max(res, cur)

        return res


        
        