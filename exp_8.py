# Implementation of graph using adjacency list and performs Bfs


class Graph:
    def __init__(self,v):
        self.vertices = v
        self.Adjl = [[] for i in range(v)]

    def addEdge(self):   
        e=int(input("Enter the number of edges: "))

        for i in range(e):
            print(f"Enter the edge {i+1}:")
            u=int(input("Enter the starting vertex: "))
            v=int(input("Enter the ending vertex: "))
            self.Adjl[u].append(v)
            self.Adjl[v].append(u)  # for undirected graph

    def display(self):
        for i in range (self.vertices):
            print(i,"- >", self.Adjl[i])

    def bfs(self, start):
        visited = [False] * self.vertices
        q = queue()
        q.Insert(start)
        visited[start] = True

        while q.F != -1:
             current = q.delete()
             print(current)

             for vertex in self.Adjl[current]:
                 if visited[vertex]== False:
                     visited[vertex] = True
             q.Insert(vertex)
                     

class queue:
    def __init__(self):
        self.F = -1
        self.R = -1
        self.QT = [0] * 5

    def Insert(self, x):
        if self.F == -1:
            self.F = 0

        self.R += 1
        self.QT[self.R] = x

    def delete(self):
        if self.F == -1:
            print("nothing to delete")
            return

        else:
            y = self.QT[self.F]

            if self.F == self.R:
                self.F = -1
                self.R = -1
            else:
                self.F += 1

            return y



           
obj = Graph(3)
obj.addEdge()
obj.display()
start = int(input("enter the starting vertex : "))
obj.bfs(start)