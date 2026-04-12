class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0

        preFixCnt = {
            0 : 1
        }

        total = 0

        for n in nums:
            total += n
            if total - k in preFixCnt:
                res += preFixCnt[total - k]
            
            preFixCnt[total] = preFixCnt.get(total, 0) + 1

        return res
