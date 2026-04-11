class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        for i in range(1, len(maxLeft)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])

        for i in range(len(maxRight)-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1])

        res = 0

        for i in range(len(height)):
            print(max(0, min(maxLeft[i], maxRight[i]) - height[i]))
            res += max(0, min(maxLeft[i], maxRight[i]) - height[i])

        return res



        

        