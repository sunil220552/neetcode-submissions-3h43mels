class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0] == 1:
            return 0

        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * COL for _ in range(ROW)]

        print(dp)
        dp[0][0] = 1
        print(dp)
        for r in range(1, ROW):
            if obstacleGrid[r][0] == 1:
                dp[r][0] = 0
            else:
                dp[r][0] = dp[r-1][0]
        
        print(dp)
        
        for c in range(1, COL):
            if obstacleGrid[0][c] == 1:
                dp[0][c] = 0
            else:
                dp[0][c] = dp[0][c-1]


        print(dp)

        

        for r in range(1, ROW):
            for c in range(1, COL):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[-1][-1]


