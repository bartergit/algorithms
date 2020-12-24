import unittest
from testfixtures import compare
from graph import Graph, find_connectivity_components, is_eulerian, is_bipartite, find_euler_path, find_bipartite


class TestGraph(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_graph(self):
        g = Graph({1: [2, 3], 3: [5]})
        self.assertEqual(g.vertices, {1: [2, 3], 2: [1], 3: [1, 5], 5: [3]})

    def test_functionality(self):
        g = Graph({1: [2, 3], 2: [4, 6, 7], 3: [6], 4: [7], 5: [6, 7], 6: [3, 2, 7, 5], 7: [6, 5]})
        self.assertEqual(g.len, 7)

    def test_disconnect_1(self):
        g = Graph({1: [2, 3, 4], 4: [5, 2]})
        g.disconnect(4, 1)
        self.assertFalse(4 in g[1])
        self.assertFalse(1 in g[4])
        self.assertEqual(g[1], [2, 3])
        self.assertEqual(g[4], [5, 2])

    def test_disconnect_nonexisten(self):
        g = Graph({3: [5, 9], 1: []})
        with self.assertRaises(Exception):
            g.disconnect(3, 1)

    def test_add(self):
        g = Graph({1: [2, 3], 4: [5, 2]})
        g.connect(4, 1)
        self.assertTrue(4 in g[1])
        self.assertTrue(1 in g[4])
        self.assertEqual(g[1], [2, 3, 4])
        self.assertEqual(g[4], [5, 2, 1])

    def test_find_connectivity_components_1(self):
        g = Graph({1: [2, 3], 4: [2, 3]})
        self.assertTrue(len(find_connectivity_components(g)), 1)
        self.assertTrue(find_connectivity_components(g), [1, 2, 3, 4])

    def test_find_connectivity_components_2(self):
        g = Graph({1: [2, 3], 4: []})
        self.assertTrue(len(find_connectivity_components(g)), 2)

    def test_find_connectivity_components_3(self):
        g = Graph({1: [2, 3, 4], 4: [5], 5: [6], 6: [1]})
        self.assertTrue(len(find_connectivity_components(g)), 1)
        self.assertTrue(find_connectivity_components(g), g)

    def test_find_connectivity_components_4(self):
        g = Graph({1: [2, 3, 4], 5: [6], 7: [1], 8: [9], 11: [10]})
        self.assertTrue(len(find_connectivity_components(g)), 4)
        self.assertTrue([find_connectivity_components(g), [[1, 2, 3, 4, 7], [5, 6], [8, 9], 11, 10]])

    def test_find_connectivity_components_4(self):
        g = Graph({1: [2, 3], 4: [2, 3, 5], 5: [6, 7, 8], 7: [9]})
        self.assertEqual(len(find_connectivity_components(g)), 1)

    def test_is_eulerian_1(self):
        g = Graph({1: [2, 3]})
        self.assertFalse(is_eulerian(g))

    def test_is_eulerian_2(self):
        g = Graph({4: []})
        self.assertTrue(is_eulerian(g))

    def test_is_eulerian_3(self):
        g = Graph({1: [2, 3], 4: [2, 3]})
        self.assertTrue(is_eulerian(g))

    def test_is_bipartite_1(self):
        g = Graph({5: []})
        self.assertFalse(is_bipartite(g))

    def test_is_bipartite_2(self):
        g = Graph({5: [1, 2, 3]})
        self.assertTrue(is_bipartite(g))

    def test_is_bipartite_3(self):
        g = Graph({1: [2, 3], 4: [2, 3]})
        self.assertTrue(is_bipartite(g))

    def test_is_bipartite_4(self):
        g = Graph({1: [2, 3], 2: [3]})
        self.assertFalse(is_bipartite(g))

    def test_is_bipartite_5(self):
        g = Graph({1: [], 2: []})
        self.assertTrue(is_bipartite(g))

    def test_is_bipartite_6(self):
        g = Graph({1: [2]})
        self.assertTrue(is_bipartite(g))

    def test_find_bipartite_1(self):
        g = Graph({5: []})
        with self.assertRaises(Exception):
            find_bipartite([g])

    def test_find_bipartite_2(self):
        g = Graph({5: [1, 2, 3]})
        a, b = find_bipartite(g)
        if len(a) > len(b):
            a, b = b, a
        self.assertEqual(a, [5])
        self.assertEqual(b, [1, 2, 3])
        self.assertTrue(is_bipartite(g))

    def test_find_bipartite_3(self):
        g = Graph({1: [2, 3], 4: [2, 3, 5], 5: [6, 7, 8], 7: [9]})
        a, b = find_bipartite(g)
        if len(a) > len(b):
            a, b = b, a
        self.assertEqual(b, [1, 4, 6, 7, 8])
        self.assertEqual(a, [2, 3, 5, 9])
        self.assertTrue(is_bipartite(g))

    def test_find_euler_path_1(self):
        g = Graph({1: [2, 3], 4: [2, 3, 5], 5: [6, 7, 8], 7: [9]})
        with self.assertRaises(Exception):
            find_euler_path(g)

    def test_find_euler_path_2(self):
        g = Graph({1: [2, 3], 2: [4, 6, 7], 3: [6], 4: [7], 5: [6, 7], 6: [3, 2, 7, 5], 7: [6, 5]})
        self.assertEqual(find_euler_path(g),
                         [(1, 3), (3, 6), (6, 7), (7, 5), (5, 6), (6, 2), (2, 7), (7, 4), (4, 2), (2, 1)])

    def test_find_euler_path_3(self):
        g = Graph({1: [2, 3], 4: [2, 3]})
        self.assertEqual(find_euler_path(g),
                         [(1, 3), (3, 4), (4, 2), (2, 1)])


if __name__ == "__main__":
    unittest.main()
