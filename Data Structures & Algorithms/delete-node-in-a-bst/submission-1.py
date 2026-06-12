# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Any
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def findMin(root:TreeNone) -> Any:
            while root.left:
                root = root.left

            return root.val


        def helper(root:Optional[TreeNode]) -> Optional[TreeNode]:
            if root is None:
                return root

            if key < root.val:
                root.left = helper(root.left)
            elif key > root.val:
                root.right = helper(root.right)
            else:
                if root.right is None:
                    return root.left
                
                if root.left is None:
                    return root.right

                minVal = findMin(root.right)

                root.right = self.deleteNode(root.right, minVal)

                root.val = minVal
            return root

        return helper(root)
                
        