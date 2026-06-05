import heapq
import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []
        for x, y in points:
            d = -1 * math.sqrt(math.pow(x, 2) + math.pow(y, 2))
            heapq.heappush(max_heap, (d, x, y))
            
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        res = []
        
        while max_heap:
            d, x, y = heapq.heappop(max_heap)
            res.append([x, y])
            
        return res 


        