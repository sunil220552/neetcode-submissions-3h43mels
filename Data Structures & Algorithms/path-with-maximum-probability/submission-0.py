import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        res = {}

        for i in range(n):
            adj[i] = []

        for i, [a, b] in enumerate(edges):
            adj[a].append((succProb[i], b))
            adj[b].append((succProb[i], a))

        maxHeap = []

        heapq.heappush(maxHeap, (-1, start_node))

        while maxHeap:
            p1, n1 = heapq.heappop(maxHeap)

            if n1 in res:
                continue

            p1 *= -1
            res[n1] = p1

            for p2, n2 in adj[n1]:
                if n2 in res:
                    continue
                
                heapq.heappush(maxHeap, (p1*p2*-1, n2))

        return res[end_node] if end_node in res else 0
        