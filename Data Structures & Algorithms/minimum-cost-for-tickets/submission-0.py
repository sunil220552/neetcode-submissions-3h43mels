class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        passMap = {
            0 : 1,
            1 : 7,
            2 : 30
        }

        memo = {}
        def helper(i):
            if i >= len(days):
                return 0
            if i in memo:
                return memo[i]

            res = float('inf')

            for dp in range(3):
                j = i
                while j < len(days) and days[j] <= (days[i] + passMap[dp] - 1):
                    j += 1

                res = min(res, costs[dp] + helper(j))
            
            memo[i] = res
            return res

        return helper(0)