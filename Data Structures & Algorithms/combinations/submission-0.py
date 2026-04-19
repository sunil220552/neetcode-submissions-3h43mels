class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curCom = []

        def dfs(i: int) -> None:
            if len(curCom) == k:
                res.append(curCom.copy())
                return

            if k > n:
                return

            for j in range(i, n+1):
                curCom.append(j)
                dfs(j+1)
                curCom.pop()


        dfs(1)
        return res
        