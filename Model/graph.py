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

    def is_edge(self, u, v):
        if v in self.adj_list[u]:
            return 1
        return 0

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
            path_flow = float("Inf")
            path = []
            s = sink

            while (s != source):
                path_flow = min(path_flow, aux_graph.is_edge(parent[s], s))
                path.append(s)
                s = parent[s]
        
            path.append(source)
            path.reverse()
            paths.append(path)
            max_flow += path_flow

            v = sink
            while (v != source):
                u = parent[v]
                aux_graph.remove_edge(u, v)
                aux_graph.add_edge(v, u)
                v = parent[v]
        return max_flow, paths

    def print(self):
        for i in range(self.num_nodes):
            for j in self.adj_list[i]:
                print(i, j)

    def print_adj_list(self):
        print(self.adj_list)
