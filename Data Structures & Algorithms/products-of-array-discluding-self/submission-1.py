class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        preFix = [1] * len(nums) 
        postFix = [1] * len(nums)

        for i in range(1, len(preFix)):
            preFix[i] = preFix[i-1] * nums[i-1]

        for j in range(len(postFix)-2, -1, -1):
            postFix[j] = postFix[j+1] * nums[j+1]

        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = preFix[i] * postFix[i]

        return res


        