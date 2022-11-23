class Graph:
    def __init__(self, num_vertices, origem, destino):
        self.num_vertices = num_vertices
        self.graph = list()
        self.verticeOrigem = origem
        self.verticeDestino = destino
    
    def addEdges(self, u, v):
        self.graph.append([u, v])
    
    def printGraph(self):
        for i in range(0, len(self.graph)):
            print(self.graph[i])