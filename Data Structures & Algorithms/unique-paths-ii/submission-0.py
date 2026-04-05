class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])

        cache = {}
        def dfs(r: int, c: int) -> int:
            if r == ROW or c == COL or obstacleGrid[r][c] == 1:
                return 0

            if r == ROW-1 and c == COL-1:
                return 1

            key = tuple([r, c])
            if key in cache:
                return cache[key]

            cache[key] = dfs(r+1, c) + dfs(r, c+1)

            return cache[key]

        return dfs(0, 0)