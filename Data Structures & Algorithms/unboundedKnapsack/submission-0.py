class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dfs(i, c, p):

            if i >= len(weight):
                return p

            maxProfit = dfs(i+1, c, p)

            if c - weight[i] >= 0:
                maxProfit = max(maxProfit, dfs(i, c-weight[i], p + profit[i]))

            return maxProfit

        return dfs(0, capacity, 0)

