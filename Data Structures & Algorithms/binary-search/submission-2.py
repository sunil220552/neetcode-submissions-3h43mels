import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        idx = bisect.bisect_right(nums, target)

        if idx == 0:
            return -1
        else:
            return idx-1 if nums[idx-1] == target else -1
