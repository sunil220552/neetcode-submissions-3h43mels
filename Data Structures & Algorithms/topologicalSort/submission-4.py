class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(n)}

        for u, v in edges:
            adjList[u].append(v)

        visited = set()
        path = set()

        topSort = []

        def dfs(node: int) -> bool:
            if node in path:
                return False

            if node in visited:
                return True

            visited.add(node)
            path.add(node)

            for nb in adjList[node]:
                if not dfs(nb):
                    return False

            path.remove(node)
            topSort.append(node)

            return True

        for i in range(n):
            if i not in visited:
                if not dfs(i):
                    return []
            
        topSort.reverse()
        return topSort
        