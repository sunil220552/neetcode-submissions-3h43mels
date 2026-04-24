class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, R = 0, 0

        res = 0

        freq = {}

        while R < len(s):
            freq[s[R]] = freq.get(s[R], 0) + 1

            while sum(freq.values()) - max(freq.values()) > k:
                freq[s[L]] -= 1
                if freq[s[L]] <= 0:
                    del freq[s[L]] 
                L += 1

            res = max(res, R-L+1)
            R += 1

        return res
        
        

            

        