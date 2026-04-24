class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {
            (m-1, n-1) : 1
        }

        def helper(r: int, c: int) -> int:
            if (r,c) in mem:
                return mem[(r, c)]

            if min(r, c) < 0 or r == m or c == n:
                return 0

            mem[(r, c)] = helper(r + 1, c) + helper(r, c+1)

            return mem[(r, c)]

        return helper(0, 0)


            

            


        