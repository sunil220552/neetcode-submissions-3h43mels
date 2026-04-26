class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        L1, L2, L3 = len(s1), len(s2), len(s3)

        if L1 + L2 != L3:
            return False

        import functools

        @functools.lru_cache(maxsize=None)
        def helper(i: int, j: int, k: int) -> bool:
            if (i, j, k) == (L1, L2, L3):
                return True

            if i < L1 and k < L3 and s1[i] == s3[k]:
                if helper(i+1, j, k+1):
                    return True

            if j < L2 and k < L3 and s2[j] == s3[k]:
                if helper(i, j+1, k+1):
                    return True

            
            return False

        return helper(0, 0, 0)