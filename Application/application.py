import sys
import random

# Importando pastas a sere utilizadas
sys.path.insert(0, '../Model')

# Importando funções e objetos de outros arquivos
from graph import Graph

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
    dir_name = sys.argv[1]
    origin = sys.argv[2]
    destiny = sys.argv[3]

    create_simple_graph(dir_name, 10000) # Retirar essa linha e passar o nome do arquivo por parametro caso queira usar outro grafo
    arq = open(dir_name, 'r')

    graph = Graph(arq)
    max_paths, paths, time = graph.get_disjoint_paths(int(origin), int(destiny))
    print(f'Temos no máximo {max_paths} caminhos disjuntos.')
    print(f'Os caminhos são {paths}')
    print(f'A duração para achar os caminhos disjuntos foi de: {time} segundos')

# Programa principal
if __name__ == '__main__':
    main()