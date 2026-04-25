class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        L1, L2 = len(text1), len(text2)

        mem = {}

        def helper(i, j):
            if i == L1 or j == L2:
                return 0
            if (i, j) in mem:
                return mem[(i, j)]

            if text1[i] == text2[j]:
                mem[(i, j)] =  1 + helper(i+1, j+1)
            else:
                mem[(i, j)] = max(helper(i, j+1), helper(i+1, j))

            return mem[(i, j)]

        return helper(0, 0)

        

            


        