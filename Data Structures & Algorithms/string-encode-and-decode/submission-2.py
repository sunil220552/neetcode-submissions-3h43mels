class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "None"
        res = ""

        for word in strs:
            res += str(len(word)) + "|" + word 
        return res

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        i = 0

        res = []
        while i < len(s):
            j = i
            while s[j] != "|":
                j += 1

            cnt = int(s[i:j])
            res.append(s[j+1:j+1+cnt])

            i = j+1+cnt

        return res