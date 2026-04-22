class Solution:
    def climbStairs(self, n: int) -> int:

        mem = {
            0 : 0, 
            1 : 1,
            2 : 2
        }

        def helper(n : int) -> int:
            if n in mem:
                return mem[n]

            mem[n] = helper(n-1) + helper(n-2)
            return mem[n]

        return helper(n)
        