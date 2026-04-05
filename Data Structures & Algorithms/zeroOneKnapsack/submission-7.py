class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def helper(i, c):
            if i >= len(profit) or c <= 0:
                return 0

            p = helper(i+1, c)

            newCap = c - weight[i]

            if newCap >= 0:
                p = max(p, profit[i] + helper(i+1, newCap))

            return p

        return helper(0, capacity)









"""
Input:
profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]
capacity = 8

Output:
12

                               [4, 4, 7, 1]
                                      _
                                

                            0,8           0,12
                                  

                     1,4       1,8    1, 8    0, 12

                  --     2, 4

                      3,3       



"""
