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

        '''Returns true if there is a path from source 's' to sink 't' in
	residual graph. Also fills parent[] to store the path '''

    def search(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False]*(self.num_nodes)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for val in self.adj_list[u]:  # adj[u] = {2, 3, 4}
                if visited[val] == False:
                    queue.append(val)
                    visited[val] = True
                    parent[val] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False

        # Returns the maximum number of edge-disjoint paths from
        # s to t in the given graph

    def is_edge(self, u, v):
        if v in self.adj_list[u]:
            return 1
        return 0

    def get_disjoint_paths(self, source, sink):
        aux_graph = deepcopy(self)

        # This array is filled by BFS and to store path
        parent = [-1]*(aux_graph.num_nodes)
        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while aux_graph.search(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, aux_graph.is_edge(parent[s], s))
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while (v != source):  # 1 2 3 5
                u = parent[v]
                aux_graph.remove_edge(u, v)
                aux_graph.add_edge(v, u)
                v = parent[v]

        return max_flow

    def print(self):
        for i in range(self.num_nodes):
            for j in self.adj_list[i]:
                print(i, j)

    def print_adj_list(self):
        print(self.adj_list)
