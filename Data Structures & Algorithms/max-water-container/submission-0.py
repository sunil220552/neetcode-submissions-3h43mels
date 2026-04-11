class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        for L in range(len(heights)):
            for R in range(1, len(heights)):
                res = max(res, (min(heights[L], heights[R]) * (R - L)))


        return res    