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

    def __getPathDFS(self, v1, v2, visited):
        if v1 == v2:
            return list([v1])
        visited[v1] = True
        for i in range(self.nVertices):
            if self.adjMatrix[v1][i] == 1 and visited[i] is False:
                li = self.__getPathDFS(i, v2, visited)
                if li != None:
                    li.append(v1)
                    return li
        return None

    def getPathDFS(self, v1, v2):
        visited = [False for i in range(self.nVertices)]
        return self.__getPathDFS(v1, v2, visited)

    def __str__(self):  # Dunder methods-returns the object reprsentation when we print the object. Converts objects to strings
        # print("__str__")
        return str(self.adjMatrix)


#main
li = input().strip().split()
V = int(li[0])
E = int(li[1])

g = Graph(V)

for i in range(E) :
    arr = input().strip().split()
    fv = int(arr[0])
    sv = int(arr[1])
    g.addEdge(fv, sv)

li = input().strip().split()
sv = int(li[0])
ev = int(li[1])

li = g.getPathDFS(sv, ev)
print(li)