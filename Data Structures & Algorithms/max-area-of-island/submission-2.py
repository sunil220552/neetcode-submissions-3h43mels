class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ret = 0

        ROW, COL = len(grid), len(grid[0])

        visited = set()

        def dfs(r : int, c : int) -> int:

            if min(r, c) < 0 or r == ROW or c == COL or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))

            res = 1

            for rd, cd in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                res += dfs(r + rd, c + cd)

            return res

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in visited:
                    ret = max(ret, dfs(r, c))

        return ret

        
        