class Solution:
    def shortestPath(self, nl: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adList = {}

        for s, d, w in edges:
            if s not in adList:
                adList[s] = []

            if d not in adList:
                adList[d] = []

            adList[s].append((w, d))

        queue = []
        queue.append((0, src))
        shPath = {}

        while queue:
            c, n = heapq.heappop(queue)

            if n in shPath:
                continue

            shPath[n] = c

            for nc, nb in adList[n]:
                if nb in shPath:
                    continue
                heapq.heappush(queue, (c + nc, nb))

        for i in range(nl):
            if i not in shPath:
                shPath[i] = -1


        return shPath

                

            
            


