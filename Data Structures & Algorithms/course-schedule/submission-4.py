class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = {i:[] for i in range(numCourses)}

        for a, b in prerequisites:
            preReqMap[a].append(b)

        visited = set()

        def dfs(crs:int) -> bool:

            if crs in visited:
                return False

            if len(preReqMap[crs]) == 0:
                return True

            visited.add(crs)

            for nb in preReqMap[crs]:
                if not dfs(nb):
                    return False

            visited.remove(crs)
            preReqMap[crs] = []

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


            

            




        