class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        import functools
        # is s[i:] is beakable by using wordDict ?
        @functools.lru_cache(maxsize=None)
        def helper(i) -> bool:
            if i == len(s):
                return True

            for j in range(i+1, len(s)+1):
                if s[i:j] in wordSet and helper(j):
                    return True

            return False

        return helper(0)
        