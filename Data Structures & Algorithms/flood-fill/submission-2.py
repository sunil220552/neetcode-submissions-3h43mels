class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        ROW, COL = len(image), len(image[0])

        visited = set()

        def dfs(r, c, or_color, target_color) -> None:

            if min(r, c) < 0 or r == ROW or c == COL or (r, c) in visited or image[r][c] != or_color:
                return

            visited.add((r, c))
            image[r][c] = target_color

            for rd, cd in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r+rd, c+cd, or_color, target_color)

        dfs(sr, sc, image[sr][sc], color)

        return image
        