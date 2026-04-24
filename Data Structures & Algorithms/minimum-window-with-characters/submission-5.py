class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqT = {}

        intChars = set()

        for c in t:
            freqT[c] = freqT.get(c, 0) + 1
            intChars.add(c)

        freqS = {}

        L, R = 0, 0

        ret = ""

        while R < len(s):

            freqS[s[R]] = freqS.get(s[R], 0) + 1

            while self.isValid(freqS, freqT):
                if ret == "" or (R - L + 1) < len(ret):
                    ret = s[L:R+1]
                freqS[s[L]] -= 1
                if freqS[s[L]] <= 0:
                    del freqS[s[L]]
                L += 1

            R += 1

        return ret

    def isValid(self, freqS, freqT):
        for k, v in freqT.items():
            if k not in freqS or freqS[k] < v:
                return False

        return True



            
                





        