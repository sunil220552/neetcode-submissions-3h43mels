class Node:
    def __init__(self, L, R, total):
        self.L = L
        self.R = R
        self.total = total
        self.left = None
        self.right = None

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = None
        self.buildTree(nums)
        self.dfs()

    def dfs(self):
        def helper(node):
            if not node:
                return None

            helper(node.left)
            print(node.L, node.R, node.total)
            helper(node.right)


    def buildTree(self, nums):

        def helper(L, R):
            if L == R:
                return Node(L, R, nums[L])

            M = (L+R) // 2

            node = Node(L, R, 0)
            node.left = helper(L, M)
            node.right = helper(M+1, R)

            node.total = node.left.total + node.right.total
            return node

        self.root = helper(0, len(nums)-1)
    
    def update(self, index: int, val: int) -> None:

        def helper(node, index, val):
            if node.L == node.R:
                node.total = val
                return
            M = (node.L + node.R) // 2
            if index > M:
                helper(node.right, index, val)
            else:
                helper(node.left, index, val)

            node.total = node.left.total + node.right.total

        helper(self.root, index, val)

    
    def query(self, L: int, R: int) -> int:

        def helper(node, L, R):
            if node.L == L and node.R == R:
                return node.total
            M = (node.L + node.R) // 2
            if L > M:
                return helper(node.right, L, R)
            elif R <= M:
                return helper(node.left, L, R)
            else:
                return helper(node.left, L, M) + helper(node.right, M+1, R)

        return helper(self.root, L, R)
                


