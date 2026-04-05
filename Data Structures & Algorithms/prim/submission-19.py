class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}
        for i in range(n):
            adjList[i] = []

        for u, v, w in edges:
            adjList[u].append((v, w))
            adjList[v].append((u, w))

        minHeap = []

        for d, w in adjList[0]:
            minHeap.append((w, 0, d))

        heapq.heapify(minHeap)

        mst = []
        visited = set()
        visited.add(0)
        cost = 0
        while minHeap:
            print(visited, minHeap)
            w, s, d = heapq.heappop(minHeap)
            if d in visited:
                continue
            mst.append((s, d))
            visited.add(d)
            cost += w

            for nd, w1 in adjList[d]:
                if nd in visited:
                    continue
                heapq.heappush(minHeap, (w1, d, nd))

        return cost if len(mst) == n-1 else -1



        