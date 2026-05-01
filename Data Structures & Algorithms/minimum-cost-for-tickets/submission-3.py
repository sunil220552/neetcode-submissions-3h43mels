
import functools
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        passDays = { 
            0 : 1, 
            1 : 7,
            2 : 30
        }

        ## Decision point 
        # I'll explore each POS option in a decision tree. 
        ## State 
        # Minimum cost for i-Days  
        ## Return value. 
        # Minimum cost, aggregator min
        ## helper(i) --> Returns the minimum cost to travel for days[i:]
        @functools.lru_cache(maxsize=None)
        def helper(i: int) -> int:
            if i >= len(days):
                return 0

            res = float('inf')

            for k in range(len(costs)):
                price = costs[k]
                passLen = passDays[k]

                j = i

                while j < len(days) and days[j] <= (days[i] + passLen - 1):
                    j += 1


                res = min(res, price + helper(j))

            return res

        return helper(0)

                
        