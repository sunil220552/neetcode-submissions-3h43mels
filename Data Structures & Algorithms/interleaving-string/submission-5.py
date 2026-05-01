import functools
class Solution:
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        L1, L2, L3 = len(s1), len(s2), len(s3)

        @functools.lru_cache(maxsize=None)
        def helper(i, j, k) -> bool:
            if (i, j, k) == (L1, L2, L3):
                return True

            ret = False
            if i < L1 and k < L3 and s1[i] == s3[k]:
                ret = ret or helper(i+1, j, k+1)

            if j < L2 and  k < L3 and s2[j] == s3[k]:
                ret = ret or helper(i, j+1, k+1)

            return ret 
        
        return helper(0, 0, 0)

        
        