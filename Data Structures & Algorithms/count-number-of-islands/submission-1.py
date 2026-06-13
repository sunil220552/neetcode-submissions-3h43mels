class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        visited = set()

        def dfs(r, c):
            if min(r, c) < 0 or r == ROW or c == COL or grid[r][c] == "0" or (r, c) in visited:
                return

            visited.add((r, c))

            for rd, cd in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + rd, c + cd)

        
        res = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1
                    dfs(r, c)


        return res

            