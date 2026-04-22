class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasIn = {}

        for i in range(len(nums)):
            if target - nums[i] in hasIn:
                res = [i, hasIn[target - nums[i]]]
                res.sort()
                return res

            hasIn[nums[i]] = i



            
        