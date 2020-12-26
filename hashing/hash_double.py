import random


class HashTable:
    def __init__(self, M, C=None):
        if M == 0:
            raise Exception("M must be greater than 0")
        self.M = M
        self.C = C or 0.61
        self.values = [None] * M
    
    @staticmethod
    def h1(number, M, C):
        return int(M * ((C * number) % 1))

    @staticmethod
    def h2(number, M, C):
        return number % (M - 1) + 1

    def __repr__(self):
        return "hash_table\n " + '\n '.join(
            [str(i) + ": " + str(x) for i, x in enumerate(self.values) if x is not None])

    def add(self, value):
        x = HashTable.h1(value, self.M, self.C)
        y = HashTable.h2(value, self.M, self.C)
        for i in range(self.M):
            if self.values[x] == None or self.values[x] == value:
                self.values[x] = value
                return
            x = (x + y) % self.M
        raise Exception("no available space")

    def find(self, value):
        x = HashTable.h1(value, self.M, self.C)
        y = HashTable.h2(value, self.M, self.C)
        for i in range(self.M):
            if self.values[x] is not None:
                if self.values[x] == value:
                    return x
                else:
                    return None
            x = (x + y) % self.M
        return -1

    def delete(self, value):
        key = self.find(value)
        if key == -1:
            raise Exception(f"no such a value {value}")
        else:
            self.values[key] = None


if __name__ == "__main__":
    h = HashTable(1024)
    random.seed(1)
    for i in range(0, 800):
        h.add(random.randint(1, 10000))
    print(h)
