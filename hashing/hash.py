import random
from math import sqrt


class HashTable:
    def __init__(self, M, C=None):
        if M == 0:
            raise Exception("M must be greater than 0")
        self.M = M
        self.C = C or (sqrt(5) - 1) / 2
        self.values = [None] * M

    @staticmethod
    def hash_mul(number, M, C):
        return int(M * ((C * number) % 1))

    def __repr__(self):
        return '\n'.join([str(i) + ": " + str(x) for i, x in enumerate(self.values) if x is not None])

    def add(self, value):
        hashed = HashTable.hash_mul(value, self.M, self.C)
        if type(self.values[hashed]) == set:
            self.values[hashed].add(value)
        elif self.values[hashed] is not None:
            if self.values[hashed] != value:
                self.values[hashed] = {self.values[hashed], value}
        else:
            self.values[hashed] = value

    def delete(self, value):
        hashed = HashTable.hash_mul(value, self.M, self.C)
        if type(self.values[hashed]) == set:
            try:
                self.values[hashed].remove(value)
                if len(self.values[hashed]) == 1:
                    temp = self.values[hashed].pop()
                    self.values[hashed] = temp
            except:
                raise Exception(f"no such value {value}")
        elif self.values[hashed] is not None:
            if self.values[hashed] == value:
                self.values[hashed] = None
            else:
                raise Exception(f"no such value {value}")
        else:
            raise Exception(f"no such value {value}")


def test_const(P, N, R, M, C):
    # для P наборов из N случайных ключей от 1 до R, при длине хеш-таблицы M.
    sizes = []
    for i in range(P):
        hash_table = HashTable(M, C)
        for j in range(N):
            hash_table.add(random.randint(1, R))
        size = 1
        for value in hash_table.values:
            if type(value) == set and len(value) > size:
                size = len(value)
        sizes.append(size)
    return sum(sizes) / len(sizes)


if __name__ == "__main__":
    consts = {}
    for c in [(sqrt(5) - 1) / 2, 0.61, 0.1, 0.33, 1, 2, 10, 0.11, 0.65]:
        consts[c] = test_const(100, 300, 500, 50, c)
    print(consts)
