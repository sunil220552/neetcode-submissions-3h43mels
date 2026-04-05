# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.helper(pairs, 0, len(pairs)-1)

    def helper(self, pairs: List[Pair], s, e) -> List[Pair]:

        if e - s + 1 <= 1:
            return pairs 
        
        pivot = pairs[e].key
        left = s

        for i in range(s, e):
            if pairs[i].key < pivot:
                tmp = pairs[i] 
                pairs[i] = pairs[left]
                pairs[left] = tmp
                left += 1

        tmp = pairs[left]
        pairs[left] = pairs[e]
        pairs[e] = tmp

        self.helper(pairs, s, left-1)
        self.helper(pairs, left+1, e)
        return pairs



        