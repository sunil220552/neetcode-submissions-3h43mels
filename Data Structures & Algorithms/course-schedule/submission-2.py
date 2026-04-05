class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqMap = {}

        for a, b in prerequisites:
            if a not in reqMap:
                reqMap[a] = []

            if b not in reqMap:
                reqMap[b] = []

            reqMap[a].append(b)


        visited = set()
        def dfs(node: int) -> bool:
            if not reqMap[node]:
                return True

            if node in visited:
                return False

            visited.add(node)

            for req in reqMap[node]:
                if not dfs(req):
                    return False

            visited.remove(node)

            reqMap[node] = []
            
            return True

        for req in reqMap.keys():
            if not dfs(req):
                return False

        return True