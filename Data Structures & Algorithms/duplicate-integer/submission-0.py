class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapTmp = {}

        for num in nums:
            if num in mapTmp:
                return True
            else:
                mapTmp[num] = True

        return False
        