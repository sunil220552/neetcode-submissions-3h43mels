import functools
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @functools.lru_cache(maxsize=None)
        def helper(i, j)-> int:
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0

            res = helper(i+1, j)

            if s[i] == t[j]:
                res += helper(i+1, j+1)

            return res

        return helper(0, 0)

        
        