import functools
class Solution:
    
    def minCost(self, costs: List[List[int]]) -> int:

        HLen = len(costs)
        @functools.lru_cache(maxsize=None)
        def helper(i:int, prev:int) -> int:
            if i == HLen:
                return 0

            colrOption = set([0, 1, 2])
            if prev != None:
                colrOption.remove(prev)

            res = float('inf')
            for options in colrOption:
                res = min(res, costs[i][options] + helper(i+1, options))

            return res

        return helper(0, None)

        

             





        