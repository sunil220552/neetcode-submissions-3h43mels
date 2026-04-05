class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adjList = {}
        for s, d, w in edges:
            if s not in adjList:
                adjList[s] = []

            if d not in adjList:
                adjList[d] = []

            adjList[s].append((w, d))

        minHeap = [(0, src)]

        shPath = {}

        while minHeap:
            w1, dst = heapq.heappop(minHeap)
            if dst in shPath:
                continue

            shPath[dst] = w1

            for w2, nb in adjList[dst]:
                if nb not in shPath:
                    heapq.heappush(minHeap, (w1+w2, nb))

        for i in range(n):
            if i not in shPath:
                shPath[i] = -1


        return shPath

            


