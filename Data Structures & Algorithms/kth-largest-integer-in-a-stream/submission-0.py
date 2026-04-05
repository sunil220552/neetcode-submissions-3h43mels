class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._heap = [0]
        self._k = k
        for n in nums:
            self.addHeap(n)

    def addHeap(self, val: int) -> None:
        self._heap.append(val)
        i = len(self._heap) - 1
        while i > 1 and self._heap[i] < self._heap[i//2]:
            tmp = self._heap[i//2] 
            self._heap[i//2] = self._heap[i]
            self._heap[i] = tmp
            i = i // 2
        if len(self._heap) > self._k + 1:
            self.popHeap()

    def popHeap(self) -> int:
        if len(self._heap) <= 1:
            return None
        if len(self._heap) == 2:
            return self._heap.pop()
        val = self._heap[1]
        self._heap[1] = self._heap.pop()

        i = 1
        while 2*i < len(self._heap):
            child = 2*i
            if child + 1 < len(self._heap) and self._heap[child + 1] < self._heap[child]:
                child += 1
            if self._heap[child] < self._heap[i]:
                tmp = self._heap[i]
                self._heap[i] = self._heap[child]
                self._heap[child] = tmp
                i = child
            else:
                break
        return val

    def add(self, val: int) -> int:
        self.addHeap(val)
        return self._heap[1]