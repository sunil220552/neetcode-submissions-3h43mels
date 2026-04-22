class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.freq(s) == self.freq(t)

    def freq(self, word:str) -> dict[str, int]:
        res = {}
        for c in word:
            res[c] = res.get(c, 0) + 1

        return res
        