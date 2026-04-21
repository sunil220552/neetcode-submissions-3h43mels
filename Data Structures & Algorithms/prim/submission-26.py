import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:

        adj = {}

        for i in range(n):
            adj[i] = []

        for u, v, w in edges:
            adj[u].append((w, v))
            adj[v].append((w, u))

        minHeap = []
        visited = set()
        res = 0

        for w, nb in adj[0]:
            heapq.heappush(minHeap, ((w, 0, nb)))

        visited.add(0)

        while minHeap:
            w, n1, n2 = heapq.heappop(minHeap)
            if n2 in visited:
                continue
            visited.add(n2)

            res += w

            for w1, nb in adj[n2]:
                if nb in visited:
                    continue

                heapq.heappush(minHeap, (w1, n2, nb))

        return res if len(visited) == n else -1

                
                

        

        