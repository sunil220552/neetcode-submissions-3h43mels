class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_min = 1
        k_max = max(piles)

        res = k_max

        while k_min <= k_max:
            k = (k_min + k_max) // 2
            totalHr = 0

            for p in piles:
                totalHr += p // k
                if p % k > 0:
                    totalHr += 1

            if totalHr > h:
                k_min = k + 1
            else:
                res = k
                k_max = k - 1

        return res





        