class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        L = 0
        cnt = 0

        curSum = 0

        for R in range(len(arr)):
            curSum += arr[R]
            if (R - L + 1 == k):
                if curSum / k >= threshold:
                    cnt += 1
                curSum -= arr[L]
                L += 1

        return cnt


        