class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.im = image

        if self.im[sr][sc] == color:
            return self.im

        self.dfs(sr, sc, color, self.im[sr][sc])

        return self.im


    def dfs(self, sr: int, sc: int, color: int, stC: int):
        ROW, COL = len(self.im), len(self.im[0])
        if sr < 0 or sc < 0 or sr == ROW or sc == COL or self.im[sr][sc] != stC:
            return

        self.im[sr][sc] = color
        self.dfs(sr+1, sc, color, stC)
        self.dfs(sr-1, sc, color, stC)
        self.dfs(sr, sc+1, color, stC)
        self.dfs(sr, sc-1, color, stC)