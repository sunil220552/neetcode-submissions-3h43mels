class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}
        
        for word in strs:
            sg = self.sig(word)
            if sg in res:
                res[sg].append(word)
            else:
                res[sg] = [word]

        ret = []

        for v in res.values():
            ret.append(v)

        return ret


    def sig(self, word: str) -> str:
        sig = {}

        res = ""

        for c in word:
            sig[c] = sig.get(c, 0) + 1

        chars = list(sig.keys())
        chars.sort()
        
        for c in chars:
            res += c + str(sig[c])

        return res

        