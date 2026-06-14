import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adjList = { i: [] for i in range(n)}

        for u, v, w in edges:
            adjList[u].append((v, w))

        minHeap = []

        shortest = {}

        heapq.heappush(minHeap, (0, src))

        while minHeap:
            (w1, v) = heapq.heappop(minHeap)

            if v in shortest:
                continue

            shortest[v] = w1

            for nb, w2 in adjList[v]:
                if nb in shortest:
                    continue

                heapq.heappush(minHeap, (w1+w2, nb))

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest




