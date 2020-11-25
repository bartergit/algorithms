import copy

import numpy as np
from binarytree import Node
import unittest
import gspread


M = float("inf")


class Matrix(object):
    def __init__(self, matrix):
        self.array = np.array(matrix)
        self.x = list(range(len(matrix)))
        self.y = list(range(len(matrix)))

    def set(self, x, y, value):
        x -= 1
        y -= 1
        if x in self.x and y in self.y:
            ind_x = self.x.index(x)
            ind_y = self.y.index(y)
            self.array[ind_x][ind_y] = value

    def collapse(self, x, y):
        x -= 1
        y -= 1
        if x in self.x and y in self.y:
            ind_x = self.x.index(x)
            self.x.remove(x)
            ind_y = self.y.index(y)
            self.y.remove(y)
            self.array = np.delete(self.array, ind_x, 0)
            self.array = np.delete(self.array, ind_y, 1)
        return self.array

    def find_penalty_zeroes(self):
        out = (-1, -1, -M)
        for i, _ in enumerate(self.array):
            for j, _ in enumerate(self.array[i]):
                if self.array[i][j] == 0:
                    a = list(self.array[:, j])
                    a.remove(0)
                    b = list(self.array[i])
                    b.remove(0)
                    if min(a) + min(b) > out[2]:
                        out = (self.x[i] + 1, self.y[j] + 1, min(a) + min(b))
        return out

    def transform(self):
        h = 0
        for i in range(len(self.array)):
            min_h = min(self.array[i])
            h += min_h
            for j in range(len(self.array)):
                self.array[i][j] -= min_h
        for i in range(len(self.array)):
            min_h = min(self.array[:, i])
            h += min_h
            for j in range(len(self.array)):
                self.array[j][i] -= min_h
        return h

    def __repr__(self):
        return self.array.__str__()


def dfs(node, out):
    if node.left is None and node.right is None:
        out.append(node)
    else:
        dfs(node.left, out)
        dfs(node.right, out)


def foo(node):
    if len(node.matrix.array) == 2:
        return node.val
    matrix_left, matrix_right = copy.deepcopy(node.matrix), copy.deepcopy(node.matrix)
    penalty_zero = node.matrix.find_penalty_zeroes()
    i, j = penalty_zero[0], penalty_zero[1]
    # proceed left
    matrix_left.set(i, j, M)
    node.left = Node(node.val + penalty_zero[2])
    matrix_left.transform()
    node.left.matrix = matrix_left
    node.left.path = node.path.copy()
    # proceed right
    matrix_right.collapse(i, j)
    ind = 0
    tail = i
    head = j
    while ind < len(node.path):
        if node.path[ind][1] == tail:
            matrix_right.set(head, node.path[ind][0], M)
            tail = node.path[ind][0]
            ind = 0
        elif node.path[ind][0] == head:
            matrix_right.set(node.path[ind][1], tail, M)
            head = node.path[ind][1]
            ind = 0
        else:
            ind += 1
    matrix_right.set(j, i, M)  # and some others
    node.right = Node(node.val + matrix_right.transform())
    node.right.matrix = matrix_right
    node.right.path = node.path.copy()
    node.right.path.append((i, j))


def little(matrix):
    h = matrix.transform()
    root = Node(h)
    root.matrix = matrix
    root.path = []
    start_node = root
    answers = []
    while True:
        answer = foo(start_node)
        if answer:
            if len(answers) and answer != answers[0]:
                break
            answers.append(answer)
        out = []
        dfs(root, out)
        out.sort(key=lambda x: x.val)
        start_node = out[len(answers)]
        if len(answers) and start_node.val != answers[0]:
            break 
    print(answers)
    print(root)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = Matrix([
            [M, 5, 1, 7, 3],
            [2, M, 1, 5, 2],
            [9, 3, M, 2, 5],
            [4, 6, 2, M, M],
            [1, 2, M, 7, M]
        ])

    def test_transform(self):
        m = Matrix([[M, 5, 2, 5, 8],
                    [1, M, 8, 1, 6],
                    [M, 7, M, 7, 2],
                    [9, 8, M, M, 4],
                    [2, 1, 5, 9, M]])
        m2 = Matrix(m.array)
        h = m.transform()
        self.assertEqual(h, m2.transform())
        self.assertEqual(h, 10)

    def test_collapse(self):
        matrix = Matrix([[M, 3, 0, 6, 1],
                         [1, M, 0, 4, 0],
                         [7, 0, M, 0, 2],
                         [2, 3, 0, M, M],
                         [0, 0, M, 6, M]])
        self.assertTrue((matrix.collapse(3, 4) == [[M, 3, 0, 1],
                                                   [1, M, 0, 0],
                                                   [2, 3, 0, M],
                                                   [0, 0, M, M]]).all())
        self.assertEqual(len(matrix.array), 4)

    def test_find_penalty(self):
        matrix = Matrix([[M, 3, 0, 6, 1],
                         [1, M, 0, 4, 0],
                         [7, 0, M, 0, 2],
                         [2, 3, 0, M, M],
                         [0, 0, M, 6, M]])
        self.assertEqual(matrix.find_penalty_zeroes(), (3, 4, 4))

    def test_little(self):
        little(self.matrix)
        # little(Matrix([[M, 5, 2, 5, 8],
        #             [1, M, 8, 1, 6],
        #             [M, 7, M, 7, 2],
        #             [9, 8, M, M, 4],
        #             [2, 1, 5, 9, M]]))
        # little(Matrix([[M, 9, 1, 4, 5],
        #             [4, M, 4, 8, 8],
        #             [6, 9, M, 8, M],
        #             [1, 9, 5, M, M],
        #             [2, 4, 2, 3, M]]))
        # little(Matrix([
        #             [M,8,3,1,7],
        #             [3,M,6,7,6],
        #             [8,7,M,3,5],
        #             [8,6,1,M,1],
        #             [9,2,9,6,M]]))


if __name__ == '__main__':
    unittest.main()
