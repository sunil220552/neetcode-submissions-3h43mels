"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node
        old2new = {}

        visited = set()
        def dfs(node: Optional['Node']) -> None:
            if not node:
                return
            if node in visited:
                return

            visited.add(node)

            old2new[node] = Node(node.val)

            for nb in node.neighbors:
                dfs(nb)




        dfs(node)

        for n in old2new.keys():
            for nb in n.neighbors:
                old2new[n].neighbors.append(old2new[nb])

        return old2new[node]

        