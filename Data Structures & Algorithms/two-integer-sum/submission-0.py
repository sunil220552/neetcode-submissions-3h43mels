class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resMap = {}
        for i in range(len(nums)):
            req = target - nums[i]
            if req in resMap:
                return [i, resMap[req]] if i < resMap[req] else [resMap[req], i]
            else:
                resMap[nums[i]] = i
        