class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        if grid[0][0] == 1:
            return -1
        
        queue.append((0,0))
        # visited.add((0,0))

        lenght = 1

        while queue:
            for _ in range(len(queue)):

                (r,c) = queue.popleft()
                if grid[r][c] == 1 or (r, c) in visited:
                    continue

                if r == ROW-1 and c == COL-1:
                    return lenght

                visited.add((r,c))

                dir = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
                for rd, cd in dir:
                    nr, nc = r + rd, c + cd
                    if nr < 0 or nc < 0 or nr == ROW or nc == COL:
                        continue
                    queue.append((nr, nc))

            lenght += 1

        return -1