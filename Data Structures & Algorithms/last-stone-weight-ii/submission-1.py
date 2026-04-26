class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        total = sum(stones)
        target = total // 2

        memo = {}
        def helper(i : int, curSum: int) -> int:
            if (i, curSum) in memo: return memo[(i, curSum)]
            if i == len(stones):
                return curSum
            
            res = helper(i + 1, curSum)
            if curSum + stones[i] <= target:
                res = max(res, helper(i + 1, curSum + stones[i]))
            
            memo[(i, curSum)] = res
            return res

        best_sum = helper(0, 0)
        return total - 2 * best_sum