class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:

        adList = { i:[] for i in range(n) }

        for s, d in edges:
            adList[s].append(d)

        topSort = []
        visit = set()
        path = set()

        def dfs(node):
            if node in path:
                return False

            if node in visit:
                return True
            
            visit.add(node)
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

        


        
        