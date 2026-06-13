from collections import deque 

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        
        ROW, COL = len(grid), len(grid[0])
        queue = deque()    
        visited = set()
        
        visited.add((0, 0))
        queue.append((0, 0))
        
        reached = False
        path_len = 0
        while queue and not reached:
            for _ in range(len(queue)):
                (r, c) = queue.popleft()
                
                if (r, c) == (ROW-1, COL-1):
                    reached = True
                    break

                
                for rd, cd in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + rd, c + cd
                    
                    if min(nr, nc) < 0 or nr == ROW or nc == COL or (nr, nc) in visited or grid[nr][nc] == 1:
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    
            
            if reached: break
                    
            path_len += 1
        
        return path_len if reached else -1