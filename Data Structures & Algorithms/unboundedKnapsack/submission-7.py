class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        mem = {}

        def helper(i, curCap) -> int:
            key = (i, curCap)
            if key in mem:
                return mem[key]
            if i == len(profit):
                return 0

            res = helper(i+1, curCap)

            if weight[i] <= curCap:
                res = max(res, profit[i] + helper(i, curCap-weight[i]))

            mem[key] = res

            return mem[key]

        return helper(0, capacity)
