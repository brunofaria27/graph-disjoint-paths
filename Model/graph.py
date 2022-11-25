class Graph:
    def __init__(self, num_vertices, origem, destino):
        self.num_vertices = num_vertices
        self.graph = list()
        self.verticeOrigem = origem
        self.verticeDestino = destino
    
    def addEdges(self, u, v):
        self.graph.append([u, v])

    def create_adjacency_list(self):
        listaAdjacencia = [[] for i in range(self.num_vertices)] # Inicialização do array
        for i in range(len(self.graph)):
            listaAdjacencia[self.graph[i][0]].append(self.graph[i][1])
        return listaAdjacencia

    def get_disjoint_paths(self, origem, destino):
        paths = list() # Lista com os caminhos percorridos
        max_paths = 0 # Quantidade máxima de caminhos
        adjacencyList = self.create_adjacency_list()

        return paths, max_paths
    
    def printGraph(self):
        for i in range(0, len(self.graph)):
            print(self.graph[i])
