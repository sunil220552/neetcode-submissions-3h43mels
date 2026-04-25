class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False

        mem = {}

        target = sum(nums) // 2

        def helper(i :int, tar: int) -> bool:
            if (i, tar) in mem:
                return mem[(i, tar)]

            if tar == 0:
                return True

            if i == len(nums):
                return False


            mem[(i, tar)] = helper(i+1, tar) or helper(i+1, tar-nums[i])
            return mem[(i, tar)]

        return helper(0, target)

            
        