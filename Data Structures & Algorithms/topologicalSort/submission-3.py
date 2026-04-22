class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}

        for i in range(n):
            adj[i] = []

        for u, v in edges:
            adj[u].append(v)

        visited = set()
        path = set()
        topSort = []

        def dfs(node :int):
            if node in path:
                return False

            if node in visited:
                return True
            
            visited.add(node)
            path.add(node)

            for nb in adj[node]:
                if not dfs(nb):
                    return False
            
            topSort.append(node)
            path.remove(node)
            return True


        for i in range(n):
            if not dfs(i):
                return []
        topSort.reverse()
        return topSort
        