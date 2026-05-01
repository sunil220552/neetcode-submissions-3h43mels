import functools
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @functools.lru_cache(maxsize=None)
        def helper(i, j) -> int:

            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return helper(i+1, j+1)
            else:
                return 1 + min(helper(i, j+1), helper(i+1, j), helper(i+1, j+1))

        return helper(0, 0)

        

