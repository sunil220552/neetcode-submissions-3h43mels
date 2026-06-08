class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L, H = 0, len(nums)-1

        while L <= H:
            M = (L + H) // 2
            if target > nums[M]:
                L = M + 1
            elif target < nums[M]:
                H = M - 1
            else:
                return M

        return -1 
        