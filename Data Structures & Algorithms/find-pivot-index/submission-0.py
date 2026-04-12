class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        preFixSum = []
        total = 0
        for n in nums:
            total += n
            preFixSum.append(total)

        for i in range(len(nums)):
            leftSum = preFixSum[i-1] if i > 0 else 0
            rightSum = preFixSum[-1] - preFixSum[i] if i < len(nums)-1 else 0

            if leftSum == rightSum:
                return i

        return -1
