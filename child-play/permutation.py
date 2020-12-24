from itertools import permutations as it_permutations

def permutation(M, level):
    if level < 0:
        raise ValueError
    if level == 0:
        return []
    if level == 1:
        output = []
        for i in range(1, M + 1):
            if str(i) not in output:
                output.append(str(i))
        return output
    if level >= 2:
        our = []
        output = permutation(M, level - 1)
        for i in range(len(output)):
            for j in range(1, M + 1):
                if str(j) not in output[i]:
                    our.append(output[i] + str(j))
        return our


print(permutation(3, 3))
print(list(it_permutations(range(1,4),3)))