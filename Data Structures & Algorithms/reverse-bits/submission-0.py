class Solution:
    def reverseBits(self, n: int) -> int:
        print(n)
        res = []

        ret = 0

        for i in range(32):
            if n & (1 << i):
                res.append(1 << (31-i))
            else:
                res.append(0)
        
        for b in res:
            ret |= b

        return ret
