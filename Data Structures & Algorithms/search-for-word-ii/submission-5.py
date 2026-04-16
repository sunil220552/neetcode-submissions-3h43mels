class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def isPrefix(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]
        return True

    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]
        return cur.word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()
        for w in words:
            trie.add(w)

        ROW, COL = len(board), len(board[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        res = set()

        visited = set()
        def dfs(r, c, path = ""):
            if r < 0 or c < 0 or r == ROW or c == COL or (r,c) in visited:
                return

            path += board[r][c]
            if not trie.isPrefix(path):
                return
            
            if trie.search(path):
                res.add(path) 

            visited.add((r,c))
            for rd, cd in direction:
                dfs(r+rd, c+cd, path)

            visited.remove((r,c))
        
        for r in range(ROW):
            for c in range(COL):
                dfs(r, c)

        return list(res)