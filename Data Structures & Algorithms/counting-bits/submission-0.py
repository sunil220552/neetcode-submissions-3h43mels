class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(0, n+1):
            cnt = 0
            while i: 
                if i & 1:
                    cnt += 1

                i = i >> 1

            res.append(cnt)

        return res