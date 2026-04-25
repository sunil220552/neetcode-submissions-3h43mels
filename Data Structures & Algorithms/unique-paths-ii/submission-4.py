class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])

        mem = {}

        visited = set()

        def helper(r: int, c:int) -> int:
            if r == ROW-1 and c == COL-1 and obstacleGrid[r][c] == 0:
                return 1

            if (r, c) in mem:
                return mem[(r, c)]

            if min(r, c) < 0 or r == ROW or c == COL or obstacleGrid[r][c] == 1 or (r, c) in visited:
                return 0

            visited.add((r, c))

            mem[(r, c)] = helper(r+1, c) + helper(r, c+1)

            return mem[(r, c)]

        return helper(0, 0)




            
        