class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        print(freq)

        maxHeap = []
        for key, v in freq.items():
            heapq.heappush(maxHeap, (-1 * v, key))

        print(maxHeap)

        res = []
        while len(res) < k:
            v, key = heapq.heappop(maxHeap)
            print("----")
            print(key)
            print(v)
            res.append(key)

        return res