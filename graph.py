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

    def BFS(self,s):
        # queue 
        queue = []
        # mark all nodes are not visited yet 
        visited = [False for k in range(max(self.graph) + 1)]
        # append a node to s 
        queue.append(s)
        # mark visited 
        visited[s] = True
        # loop until emtpy queue 
        while queue:
            # dequeue a node from queue 
            s = queue.pop(0)
            print("visited node {0}".format(s))
            # add neighbours to the queue 
            for neighbour in self.graph[s]:
                if visited[neighbour] == False:
                    queue.append(neighbour)
                    visited[neighbour] = True 


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
    print("test DFS")
    g.DFS()


def testBFS():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print("test BFS")
    g.BFS(2)
    


if __name__=="__main__":
    testDFS()
    testBFS()