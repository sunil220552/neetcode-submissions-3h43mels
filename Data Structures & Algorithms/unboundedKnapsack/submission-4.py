class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def helper(i, cap):
            if i >= len(profit) or cap <= 0:
                return 0

            res = helper(i+1, cap)

            if cap - weight[i] >= 0:
                res = max(res, profit[i] + helper(i,cap - weight[i]) )

            return res

        return helper(0, capacity)
