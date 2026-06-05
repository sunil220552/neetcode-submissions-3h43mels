# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def helper(s:int, e:int) -> None:
            if e - s + 1 <= 1:
                return

            pivot = pairs[e]
            left = s

            for i in range(s, e):
                if pairs[i].key < pivot.key:
                    pairs[left], pairs[i] = pairs[i], pairs[left]
                    left += 1

            pairs[e], pairs[left] = pairs[left], pivot

            helper(s, left-1)
            helper(left+1, e)


        helper(0, len(pairs)-1)

        return pairs

        





            

                
        