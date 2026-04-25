class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        itemCnt = len(profit)
        dp = [[0] * (capacity+1) for _ in range(itemCnt+1)]

        for i in range(1, itemCnt+1):
            for c in range(1, capacity+1):
                dp[i][c] = dp[i-1][c]

                if weight[i-1] <= c:
                    dp[i][c] = max(dp[i][c], dp[i-1][c-weight[i-1]] + profit[i-1])

        return dp[itemCnt][capacity]




