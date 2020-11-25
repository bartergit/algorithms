class Graph:
    def __init__(self, n):
        self.edges = [[0 if x == y else float("inf") for y in range(n)] for x in range(n)]

    @property
    def n(self):
        return len(self.edges)

    def connect(self, a, b, w):
        self.edges[a][b] = w

    def get_near(self, a):
        return [(ind, x) for ind, x in enumerate(self.edges[a]) if x != float("inf")]


def dijkstra(graph, start_node):
    marked = {start_node: 0}
    while len(marked) != graph.n:
        min_weight, min_node = float("inf"), None
        for marked_node in marked.keys():
            for node, weight in graph.get_near(marked_node):
                if node not in marked:
                    potential_min = marked[marked_node] + weight
                    if potential_min < min_weight:
                        min_weight, min_node = potential_min, node
        marked[min_node] = min_weight
    if None in marked:
        for x in range(graph.n):
            if x not in marked or marked[x] is None:
                marked[x] = float("inf")
        del marked[None]
    return marked


def transform_adjacency_matrix(matrix):
    matrix = matrix[:]
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j] = min(matrix[i][j], matrix[j][i])
            matrix[j][i] = matrix[i][j]
    return matrix


def find_firestation(graph):
    graph.edges = transform_adjacency_matrix(graph.edges)
    firestation, firestation_weight = None, float("inf")
    for i in range(graph.n):
        weight = max(list(dijkstra(graph, i).values()))
        if firestation_weight > weight:
            firestation, firestation_weight = i, weight
    return firestation, firestation_weight
