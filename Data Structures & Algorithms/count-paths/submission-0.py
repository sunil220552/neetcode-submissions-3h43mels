class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = {}

        def dfs(r:int, c:int) -> int:
            if r == m or c == n:
                return 0
            if r == m-1 and c == n-1:
                return 1

            key = tuple([r,c])

            if key in cache:
                return cache[key]

            cache[key] = dfs(r+1, c) + dfs(r, c+1)
            return cache[key]
        
        return dfs(0, 0)

        