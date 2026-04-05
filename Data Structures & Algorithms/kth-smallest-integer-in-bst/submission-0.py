# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.n = 0

        self.helper(root, k)
        return self.res

    def helper(self, root: Optional[TreeNode], k: int) -> None:
        if self.res != None:
            return

        if not root:
            return

        self.helper(root.left, k)
        self.n += 1
        if self.n == k:
            self.res = root.val
        self.helper(root.right, k)

        
        