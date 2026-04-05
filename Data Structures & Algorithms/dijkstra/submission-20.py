class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = {}

        for i in range(n):
            adjList[i] = []


        for u, v, w in edges:
            adjList[u].append((v, w))

        minHeap = [(0, src)]

        stDist = {}
        while minHeap:
            w, n1 = heapq.heappop(minHeap)

            if n1 in stDist:
                continue

            stDist[n1] = w

            for n2, w2 in adjList[n1]:
                if n2 in stDist:
                    continue
                heapq.heappush(minHeap, (w+w2, n2))

        for i in range(n):
            if i not in stDist:
                stDist[i] = -1

        return stDist

                

            

