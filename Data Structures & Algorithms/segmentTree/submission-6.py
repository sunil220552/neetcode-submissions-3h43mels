class ST(object):
    def __init__(self, total, L, R):
        self.total, self.L, self.R = total, L, R
        self.left, self.right = None, None

    @staticmethod
    def build(nums, L, R):
        if L == R:
            return ST(nums[L], L, R)

        M = (L + R) // 2

        root = ST(0, L, R)
        root.left = ST.build(nums, L, M)
        root.right = ST.build(nums, M+1, R)
        root.total = root.left.total + root.right.total
        return root

    def update(self, index, val):
        if self.L == self.R:
            self.total = val
            return

        M = (self.L + self.R) // 2

        if index > M:
            self.right.update(index, val)
        else:
            self.left.update(index, val)

        self.total = self.left.total + self.right.total

    def query(self, L, R):
        if self.L == L and self.R == R:
            return self.total

        M = (self.L + self.R) // 2

        if L > M:
            return self.right.query(L, R)
        elif R <= M:
            return self.left.query(L, R)
        else:
            return self.left.query(L, M) + self.right.query(M+1, R)


class SegmentTree:    
    def __init__(self, nums: List[int]):
        self.st = ST.build(nums, 0, len(nums)-1)

    
    def update(self, index: int, val: int) -> None:
        self.st.update(index, val)

    
    def query(self, L: int, R: int) -> int:
        return self.st.query(L, R)
