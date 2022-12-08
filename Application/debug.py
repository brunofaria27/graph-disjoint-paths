import sys
import random

from copy import deepcopy

class Graph:
    def __init__(self, arq):
        self.read_graph(arq)

    def read_graph(self, arq):
        self.num_nodes = int(arq.readline())
        self.adj_list = [[] for i in range(self.num_nodes)]
        for linha in arq:
            u, v = linha.split(' ')
            self.add_edge(int(u), int(v))

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def remove_edge(self, u, v):
        self.adj_list[u].remove(v)

    def search(self, s, t, parent):
        visited = [False] * (self.num_nodes)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for val in self.adj_list[u]:  # adj[u] = {2, 3, 4}
                if visited[val] == False:
                    queue.append(val)
                    visited[val] = True
                    parent[val] = u
        if visited[t]:
            return True
        return False

    def get_disjoint_paths(self, source, sink):
        aux_graph = deepcopy(self)
        parent = [-1] * (aux_graph.num_nodes)
        max_flow = 0
        paths = []
        
        while aux_graph.search(source, sink, parent):
            reversed_path = []
            v = sink

            while (v != source):
                u = parent[v]
                reversed_path.append(v)
                aux_graph.remove_edge(u, v)
                aux_graph.add_edge(v, u)
                v = parent[v]
            
            reversed_path.append(source)
            path = reversed_path[::-1]
            paths.append(path)
            max_flow += 1
        return max_flow, paths

    def print(self):
        for i in range(self.num_nodes):
            for j in self.adj_list[i]:
                print(i, j)

    def print_adj_list(self):
        print(self.adj_list)


def looping_aux(start, end):
    edges = list()
    for i in range(start, end):
        for j in range(start, end):
            if i != j and [i, j] not in edges and [j, i] not in edges:
                edges.append([i, j])
                edges.append([j, i])
    return edges

def get_edge_random(start, end):
    return random.randint(start, end)

# Criar grafo completo
def create_complete_graph(dir_name, num_vertex):
    with open(dir_name, 'w') as arquivo:
        arquivo.write(str(num_vertex) + '\n')
        edges_k1 = looping_aux(0, (num_vertex // 2))
        edges_k2 = looping_aux((num_vertex // 2), num_vertex)
        edges = edges_k1 + edges_k2

        # Escrever arestas no arquivo
        for i in range(len(edges)):
            arquivo.write(str(edges[i][0]) + ' ' + str(edges[i][1]) + '\n')
        
        # Criar arestas de teste para caminho
        edge_test = [get_edge_random(0, (num_vertex // 2) - 1), get_edge_random((num_vertex // 2), num_vertex - 1)]
        edge_test2 = [get_edge_random(0, (num_vertex // 2) - 1), get_edge_random((num_vertex // 2), num_vertex - 1)]
        while edge_test == edge_test2:
            edge_test = [get_edge_random(0, (num_vertex // 2) - 1), get_edge_random((num_vertex // 2), num_vertex - 1)]
            edge_test2 = [get_edge_random(0, (num_vertex // 2) - 1), get_edge_random((num_vertex // 2), num_vertex - 1)]
        arquivo.write(str(edge_test[0]) + ' ' + str(edge_test[1]) + '\n')
        arquivo.write(str(edge_test2[0]) + ' ' + str(edge_test2[1]) + '\n')

# Criar grafo circular
def create_graph_circular(dir_name, num_vertex):
    with open(dir_name, 'w') as arquivo:
        arquivo.write(str(num_vertex) + '\n')
        for i in range(num_vertex):
            if i != (num_vertex - 1):
                arquivo.write(str(i) + ' ' + str(i + 1) + '\n')
        arquivo.write(str(num_vertex - 1) + ' ' + str(0) + '\n')

# Criar grafo simples
def create_simple_graph(dir_name, num_vertex):
    with open(dir_name, 'w') as arquivo:
        arquivo.write(str(num_vertex) + '\n')
        for i in range(num_vertex):
            for j in range(i, num_vertex):
                if i != j:
                    arquivo.write(str(i) + ' ' + str(j) + '\n')

# Ler o arquivo que tem todas as arestas
def create_graph(arq, graph):
    for linha in arq:
        u, v = linha.split(' ')
        graph.add_edge(int(u), int(v))

def main():
    dir_name = input()
    origin = input()
    destiny = input()

    #create_complete_graph(dir_name, 10)
    arq = open(dir_name, 'r')

    graph = Graph(arq)
    max_paths, paths = graph.get_disjoint_paths(int(origin), int(destiny))
    print(f'Temos no máximo {max_paths} caminhos disjuntos.')
    print(f'Os caminhos são {paths}')

# Programa principal
if __name__ == '__main__':
    main()