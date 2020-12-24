import unittest
from testfixtures import compare
import sys
sys.path.append('../euler')
from graph import Graph, find_bipartite


def find_increasing_chain(vertex, graph, used, curr_matching):
    if used.get(vertex,False): return False
    used[vertex] = True
    for neighbor in graph[vertex]:
        if neighbor not in curr_matching or find_increasing_chain(curr_matching[neighbor], graph, used, curr_matching):
            curr_matching[neighbor] = vertex
            return True
    return False

def find_greatest_matching(graph, first_part, second_part): #kuhn algorithm
    assert len(first_part) == len(second_part)
    curr_matching = {}
    for vertex in first_part:
        used = {}
        find_increasing_chain(vertex, graph, used, curr_matching)
    matching = []
    for vertex in curr_matching:
        matching.append(sorted([vertex, curr_matching[vertex]]))
        second_part.remove(vertex)
        first_part.remove(curr_matching[vertex])
    if not (len(first_part) == len(second_part) == 0):
        message = ""
        for i in range(len(first_part)):
            message += f"worker {first_part.pop()} should be educated to {second_part.pop()} job\n"
        # print(message)        
        raise Exception(message)
    return matching

class TestMatching(unittest.TestCase):
    def setUp(self):
        self.graphs = [Graph({0: [4, 3], 3: [1], 2:[5]})]
        self.graphs.append(Graph({
        1: [6, 7],
        2: [6, 7],
        3: [6, 8],
        4: [8, ],
        5: [1, ],
        6: [1, 3, 2],
        7: [2, 1],
        8: [3, 4]
        }))
        self.expected = [
            [[0, 4], [1, 3], [2, 5]],
            [[1, 5], [3, 6], [2, 7], [4, 8]]
        ]


    def test_matching(self):
        for i, graph in enumerate(self.graphs):
            with self.subTest(i=i):
                self.assertCountEqual(find_greatest_matching(graph, *find_bipartite(graph)), self.expected[i])

    def test_exception(self):
        g = Graph({4: [2], 0: [3], 3: [1], 2:[5]})
        with self.assertRaises(Exception):
            find_greatest_matching(g, [0, 1, 2], [3,4,5])
        g2 = Graph({4: [0,1,2], 1:[3,5]})
        with self.assertRaises(Exception):
            find_greatest_matching(g2, [0,1,2], [3,4,5])





if __name__ == "__main__":
    unittest.main()