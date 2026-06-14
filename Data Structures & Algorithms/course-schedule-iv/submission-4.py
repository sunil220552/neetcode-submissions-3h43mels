class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adList = { i : [] for i in range(numCourses)}

        for a, b in prerequisites:
            adList[b].append(a)

        preReqMap = {}

        def dfs(c:int) -> dict[int:set[int]]:
            if c not in preReqMap:
                preReqMap[c] = set()
                for nb in adList[c]:
                    preReqMap[c] |= dfs(nb)

                preReqMap[c].add(c)

            return preReqMap[c]

        for i in range(numCourses):
            dfs(i)

        res = []
        for u, v in queries:
            res.append(u in preReqMap[v])

        return res

                




        