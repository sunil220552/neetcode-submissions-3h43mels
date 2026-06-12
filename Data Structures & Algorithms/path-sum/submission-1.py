# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def helper(node:Optional[TreeNode], curSum: int) -> bool:

            if node is None:
                return False

            if node.right is None and node.left is None:
                return curSum + node.val == targetSum 
            return helper(node.right, curSum + node.val ) or helper(node.left, curSum + node.val)

        return helper(root, 0)
        