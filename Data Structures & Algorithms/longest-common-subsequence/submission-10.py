import functools
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # if text1[i] == text[j]:
        #     1 + solution(text1[i+1], text[j+1])
        # else:
        #     max(solution(text1[i], text[j+1]), solution(text1[i], text[j+1]))
        @functools.lru_cache(maxsize=None)
        def helper(i, j) -> int:
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + helper(i+1, j+1)
            else:
                return max(helper(i, j+1), helper(i+1, j))

        return helper(0, 0)

        