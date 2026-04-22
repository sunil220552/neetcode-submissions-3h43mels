class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {}
        for i in range(numCourses):
            adj[i] = []

        for a, b in prerequisites:
            adj[a].append(b)

        topSort = []
        visited = set()
        path = set()

        def dfs(node: int) -> bool:
            if node in path:
                return False
            
            if node in visited:
                return True

            path.add(node)
            visited.add(node)

            for nb in adj[node]:
                if not dfs(nb):
                    return False

            topSort.append(node)
            path.remove(node)
            return True 

        for i in range(numCourses):
            if not dfs(i):
                return []

        return topSort
        