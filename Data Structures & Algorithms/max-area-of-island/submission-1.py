class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxArea = 0

        ROW, COL = len(grid), len(grid[0])
        visited = set()

        def dfs(r:int, c:int) -> int:
            if min(r, c) < 0 or r == ROW or c == COL or grid[r][c] == 0 or (r,c) in visited:
                return 0

            visited.add((r, c))

            return 1 + dfs(r+1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1)

        for r in range(ROW):
            for c in range(COL):
                maxArea = max(maxArea, dfs(r, c))

        return maxArea

        