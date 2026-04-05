class Solution:
    def climbStairs(self, n: int) -> int:

        mem = {}

        def solution(n: int) -> int:
            if n <= 2:
                return n

            if n in mem:
                return mem[n]

            mem[n] = solution(n-1) + solution(n-2)

            return mem[n]

        return solution(n)
        