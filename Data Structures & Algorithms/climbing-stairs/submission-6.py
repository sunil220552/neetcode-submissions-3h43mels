class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        mem = {}
        mem[1] = 1
        mem[2] = 2

        i = 3 

        while i <= n:
            tmp = mem[2]
            mem[2] = mem[2] + mem[1]
            mem[1] = tmp
            i += 1

        return mem[2]
        