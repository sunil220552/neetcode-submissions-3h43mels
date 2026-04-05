class Graph:
    
    def __init__(self):
        # src : set(dst)
        self.adList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adList:
            self.adList[src] = set()

        if dst not in self.adList:
            self.adList[dst] = set()

        self.adList[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adList and dst in self.adList[src]:
            self.adList[src].remove(dst)
            return True
        return False


    def hasPath(self, src: int, dst: int) -> bool:

        visited = set()

        def helper(node):

            if node == dst:
                return True

            visited.add(node)

            for nd in self.adList[node]:
                if helper(nd):
                    return True

            visited.remove(node)

            return False

        return helper(src)

        



