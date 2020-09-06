#A Tree is also a graph because we have vertices and edges but not vice-versa
# A Tree is a connected graph. A disconnected graph cannot be a Tree
# A Tree will not have a cycle i.e no cycle in a Tree
# Minimum edges in a connected graph is (n-1)edges-->eg. Tree in this case
# Maximum edges in a connected graph is (E)edges means every vertex has edge to every other vertex.So, time complexity in worst case will
#be O(n^2)

#Graph with Adjacency Matrix

import queue
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __hasPath(self, v1, v2, visited):
        if v1 == v2:
            return True
        q = queue.Queue()
        q.put(v1)
        visited[v1] = True
        while(q.empty() is False):
            u = q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[u][i] == 1 and visited[i] is False:
                    if i == v2:
                        return True
                    q.put(i)
                    visited[i] = True
        return False

    # Solve with DFS
    def hasPath(self, v1, v2):
        visited = [False for i in range(self.nVertices)]
        return self.__hasPath(v1, v2, visited)

    def __str__(self): #Dunder methods-returns the object reprsentation when we print the object. Converts objects to strings
        # print("__str__")
        return str(self.adjMatrix)

# g = Graph(5)
# g.addEdge(0, 1)
# g.addEdge(1, 3)
# g.addEdge(2, 4)
# g.removeEdge(3, 1)
# print(g.containsEdge(3, 1))
# print(g)
li = input().strip().split()
V = int(li[0])
E = int(li[1])

g = Graph(V)

for i in range(E):
    arr = input().strip().split()
    fv = int(arr[0])
    sv = int(arr[1])
    g.addEdge(fv, sv)

li = input().strip().split()
sv = int(li[0])
ev = int(li[1])

if g.hasPath(sv, ev):
    print('True')
else :
    print('False')
