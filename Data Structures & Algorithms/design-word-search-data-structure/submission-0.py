class TreeNode(object):
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.word = True
        

    def search(self, word: str) -> bool:

        def dfs(node: TreeNode, i: int) -> bool:
            if i == len(word):
                return node.word

            if word[i] == '.':
                for n in node.children.values():
                    if dfs(n, i+1):
                        return True
            else:
                if word[i] in node.children:
                    return dfs(node.children[word[i]], i+1)

            return False

        return dfs(self.root, 0)
