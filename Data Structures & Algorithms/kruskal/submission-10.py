class UnionFind(object):
    def __init__(self, n):

        self._parent = {}
        self._rank = {}

        for i in range(n):
            self._parent[i] = i
            self._rank[i] = 0

    def find(self, n):
        p = self._parent[n]

        while p != self._parent[p]:
            self._parent[p] = self._parent[self._parent[p]]
            p = self._parent[p]

        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False

        if self._rank[p1] > self._rank[p2]:
            self._parent[p2] = p1
        elif self._rank[p2] > self._rank[p1]:
            self._parent[p1] = p2
        else:
            self._parent[p2] = p1
            self._rank[p1] += 1
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []

        for s, d, w in edges:
            minHeap.append((w, s, d))
            minHeap.append((w, d, s))

        heapq.heapify(minHeap)

        uf = UnionFind(n)

        mst_wt = 0
        mst_cnt = 0
        while minHeap:
            w, s, d = heapq.heappop(minHeap)
            if not uf.union(s, d):
                continue
            mst_wt += w
            mst_cnt += 1

        if mst_cnt == n - 1:
            return mst_wt
        else:
            return -1


            

        

