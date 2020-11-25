from math import inf
import gspread

gc = gspread.service_account(filename='service_account.json')

sh = gc.open("asd")


class Graph:
    def __init__(self, graph: list):
        self.graph = graph
        self.vertices_amount = len(graph)
        self.s_matrix = self.get_s_matrix()
        self.step_for_path = 0

    def get_s_matrix(self):
        return [[1, 2, 3, 4, 5] for _ in range(5)]

    def floyd(self):
        step = 1
        for k in range(self.vertices_amount):
            for i in range(self.vertices_amount):
                for j in range(self.vertices_amount):
                    if self.graph[j][j] < 0:
                	    return self.graph
                    if j == 0 and i == 0:
                        graph_copy = []
                        s_matrix_copy = []
                        for lst in self.graph:
                            graph_copy.append([x if x != inf else 'M' for x in lst])
                        for lst in self.s_matrix:
                            s_matrix_copy.append([x if x != inf else 'M' for x in lst])
                        sh.sheet1.update(f'B{step}:F{step + 4}', graph_copy)
                        sh.sheet1.update(f'I{step}:M{step + 4}', s_matrix_copy)
                        step += 6
                    copy = self.graph[i][j]
                    self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])
                    if copy != self.graph[i][j]:
                        self.s_matrix[i][j] = self.s_matrix[i][k]
        graph_copy = []
        s_matrix_copy = []
        for lst in self.graph:
            graph_copy.append([x if x != inf else 'M' for x in lst])
        for lst in self.s_matrix:
            s_matrix_copy.append([x if x != inf else 'M' for x in lst])
        sh.sheet1.update(f'B{step}:F{step + 4}', graph_copy)
        sh.sheet1.update(f'I{step}:M{step + 4}', s_matrix_copy)
        return self.graph

    def get_path(self, i, j, sheet_num):
        k = 1
        sh.get_worksheet(sheet_num).update(f'P{19 + self.step_for_path}', f'{i}->{j}')
        sh.get_worksheet(sheet_num).update_cell(19 + self.step_for_path, 17, i)
        while i - 1 != j - 1:
            i = self.s_matrix[i - 1][j - 1]
            sh.get_worksheet(sheet_num).update_cell(19 + self.step_for_path, 17 + k, i)
            k += 1
        self.step_for_path += 1

    def mod_floyd(self):
        step = 1
        self.s_matrix = self.get_s_matrix()
        for k in range(self.vertices_amount):
            for i in range(self.vertices_amount):
                for j in range(self.vertices_amount):
                    if j == 0 and i == 0:
                        graph_copy = []
                        s_matrix_copy = []
                        for lst in self.graph:
                            graph_copy.append([x if x != -inf else 'M' for x in lst])
                        for lst in self.s_matrix:
                            s_matrix_copy.append([x if x != -inf else 'M' for x in lst])
                        sh.get_worksheet(1).update(f'B{step}:F{step + 4}', graph_copy)
                        sh.get_worksheet(1).update(f'I{step}:M{step + 4}', s_matrix_copy)
                        step += 6
                    copy = self.graph[i][j]
                    self.graph[i][j] = max(self.graph[i][j], min(self.graph[i][k], self.graph[k][j]))
                    if copy != self.graph[i][j]:
                        self.s_matrix[i][j] = self.s_matrix[i][k]
        graph_copy = []
        s_matrix_copy = []
        for lst in self.graph:
            graph_copy.append([x if x != -inf else 'M' for x in lst])
        for lst in self.s_matrix:
            s_matrix_copy.append([x if x != -inf else 'M' for x in lst])
        sh.get_worksheet(1).update(f'B{step}:F{step + 4}', graph_copy)
        sh.get_worksheet(1).update(f'I{step}:M{step + 4}', s_matrix_copy)
        return self.graph


if __name__ == '__main__':
    graph = [
     	[inf, 9, inf, 3, 9],
        [-2, inf, inf, -4, 5],
        [6, -3, inf, 5, 2],
        [4, 6, 9, inf, 3],
        [8, 2, 1, 5, inf]
        # [inf, 7, 9, inf, -4],
        # [7, inf, 4, -1, 2],
        # [5, -2, inf, 2, 4],
        # [7, 8, 5, inf, 9],
        # [inf, -2, 5, -2, inf]
    ]
    g = Graph(graph)
    print(*g.floyd(), sep='\n')
    print()
    print(*g.s_matrix, sep='\n')
    print()
    g.get_path(2, 3, 0)
    g.get_path(1, 3, 0)

    g.graph = [
    	[-inf, -inf, 3, 1, 2],
        [1, -inf, 7, 4, 6],
        [9, 7, -inf, 6, 9],
        [1, 4, 8, -inf, 5],
        [7, 5, 9, 6, -inf]
        # [-inf, 9, 6, 8, 6],
        # [2, -inf, 1, 4, 9],
        # [8, 2, -inf, 8, 9],
        # [4, 8, 1, -inf, 3],
        # [-inf, 9, 1, 9, -inf]
    ]
    g.step_for_path = 0
    print(*g.mod_floyd(), sep='\n')
    print()
    print(*g.s_matrix, sep='\n')
    g.get_path(2, 1, 1)
    g.get_path(4, 1, 1)


