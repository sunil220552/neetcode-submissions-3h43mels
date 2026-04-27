import functools
class Solution:
    def climbStairs(self, n: int) -> int:

        ## Recursion meaning 
        # helper(n) returns distric ways to reach top
        # when we have n steps 
        ## Base case 
        # when n=0 , one way  
        # when n = 1, 1 way ; take one step 
        # when n=2, two ways ; 1->1, 2
        ## Explore 
        # sum of ways to reach n-1 and n-2
        @functools.lru_cache(maxsize=None)
        def helper(n: int) -> int:
            if n <= 2:
                return n

            return helper(n-1) + helper(n-2)

        return helper(n)
        