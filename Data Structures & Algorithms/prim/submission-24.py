class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}

        for i in range(n):
            adjList[i] = []

        for u, v, w in edges:
            adjList[u].append((v, w))
            adjList[v].append((u, w))

        minHeap = []

        for n1, w in adjList[0]:
            heapq.heappush(minHeap, (w, 0, n1))

        visited = set()
        visited.add(0)

        wt = 0

        while len(visited) < n and minHeap:
            w, n1, n2 = heapq.heappop(minHeap)
            if n2 in visited:
                continue

            visited.add(n2)
            wt += w

            for nb, w in adjList[n2]:
                if nb not in visited:
                    heapq.heappush(minHeap, (w, n2, nb))

        return wt if len(visited) == n else -1




        