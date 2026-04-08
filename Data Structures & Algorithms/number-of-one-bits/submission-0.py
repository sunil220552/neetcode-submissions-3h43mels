class Solution:
    def hammingWeight(self, n: int) -> int:

        cnt = 0

        while n:
            if 1 & n:
                cnt += 1

            n = n >> 1

        return cnt
        