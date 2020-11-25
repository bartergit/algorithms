import unittest
from testfixtures import compare
import random
from bst import Tree_Node, rebalance, inorder, create_bst, find_min, postorder, rotate_right, reverse_order


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.test_cases = [[2, 1, 3], [2, 1, 3, 5], [1, 1, 1], [5, 9, 1, -5, 5, 2], [18, 0, 11, 13, -1, 1],
                           [-3, 1, 9, -5, 18, -11, 0, 10, 8, -15, 7, 11, 0, 5, 2],
                           [5, 1, 9, 18, 7, 11, 0, -5], list(reversed(list(range(10)))), list(range(11))]

    def test_inorder(self):
        for i in self.test_cases:
            with self.subTest(i=i):
                root = create_bst(i)
                out = []
                inorder(root, lambda x: out.append(x))
                self.assertEqual(out, sorted(list(set(i))))

    def test_reverse_order(self):
        for i in self.test_cases:
            with self.subTest(i=i):
                root = create_bst(i)
                out = []
                reverse_order(root, lambda x: out.append(x))
                self.assertEqual(out, list(reversed(sorted(list(set(i))))))

    def test_rebalance(self):
        for i in range(len(self.test_cases)):
            test_data = self.test_cases[i]
            with self.subTest(i=test_data):
                root = create_bst(test_data)
                root = rebalance(root)
                self.assertTrue(root.is_balanced, "is not balanced")
                self.assertTrue(root.is_bst, "rebalanced tree is not bst")

    def test_find_min(self):
        for i in range(len(self.test_cases)):
            test_data = self.test_cases[i]
            with self.subTest(i=test_data):
                k = random.randint(0, len(set(test_data)) - 1)
                self.assertEqual(find_min(create_bst(test_data), k).val, sorted(list(set(test_data)))[k], msg=f"k={str(k)}, {sorted(list(set(test_data)))}")
                self.assertEqual(find_min(create_bst(test_data), len(set(test_data))), None)

    def test_rotation(self):
        Q = Tree_Node(1)
        P = Tree_Node(2)
        P.add_left(3)
        P.add_right(4)
        Q.left = P
        Q.add_right(5)
        first = []
        postorder(Q, lambda x: first.append(str(x)))
        second = []
        Q = rotate_right(Q)
        postorder(Q, lambda x: second.append(str(x)))
        self.assertEqual("".join(first), "12345")
        self.assertEqual("".join(second), "23145")


if __name__ == "__main__":
    unittest.main()
