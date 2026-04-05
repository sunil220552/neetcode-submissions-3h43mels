class Solution:

    def climbStairs(self, n: int, memo = {}) -> int:
        

        baseCase = {
            0 : 0, 
            1 : 1,
            2 : 2
        }

        if n in baseCase.keys():
            return baseCase[n]

        if n in memo:
            return memo[n]

        memo[n-1] = self.climbStairs(n-1)
        memo[n-2] = self.climbStairs(n-2)

        return memo[n-1] + memo[n-2]
        