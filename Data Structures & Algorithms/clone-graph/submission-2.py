"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        org2New = {}

        def dfs(node) -> None:
            if node is None:
                return

            if node in org2New:
                return

            org2New[node] = Node(node.val)
            for nb in node.neighbors:
                dfs(nb)
                org2New[node].neighbors.append(org2New[nb])

        dfs(node)

        return org2New[node]

            
        