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


    def DFSUtil(self,temp,v,visited):
        # mark v as visited 
        visited.add(v)
        # store visited to temp 
        temp.append(v)
        # print visited 
        print("visited node {0}".format(v))
        # recursive on neighbor of v 
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                temp = self.DFSUtil(temp,neighbour,visited)
        # return connected component for the node v 
        return temp

    def DFS(self):
        # init visited 
        visited = set()
        # loop over all vertex (nodes might not be all connected)
        for vertex in list(self.graph):
            temp = []
            if vertex not in visited:
                self.DFSUtil(temp,vertex,visited)
                print("component of node {0} is {1}".format(vertex, temp))


    def connectedComponents(self):
        # init output 
        cc = defaultdict(list)
        # visited init 
        visited = set()
        # loop over all node
        for vertex in list(self.graph):
            if vertex not in visited:
                cc[vertex] = self.DFSUtil([],vertex,visited)
        # print output 
        for node in cc:
            print("node {0} ==> {1}".format(node,cc[node]))
        # return 
        return cc 


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
    

def testComponent():
    g = Graph()
    g.addEdge(1, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.connectedComponents()



if __name__=="__main__":
    # testDFS()
    # testBFS()
    testComponent()