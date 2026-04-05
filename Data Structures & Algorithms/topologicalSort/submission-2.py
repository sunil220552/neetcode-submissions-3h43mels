class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adList = {}

        for i in range(n):
            adList[i] = []

        for u, v in edges:
            adList[u].append(v)

        topSort = []
        visited = set()
        path = set()

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True

            visited.add(node)
            path.add(node)

            for nb in adList[node]:
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
        

            

        