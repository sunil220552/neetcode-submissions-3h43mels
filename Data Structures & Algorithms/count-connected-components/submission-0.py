class UnionFind(object):
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 1

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return True

        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.par[p2] = p1
        else:
            self.par[p2] = p1
            self.rank[p1] += 1

        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)

        for e1, e2 in edges:
            uf.union(e1, e2)

        res = set()

        for i in range(n):
            res.add(uf.find(i))

        return len(res)
        