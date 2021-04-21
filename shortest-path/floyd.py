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


def floyd(graph):
    n = graph.n
    dist = graph.edges.copy()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
    return dist


def transform_adjacency_matrix(matrix):
    matrix = matrix[:]
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j] = min(matrix[i][j], matrix[j][i])
            matrix[j][i] = matrix[i][j]
    return matrix


def find_firestation(graph):
    graph.edges = transform_adjacency_matrix(graph.edges)
    dist = floyd(graph)
    firestation, firestation_weight = None, float("inf")
    for i in range(graph.n):
        weight = max(dist[i])
        if firestation_weight > weight:
            firestation, firestation_weight = i, weight
    return firestation, firestation_weight


if __name__ == "__main__":
    g = Graph(9)
    s = 0; a = 1; c = 2; e = 4; f=5; d=6; b=7; t=8;
    # [s: 0, a: 3, c: 4, e:inf, f: 1, d: -7, b:-4, t:-8, -11]
    g.connect(s, a, 3)
    g.connect(s, c, 4)
    g.connect(s, e, 4)
    g.connect(a, e, 3)
    g.connect(a, b, 4)
    g.connect(a, c, 4)
    g.connect(c, e, -3)
    g.connect(c, b, -3)
    g.connect(c, f, 3)
    g.connect(e, d, -5)
    g.connect(e, f, -1)
    g.connect(f, t, 3)
    g.connect(f, b, -1)
    g.connect(d, f, -3)
    g.connect(d, t, -3)
    g.connect(b, d, 4)
    g.connect(b, t, -3)
    print(floyd(g))
    pass
