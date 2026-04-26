class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        L1, L2 = len(word1), len(word2)

        import functools
        @functools.lru_cache(maxsize=None)
        def helper(i: int, j: int) -> int:
            if i == L1:
                return L2 - j
            if j == L2:
                return L1 - i

            if word1[i] == word2[j]:
                return helper(i+1, j+1)
            else:
                return min(1+helper(i+1, j), 1+helper(i+1, j+1), 1+helper(i, j+1) )
        return helper(0, 0)