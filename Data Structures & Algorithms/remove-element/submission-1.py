class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valid = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[valid] = nums[i]
                valid += 1

        return valid

        