# 21 JUL 2021 
# Basic Graph 
from collections import defaultdict 

class Graph():
    """
    Simple practice some graph algorithms
    """
    def __init__(self):
        """
        """
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSUtil(self,v,visited):
        # mark v as visited 
        visited.add(v)
        # print visited 
        print("visited node {0}".format(v))
        # recursive on neighbor of v 
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour,visited)

    def DFS(self):
        # init visited 
        visited = set()
        # 
        for vertex in list(self.graph):
            if vertex not in visited:
                self.DFSUtil(vertex,visited)


def testDFS():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.DFS()
    


if __name__=="__main__":
    testDFS()
