class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        mem = {}
        def helper(i: int, cap: int) -> int:
            if i == len(profit):
                return 0

            if (i, cap) in mem:
                return mem[(i, cap)]
            
            maxProfit = helper(i+1, cap)

            newCap = cap - weight[i]

            if newCap >= 0:
                
                maxProfit = max(maxProfit, helper(i+1, newCap) + profit[i])

            mem[(i, cap)] = maxProfit

            return mem[(i, cap)]

        return helper(0, capacity)
                
