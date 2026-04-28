import functools

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0] == 1:
            return 0

        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])

        ## Recurrence definition. 
        # helper(r, c) returns the possible ways to reach the right bottom from the given grid r,c

        ## Base case 
        # if r == ROW-1 and c == COL-1, we have reached the bottom right return one. 
        # If R, C is out of bounds, if there is an obstacle return 0. 

        ## Exploration 
        # Explore going down (r+1, c) and right (r, c+1)

        @functools.lru_cache(maxsize=None)
        def helper(r, c) -> int:
            if r == ROW-1 and c == COL-1:
                return 1

            if r >= ROW or c >= COL or obstacleGrid[r][c] == 1:
                return 0

            return helper(r+1, c) + helper(r, c+1)

        return helper(0, 0)

        
        