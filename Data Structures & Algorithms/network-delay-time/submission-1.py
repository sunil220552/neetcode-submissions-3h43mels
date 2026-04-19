import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        res = {}
        adj = {}

        for i in range(1, n+1):
            adj[i] = []

        for u, v, t in times:
            adj[u].append((t, v))

        minHeap = []

        heapq.heappush(minHeap, (0, k))

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in res:
                continue

            res[n1] = w1

            for w2, n2 in adj[n1]:
                if n2 in res:
                    continue
                heapq.heappush(minHeap, (w1+w2, n2))
        
        return -1 if len(res) != n else max(res.values())



        