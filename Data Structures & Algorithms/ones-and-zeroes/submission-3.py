class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        mem = {}
        def helper(i: int, mCnt: int, nCnt: int) -> int:
            key = (i, mCnt, nCnt)
            if key in mem:
                return mem[key]

            if i == len(strs):
                return 0

            # Option 1: Skip the current string
            res = helper(i+1, mCnt, nCnt)

            # Count 0s and 1s in current string
            zeros = strs[i].count('0')
            ones = strs[i].count('1')

            # Option 2: Include the current string (if it fits)
            if mCnt + zeros <= m and nCnt + ones <= n:
                res = max(res, 1 + helper(i+1, mCnt + zeros, nCnt + ones))

            mem[key] = res
            return mem[key]

        return helper(0, 0, 0)