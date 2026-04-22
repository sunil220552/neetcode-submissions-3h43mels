class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue

            L, R = i+1, len(nums)-1

            while L < R:
                sumALR = a + nums[L] + nums[R]
                if sumALR > 0:
                    R -= 1
                elif sumALR < 0:
                    L += 1
                else:
                    res.append([a, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1

        return res
        