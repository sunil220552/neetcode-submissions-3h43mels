class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        L1, L2 = len(text1), len(text2)

        import functools

        @functools.lru_cache(maxsize=None)
        def helper(i: int, j: int) -> int:
            if i == L1 or j == L2:
                return 0

            if text1[i] == text2[j]:
                return 1 + helper(i+1, j+1)
            else:
                return max(helper(i, j+1), helper(i+1, j))

        return helper(0, 0)
        