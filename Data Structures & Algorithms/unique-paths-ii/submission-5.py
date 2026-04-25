class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]* COL for _ in range(ROW)]

        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1

        for r in range(1, ROW):
            if obstacleGrid[r][0] == 0:
                dp[r][0] = dp[r-1][0]

        for c in range(1, COL):
            if obstacleGrid[0][c] == 0:
                dp[0][c] = dp[0][c-1]

        for r in range(1, ROW):
            for c in range(1, COL):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[ROW-1][COL-1]


                

        

        
        