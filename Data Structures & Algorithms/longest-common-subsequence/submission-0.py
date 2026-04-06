class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = {}

        def sol(i: int, j:int) -> int:
            if i == len(text1) or j == len(text2):
                return 0

            key = (i, j)

            if key in cache:
                return cache[key]

            if text1[i] == text2[j]:
                res =  1 + sol(i+1, j+1)

            else:
                res = max(sol(i, j+1), sol(i+1, j))

            cache[key] = res
            return res

        return sol(0, 0)

    