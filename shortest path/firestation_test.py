from dijkstra import dijkstra, Graph, find_firestation as find_firestation_dijkstra
from floyd import floyd, find_firestation as find_firestation_floyd
import unittest


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.g = Graph(6)
        connectivity_array = [[1, 2, 7], [1, 6, 14], [1, 3, 9], [3, 6, 2], [3, 4, 11], [6, 5, 9], [4, 5, 6], [2, 4, 15]]
        for x in connectivity_array:
            self.g.connect(x[0] - 1, x[1] - 1, x[2])
            self.g.connect(x[1] - 1, x[0] - 1, x[2])

    def test_dijkstra(self):
        self.assertEqual(dijkstra(self.g, 0), {0: 0, 1: 7, 2: 9, 3: 20, 4: 20, 5: 11})
        
    def test_zero_dijkstra(self):
        g = Graph(2)
        self.assertEqual(dijkstra(g, 0), {0: 0, 1: float("inf")})

    def test_floyd(self):
        self.assertEqual(floyd(self.g)[0], [0, 7, 9, 20, 20, 11])

    def test_floyd_negative(self):
        inf = float("inf")
        g = Graph(4)
        g.edges = [[0, inf, -2, inf],
                   [4, 0, 3, inf],
                   [inf, inf, 0, 2],
                   [inf, -1, inf, 0]]
        expected = [[0, -1, -2, 0], [4, 0, 2, 4], [5, 1, 0, 2], [3, -1, 1, 0]]
        self.assertEqual(floyd(g), expected)
        
    def test_find_firestation(self):
        self.assertEqual(find_firestation_floyd(self.g), find_firestation_dijkstra(self.g))
        

if __name__ == "__main__":
    unittest.main()
