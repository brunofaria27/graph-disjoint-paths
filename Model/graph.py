from copy import deepcopy
import time

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

    def search(self, origin, destiny, parent):
        visited = [False] * (self.num_nodes)
        queue = []
        queue.append(origin)
        visited[origin] = True

        while queue:
            u = queue.pop(0)
            for val in self.adj_list[u]:  # adj[u] = {2, 3, 4}
                if visited[val] == False:
                    queue.append(val)
                    visited[val] = True
                    parent[val] = u
                    
        if visited[destiny]:
            return True
        return False

    def get_disjoint_paths(self, origin, destiny):
        start = time.time()
        aux_graph = deepcopy(self)
        parent = [-1] * (aux_graph.num_nodes)
        max_paths = 0
        paths = []
        
        while aux_graph.search(origin, destiny, parent):
            reversed_path = []
            v = destiny

            while (v != origin):
                u = parent[v]
                reversed_path.append(v)
                aux_graph.remove_edge(u, v)
                aux_graph.add_edge(v, u)
                v = parent[v]
            
            reversed_path.append(origin)
            path = reversed_path[::-1]
            paths.append(path)
            max_paths += 1
        end = time.time()
        return max_paths, paths, (end - start)

    def print(self):
        for i in range(self.num_nodes):
            for j in self.adj_list[i]:
                print(i, j)

    def print_adj_list(self):
        print(self.adj_list)
