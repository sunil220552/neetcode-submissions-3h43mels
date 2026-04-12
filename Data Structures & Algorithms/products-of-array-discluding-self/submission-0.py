class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefixProd = []
        postfixProd = [1] * len(nums)

        prod = 1 

        for n in nums:
            prod *= n
            prefixProd.append(prod)

        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            postfixProd[i] = prod

        res = []

        for i in range(len(nums)):
            leftProd = prefixProd[i-1] if i > 0 else 1
            rightProd = postfixProd[i+1] if i < (len(nums)-1) else 1

            res.append(leftProd * rightProd)

        return res




                
 

        