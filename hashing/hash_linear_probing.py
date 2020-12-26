class HashTable:
    def __init__(self, M, C=None):
        if M == 0:
            raise Exception("M must be greater than 0")
        self.M = M
        self.C = C or 0.61
        self.values = [None] * M

    @staticmethod
    def hash_mul(number, M, C):
        return int(M * ((C * number) % 1))

    def __repr__(self):
        return "hash_table:\n " + '\n '.join(
            [str(i) + ": " + str(x) for i, x in enumerate(self.values) if x is not None])

    def add(self, value):
        hashed = HashTable.hash_mul(value, self.M, self.C)
        counter = 0
        while self.values[hashed] != value and self.values[hashed] is not None and counter != self.M:
            counter += 1
            hashed = (hashed + 1) % self.M
        if counter != self.M:
            self.values[hashed] = value
        else:
            raise Exception("no available space")

    def find(self, value):
        hashed = HashTable.hash_mul(value, self.M, self.C)
        counter = 0
        while self.values[hashed] != value and self.values[hashed] is not None and counter != self.M:
            counter += 1
            hashed = (hashed + 1) % self.M
        if self.values[hashed] == value:
            return hashed
        else:
            return -1

    def delete(self, value):
        key = self.find(value)
        if key == -1:
            raise Exception(f"no such a value {value}")
        else:
            self.values[key] = None


if __name__ == "__main__":
    h = HashTable(10)
    for i in range(0, 5):
        h.add(3)
    print(h)
