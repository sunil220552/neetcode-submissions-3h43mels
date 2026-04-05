class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        cost = {}
        for i in range(n):
            cost[i] = float("inf")

        cost[src] = 0

        for i in range(n-1):
            tmpCost = cost.copy()
            for u, v, w in edges:
                if cost[u] == float("inf"):
                    continue    
                tmpCost[v] = min( cost[u] + w, tmpCost[v])

            cost = tmpCost

        for i in cost:
            if cost[i] == float('inf'):
                cost[i] = -1

        return cost

        





