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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        email2acc = {}

        for i , acc in enumerate(accounts):
            for e in acc[1:]:
                if e not in email2acc:
                    email2acc[e] = i
                else:
                    a1 = email2acc[e]
                    a2 = i
                    uf.union(a1, a2)

        res = {}

        for e, a in email2acc.items():
            pa = uf.find(a)
            if uf.find(pa) in res:
                res[pa].append(e)
            else:
                res[pa] = [e]

        ret = []

        for a, emls in res.items():
            ret.append([accounts[a][0]] + emls)

        return ret



        