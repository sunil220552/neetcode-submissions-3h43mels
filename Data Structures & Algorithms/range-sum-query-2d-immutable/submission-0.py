class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.preFixSum = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for r in range(len(matrix)):
            total = 0
            for c in range(len(matrix[0])):
                total += matrix[r][c]
                self.preFixSum[r][c] = total

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = col1
        right = col2
        res = 0
        for r in range(row1, row2+1):
            leftSum = self.preFixSum[r][left-1] if left > 0 else 0
            rightSum = self.preFixSum[r][right]
            res += (rightSum - leftSum)

        return res
