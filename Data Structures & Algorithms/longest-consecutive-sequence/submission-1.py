class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums)

        res = 0

        for n in nums:
            if n-1 not in nSet:
                cnt = 1
                while n+1 in nSet:
                    cnt += 1
                    n += 1
                res = max(res, cnt)

        return res

        