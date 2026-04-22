class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        if len(words) == 1:
            # Return only the unique characters of the single word
            return "".join(dict.fromkeys(words[0]))
        edges = []
        vertex = set()

        adj = {}

        for word in words:
            for c in word:
                if c not in vertex:
                    vertex.add(c)
                    adj[c] = []

        for w1, w2 in zip(words, words[1:]):
            # Check for invalid prefix cases like ["abc", "ab"]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for i in range(min(len(w1), len(w2))):
                if w1[i] == w2[i]:
                    continue
                adj[w1[i]].append(w2[i])
                break
                

        topSort = []

        path = set()
        visited = set()

        def dfs(c : str) -> bool:
            if c in path:
                return False 

            if c in visited:
                return True

            path.add(c)
            visited.add(c)

            for nb in adj[c]:
                if not dfs(nb):
                    return False

            topSort.append(c)
            path.remove(c)
            return True

        for c in sorted(vertex, reverse=True):
            if c not in visited:
                if not dfs(c):
                    return ""

        topSort.reverse()
        return "".join(topSort)