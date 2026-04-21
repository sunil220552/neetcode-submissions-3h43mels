class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if len(points) == 1:
            return 0
        
        # Use Prim's algorithm with an adjacency-list-free approach to save memory and time
        n = len(points)
        minHeap = [(0, 0)] # (weight, node)
        res = 0
        visited = set()

        while len(visited) < n:
            w, u = heapq.heappop(minHeap)
            if u in visited:
                continue

            visited.add(u)
            res += w

            for v in range(n):
                if v not in visited:
                    d = abs(points[u][0]-points[v][0]) + abs(points[u][1]-points[v][1])
                    heapq.heappush(minHeap, (d, v))

        return res