# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.targetSum = targetSum

        return self.helper(root)

    
    def helper(self, root : Optional(TreeNode), curSum = 0) -> bool:
        if not root:
            return False

        curSum += root.val

        if not root.left and not root.right:
            return curSum == self.targetSum

        return self.helper(root.left, curSum) or self.helper(root.right, curSum)
        