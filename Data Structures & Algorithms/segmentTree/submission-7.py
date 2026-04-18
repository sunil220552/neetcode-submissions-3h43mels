class ST:
    def __init__(self, total, L, R):
        self.total = total
        self.L, self.R = L, R
        self.left, self.right = None, None

    @staticmethod
    def build(nums, L, R):
        if L == R:
            return ST(nums[L], L, R)

        root = ST(0, L, R)
        M = (L + R) // 2
        root.left = ST.build(nums, L, M)
        root.right = ST.build(nums, M+1, R)
        root.total = root.left.total + root.right.total
        return root

    def update(self, index, value):
        if self.L == self.R:
            self.total = value
            return

        M = (self.L + self.R) // 2
        if index > M:
            self.right.update(index, value)
        else:
            self.left.update(index, value)

        self.total = self.left.total + self.right.total

    def query(self, L : int, R : int) -> int:
        if L == self.L and self.R == R:
            return self.total

        M = (self.L + self.R) // 2

        if R <= M:
            return self.left.query(L, R)
        elif L > M:
            return self.right.query(L, R)
        else:
            return self.left.query(L, M) + self.right.query(M+1, R)
            


class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.st = ST.build(nums, 0, len(nums)-1)

    def update(self, index: int, val: int) -> None:
        self.st.update(index, val)

    def query(self, L: int, R: int) -> int:
        return self.st.query(L, R)