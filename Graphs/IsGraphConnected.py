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

    def dfs(self, sv, visited):
        visited[sv] = True

        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] == 1 and not visited[i]:
                self.dfs(i, visited)
                visited[i] = True

    def isConnected(self):
        visited = [False for i in range(self.nVertices)]
        self.dfs(0, visited)

        for boolVal in visited:
            if not boolVal:
                return False
        return True

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

if g.isConnected():
    print('True')
else :
    print('False')
