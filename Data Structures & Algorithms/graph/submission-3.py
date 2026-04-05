class Graph:
    
    def __init__(self):
        self.adjList = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = []

        if dst not in self.adjList:
            self.adjList[dst] = []
        self.adjList[src].append(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjList and dst in self.adjList[src]:
            self.adjList[src].remove(dst)
            return True
        return False


    def hasPath(self, src: int, dst: int) -> bool:

        visited = set()

        def dfs(node):
            if node in visited:
                return False

            if node == dst:
                return True

            visited.add(node)

            for nd in self.adjList[node]:
                if dfs(nd):
                    return True

            visited.pop()
            
            return False

        return dfs(src)


