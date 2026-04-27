class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # helper(i, j) returns len of longerst sub-seq between text1[i:] and text2[j:].
        import functools
        @functools.lru_cache(maxsize=None)
        def helper(i: int, j:int) -> int:
            # basecase
            # If either strings are empty, no common subseq can exists
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + helper(i+1, j+1)
            else:
                return max(helper(i+1, j), helper(i, j+1))

        return helper(0, 0)
        


        