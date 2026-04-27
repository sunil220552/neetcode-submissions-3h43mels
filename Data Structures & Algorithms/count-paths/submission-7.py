class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        ## Recursion Definition 
        # helper(r, c) returns the uniq paths to reach m, n from 
        # r, c 
        ## base case 
        # When r == m and c == n ; there will be one path 
        ## Explore 
        # Explore r+1, c and r, c+1
        import functools
        @functools.lru_cache(maxsize=None)
        def helper(r, c) -> int:
            if r == m-1 and c == n-1:
                return 1

            if r == m or c == n:
                return 0

            return helper(r+1, c) + helper(r, c+1)

        return helper(0, 0)








        