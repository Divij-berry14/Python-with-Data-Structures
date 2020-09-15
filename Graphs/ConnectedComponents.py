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
        if self.adjMatrix[v1][v2] > 0:
            return True
        return False

    def __ConnectedC(self,visited, arr1, sv):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        while(q.empty() is False):
            u = q.get()
            arr1.append(u)
            for i in range(self.nVertices):
                if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True
        return arr1
    def ConnectedComp(self):
        visited = [False for i in range(self.nVertices)]
        finalArr = []
        for i in range(self.nVertices):
            if visited[i] is False:
                arr = []
                temp = self.__ConnectedC(visited, arr, i)
                finalArr.append(temp)
        return finalArr

    def __str__(self):
        return str(self.adjMatrix)
li = input().strip().split()
V = int(li[0])
E = int(li[1])

g = Graph(V)

for i in range(E):
    arr = input().strip().split()
    fv = int(arr[0])
    sv = int(arr[1])
    g.addEdge(fv, sv)

print(g.ConnectedComp())