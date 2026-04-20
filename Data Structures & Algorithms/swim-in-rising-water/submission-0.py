import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = {}

        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        minHeap = []
        ROW, COL = len(grid), len(grid[0])
        heapq.heappush(minHeap, (0, (0,0)))

        while minHeap:
            t1, (r, c) = heapq.heappop(minHeap)
            if (r, c) in res:
                continue

            res[(r,c)] = t1

            for (rd, cd) in direction:
                nr, nc = r + rd, c + cd
                if (nr, nc) in res:
                    continue
                if min(nr, nc) < 0 or nr == ROW or nc == COL:
                    continue

                me = max(grid[r][c], grid[nr][nc])

                t2 = t1
                if t1 < me:
                    t2 = t1 + me - t1
                heapq.heappush(minHeap, (t2,(nr, nc)))

        return res[(ROW-1, COL-1)]

                

                


        