import heapq
class UnionFind(object):
    def __init__(self, n: int) -> None:
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = i

    def find(self, n: int) -> int:
        p = self.par[n]

        while p != self.par[p]:
            p = self.par[self.par[p]]
        
        return p

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        mstECnt = 0

        minHeap = []

        uf = UnionFind(n)

        for s, d, w in edges:
            heapq.heappush(minHeap, (w, s, d))

        while minHeap and mstECnt < n - 1:
            w, s, d = heapq.heappop(minHeap)
            if not uf.union(s, d):
                continue

            mstECnt += 1
            res += w

        return res if mstECnt == n - 1 else -1
