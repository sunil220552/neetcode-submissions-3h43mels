class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        mem = {}

        def dfs(i, c, p):

            if i >= len(weight):
                return p

            if (i, c, p) in mem:
                return mem[(i, c, p)]

            mem[(i, c, p)] = dfs(i+1, c, p)

            if c - weight[i] >= 0:
                mem[(i, c, p)] = max(mem[(i, c, p)], dfs(i, c-weight[i], p + profit[i]))

            return mem[(i, c, p)]

        return dfs(0, capacity, 0)

