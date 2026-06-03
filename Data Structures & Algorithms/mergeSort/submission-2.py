# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def helper(S:int, E:int) -> None:
            if E - S + 1 <= 1:
                return

            M = (S + E) // 2

            helper(S, M)
            helper(M+1, E)

            merge(S, M, E)


        def merge(S:int, M:int, E:int) -> None:
            L = pairs[S:M+1]
            R = pairs[M+1:E+1]

            i, j, k = 0, 0, S

            while i < len(L) and j < len(R):
                if L[i].key <= R[j].key:
                    pairs[k] = L[i]
                    k += 1
                    i += 1
                else:
                    pairs[k] = R[j]
                    k += 1
                    j += 1

            while i < len(L):
                pairs[k] = L[i]
                k += 1
                i += 1

            while j < len(R):
                pairs[k] = R[j]
                k += 1
                j += 1

        helper(0, len(pairs)-1)
        return pairs

        






