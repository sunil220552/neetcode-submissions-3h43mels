class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adList = {}
        res = {}
        for i in range(n):
            adList[i] = []
            res[i] = -1

        for u, v, w in edges:
            adList[u].append((v, w))


        minHeap = [(0, src)]

        while minHeap:
            w, n = heapq.heappop(minHeap)

            if res[n] != -1:
                continue
            
            res[n] = w

            for nb, w_nb in adList[n]:
                if res[nb] == -1:
                    heapq.heappush(minHeap, (w + w_nb, nb))

        return res

        
