class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        mem = {}

        def dfs(i, c):
            if i >= len(profit):
                return 0

            if (i,c) in mem:
                return mem[(i, c)]

            maxProfit = dfs(i+1, c)

            nc = c - weight[i]

            if nc >= 0:
                p = profit[i] + dfs(i+1, nc)
                maxProfit = max(maxProfit, p)

            mem[(i, c)] = maxProfit
            return mem[(i, c)]

        return dfs(0, capacity)


