import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._min_heap = []
        self._k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        
        heapq.heappush(self._min_heap, val)
        
        if len(self._min_heap) > self._k:
            heapq.heappop(self._min_heap)
            
        return self._min_heap[0]