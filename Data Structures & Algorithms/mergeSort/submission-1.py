# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.helper(pairs, 0, len(pairs)-1)

    def helper(self, pairs: List[Pair], s, e) -> List[Pair]:
        if e - s + 1 <= 1:
            return pairs

        mid = (s + e) // 2 

        self.helper(pairs, s, mid)
        self.helper(pairs, mid+1, e)

        self.merge(pairs, s, mid, e)

        return pairs 

    def merge(self, pairs, s, m, e):
        L = pairs[s:m+1]
        R = pairs[m+1:e+1]

        i = 0
        j = 0
        k = s

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1
            
            k += 1

        if i < len(L):
            while i < len(L):
                pairs[k] = L[i]
                k += 1
                i += 1
        elif j < len(R):
            while j < len(R):
                pairs[k] = R[j]
                k += 1
                j += 1
        return pairs





        


