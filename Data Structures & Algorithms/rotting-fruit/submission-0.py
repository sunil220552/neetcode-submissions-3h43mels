import copy

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotten = deque()

        ROW, COL = len(grid), len(grid[0])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh.add((r,c))
                elif grid[r][c] == 2:
                    rotten.append((r,c))

        if not fresh:
            return 0

        mins = 0
        queue = rotten

        while queue and fresh:
            mins += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for rd, cd in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + rd, c + cd
                    if 0 <= nr < ROW and 0 <= nc < COL and (nr, nc) in fresh:
                        fresh.remove((nr, nc))
                        queue.append((nr, nc))

        return mins if not fresh else -1