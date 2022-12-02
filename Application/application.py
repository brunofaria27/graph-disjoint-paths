import sys

# Importando pastas a sere utilizadas
sys.path.insert(0, '../Model')

# Importando funções e objetos de outros arquivos
from graph import Graph
from copy import deepcopy

# Ler o arquivo que tem todas as arestas
def create_graph(arq, graph):
    for linha in arq:
        u, v = linha.split(' ')
        graph.add_edge(int(u), int(v))

def main():
    dir_name = sys.argv[1]
    origin = sys.argv[2]
    destiny = sys.argv[3]

    arq = open(dir_name, 'r')

    graph = Graph(arq)

    print ("There can be maximum %d edge-disjoint paths from %d to %d" %
			(graph.get_disjoint_paths(int(origin), int(destiny)), int(origin), int(destiny)))


# Programa principal
if __name__ == '__main__':
    main()