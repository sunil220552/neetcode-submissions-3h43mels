import functools
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:


        ## Recursion definition 
        # helper(i: int, zeroes_used: int, ones_used: int) returns how many strings we can add to the subset, given that we have already used zeros and ones from the set s[i:]

        ## Base case. 
        # i == len(strs), return 0

        ## Explore 
        # For each string, build a decision tree by including strs of i and excluding it. 
        @functools.lru_cache(maxsize=None)
        def helper(i: int, zeroes_used: int, ones_used: int) -> int:
            if i == len(strs):
                return 0

            z, o = strs[i].count("0"), strs[i].count("1")

            res = helper(i+1, zeroes_used, ones_used)

            if z + zeroes_used <= m and o + ones_used <= n:
                res = max(res, 1 + helper(i+1, zeroes_used + z, ones_used + o))

            return res

        return helper(0, 0, 0)


            
        