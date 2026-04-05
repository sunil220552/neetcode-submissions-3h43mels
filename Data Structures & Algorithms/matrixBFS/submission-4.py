class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        R, C = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        
        queue = deque()
        visited = set()

        if grid[0][0] == 1:
            return -1

        queue.append((0, 0))
        
        visited.add((0, 0))

        level = 0

        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                if (r, c) == (R-1, C-1):
                    return level

                for rd, cd in directions:
                    nr, nc = rd + r, cd + c

                    if nr not in range(R) or nc not in range(C) or (nr,nc) in visited or grid[nr][nc] == 1:
                        continue

                    visited.add((nr, nc))
                    queue.append((nr, nc))
            level += 1

        return -1

            
            
