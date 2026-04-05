class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        mem = {}

        def helper(i, cap):
            if i >= len(profit) or cap <= 0:
                return 0

            if (i, cap) in mem:
                return mem[(i, cap)]



            mem[(i, cap)] = helper(i+1, cap)

            if cap - weight[i] >= 0:
                mem[(i, cap)] = max(mem[(i, cap)], profit[i] + helper(i,cap - weight[i]) )

            return mem[(i, cap)]

        return helper(0, capacity)
