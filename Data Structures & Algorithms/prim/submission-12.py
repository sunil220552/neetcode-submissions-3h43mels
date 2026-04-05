class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:

        adList = {}
        for i in range(n):
            adList[i] = []

        for s, d, w in edges:
            adList[s].append((d, w))
            adList[d].append((s, w))

        minHeap = []
        visited = set()

        for d, w in adList[0]:
            minHeap.append((w, 0, d))

        heapq.heapify(minHeap)
        visited.add(0)

        cost = 0

        while minHeap:
            wt, s, d = heapq.heappop(minHeap)

            if d in visited:
                continue

            visited.add(d)
            cost += wt

            for nb, wt in adList[d]:
                if nb in visited:
                    continue

                heapq.heappush(minHeap, (wt, d, nb))

        if len(visited) == n:
            return cost
        else:
            return -1
            

            

        