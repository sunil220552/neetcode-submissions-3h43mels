class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        
        visited = set()
        
        
        def dfs(r, c) -> int:
            
            if (r, c) == (ROW-1, COL-1) and grid[r][c] == 0:
                return 1
                
            if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == 1:
                return 0
                
            if (r, c) in visited:
                return 0
                
            visited.add((r, c))
                
            res = 0
            for rd, cd in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                res += dfs(rd + r, cd + c)

            visited.remove((r, c))

            
                
            return res 
                
        return dfs(0, 0)