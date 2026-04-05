class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        self.grid = grid

        ROW, COL = len(grid), len(grid[0])

        count = 0

        def dfs(r: int, c:int) -> bool:
            if min(r, c) < 0 or r == ROW or c == COL or (r,c) in self.visited or self.grid[r][c] == '0':
                return False

            self.visited.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return True

        for r in range(ROW): 
            for c in range(COL):
                if dfs(r, c):
                    count += 1

        return count


        