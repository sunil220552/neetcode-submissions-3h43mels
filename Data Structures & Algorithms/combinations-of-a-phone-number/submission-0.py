class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d2c = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"            
        }

        res = []
        curComb = []

        def dfs(i : int) -> None:
            if len(curComb) == len(digits):
                tmp = "".join(curComb.copy())
                if tmp:
                    res.append("".join(curComb.copy()))
                return

            if len(curComb) > len(digits):
                return 

            if i >= len(digits):
                return
            
            for c in d2c[digits[i]]:
                curComb.append(c)
                dfs(i+1)
                curComb.pop()

        dfs(0)
        return res

        