class UnionFind:
    def __init__(self, n: int):

        self._par = {}
        self._rank = {}

        for i in range(n):
            self._par[i] = i
            self._rank[i] = 0

    def find(self, x: int) -> int:
        p = self._par[x]
        while p != self._par[p]:
            self._par[p] = self._par[self._par[p]]
            p = self._par[p]

        return p

    def union(self, x: int, y: int):
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return False

        if self._rank[p1] > self._rank[p2]:
            self._par[p2] = p1
        elif self._rank[p2] > self._rank[p1]:
            self._par[p1] = p2
        else:
            self._par[p1] = p2
            self._rank[p2] += 1
        return True

import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)

        minHeap = []

        for i in range(n):
            for j in range(1, n):
                x, y = points[i], points[j]
                d = abs(x[0]-y[0]) + abs(x[1] - y[1])
                heapq.heappush(minHeap, (d, (i, j)))
        
        mst = []
        res = 0
        while len(mst) < n - 1:
            d, (x, y) = heapq.heappop(minHeap)
            print(f"x, y : {x}, {y}")

            if not uf.union(x, y):
                continue

            res += d
            mst.append((x, y))


        return res 

