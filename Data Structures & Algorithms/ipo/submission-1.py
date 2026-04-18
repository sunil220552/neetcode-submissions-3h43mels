import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        capHeap = []
        profHeap = []

        for i, cap in enumerate(capital):
            heapq.heappush(capHeap, (cap, i))

        num = 0

        while num < k:
            while capHeap and w >= capHeap[0][0]:
                cap, i = heapq.heappop(capHeap)
                heapq.heappush(profHeap, -1 * profits[i])

            if not profHeap:
                break

            if profHeap:
                w += -1 * heapq.heappop(profHeap)
                num += 1

        return w






        