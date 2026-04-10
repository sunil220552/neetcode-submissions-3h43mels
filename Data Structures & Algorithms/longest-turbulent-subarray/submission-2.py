class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        L = 0
        prev = None
        for R in range(1, len(arr)):
            if arr[R] == arr[R-1]:
                L = R
                prev = None
                continue
            cur = arr[R] > arr[R-1]
            if prev == None:
                prev = not cur

            if prev == cur:
                L = R-1
                prev = cur
            else:
                prev = cur

            res = max(res, R-L+1)

        return res
