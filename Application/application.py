import sys

# Importando pastas a sere utilizadas
sys.path.insert(0, '../Model')

# Importando funções e objetos de outros arquivos
from graph import Graph

# Ler o arquivo que tem todas as arestas
def create_graph(arq, graph):
    for linha in arq:
        u, v = linha.split(' ')
        graph.addEdges(int(u), int(v))

def main():
    dir_name = sys.argv[1]
    vertice_origem = sys.argv[2]
    vertice_destino = sys.argv[3]

    arq = open(dir_name, 'r')
    num_vertices = int(arq.readline())

    graph = Graph(num_vertices, vertice_origem, vertice_destino)
    create_graph(arq, graph)
    graph.printGraph()


# Programa principal
if __name__ == '__main__':
    main()