class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1

        res = 0

        while L < R:
            water = min(heights[L], heights[R]) * ( R - L)
            res = max(res, water)
            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1

        return res
        