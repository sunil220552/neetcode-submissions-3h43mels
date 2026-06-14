import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adjList = { i: [] for i in range(n) }
        for u, v, w in edges:
            adjList[u].append((v, w))

        minHeap = []
        shortest = {}

        heapq.heappush(minHeap, (0, src))

        while minHeap:
            w, node = heapq.heappop(minHeap)

            if node in shortest:
                continue

            shortest[node] = w

            for nb, w1 in adjList[node]:
                if nb in shortest:
                    continue

                heapq.heappush(minHeap, (w + w1, nb))

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest
