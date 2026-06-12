# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.ret = None
        self.k = k

        def helper(root:Optional[TreeNode]):
            if root is None:
                return

            if self.ret is not None:
                return


            helper(root.left)
            # process here 
            self.k -= 1
            if self.k == 0:
                self.ret = root.val
            helper(root.right)

        helper(root)

        return self.ret

            
        