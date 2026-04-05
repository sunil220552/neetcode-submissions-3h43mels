class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0] * 3

        for n in nums:
            count[n] += 1

        j = 0
        for i in range(0, len(count)):
            n = count[i]
            while n > 0:
                nums[j] = i
                j += 1
                n -= 1

        return nums 

        