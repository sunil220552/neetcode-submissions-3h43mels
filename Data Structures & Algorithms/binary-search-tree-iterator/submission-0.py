class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.cur = root
        self.stack = []

    def next(self) -> int:
        while self.cur or self.stack:
            while self.cur:
                self.stack.append(self.cur)
                self.cur = self.cur.left

            self.cur = self.stack.pop()
            res = self.cur.val

            self.cur = self.cur.right
            return res

    def hasNext(self) -> bool:
        return self.cur is not None or len(self.stack) > 0