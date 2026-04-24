class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFor = []

        minSF = float('inf')

        for n in prices:
            minSF = min(minSF, n)
            minSoFor.append(minSF)

        maxSoFor = [0] * len(prices)

        maxSF = float('-inf')

        for i in range(len(prices)-1, -1, -1):
            maxSF = max(maxSF, prices[i])
            maxSoFor[i] = maxSF

        
        res = 0

        for i in range(len(prices)-1):
            res = max(res, maxSoFor[i+1]-minSoFor[i])

        return res



        