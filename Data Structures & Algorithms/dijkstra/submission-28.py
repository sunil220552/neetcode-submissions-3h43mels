class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        res = { i : float("inf") for i in range(n) }

        res[src] = 0

        for _ in range(n):
            tmp = res.copy()
            for u, v, w in edges:
                if res[v] > res[u] + w:
                    tmp[v] = res[u] + w

            res = tmp

        for n in res:
            if res[n] == float("inf"):
                res[n] = -1

        return res

                


