class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        uniqeSet = set()

        L = 0 

        for R in range(len(nums)):
            if R - L > k:
                uniqeSet.remove(nums[L])
                L += 1

            if nums[R] in uniqeSet:
                return True

            uniqeSet.add(nums[R])

        return False

        