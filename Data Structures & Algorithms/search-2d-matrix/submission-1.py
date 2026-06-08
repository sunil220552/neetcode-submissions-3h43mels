class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r, c = len(matrix), len(matrix[0])

        L, H = 0, r-1
        M = L
        while L <= H:
            M = (L + H) // 2 
            if matrix[M][0] > target:
                H = M - 1
            elif matrix[M][0] < target:
                L = M + 1
            else:
                return True

        if matrix[M][0] > target:
            M -= 1

        L, H = 0, c - 1

        while L <= H:
            m = (L + H) // 2
            if  matrix[M][m] > target:
                H = m - 1
            elif matrix[M][m] < target:
                L = m + 1
            else:
                return True

        return False


         
        