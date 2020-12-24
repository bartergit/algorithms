from typing import List
import random


def test_search(function):
    def wrapper(x, N, M):
        array = sorted([random.randint(0, M) for _ in range(N)])
        index = function(array, x)
        if x in array:
            assert array[index] == x, "returned wrong index"
        else:
            assert index == -1
    return wrapper


@test_search
def binary_search(a: List[int], key: int) -> int:
    if len(a) == 0:
        return -1
    left = 0
    right = len(a) - 1
    global operations   #
    operations.append(1) # 
    while left <= right:
        mid = int((right + left)/2)
        if a[mid] < key:
            operations[-1] += 1
            left = mid + 1
        elif a[mid] > key:
            operations[-1] += 2
            right = mid - 1
        else:
            operations[-1] += 2
            return mid
    return -1


@test_search
def interpolation_search(a: List[int], key: int) -> int:
    if len(a) == 0:
        return -1
    global operations   #
    operations.append(1) #    
    left = 0 
    right = len(a) - 1
    operations[-1] += 1       #
    while a[left] < key and key < a[right]:
        operations[-1] += 2      #
        mid = int(left + (key - a[left]) * (right - left) / (a[right] - a[left]))
        if a[mid] < key:
            operations[-1] += 1  #
            left = mid + 1
        elif a[mid] > key:
            operations[-1] += 2  #
            right = mid - 1
        else:
            return mid
    operations[-1] += 1       #
    if a[left] == key: return left
    operations[-1] += 1       #
    if a[right] == key: return right
    return -1


if __name__ == "__main__":
    RANGE = 1000
    operations = []
    for _ in range(RANGE * 10):
        interpolation_search(random.randint(0,RANGE), random.randint(0,RANGE), random.randint(0,RANGE))
    print(f"avg compare operations for interpolation_search: {sum(operations) / len(operations)}")
    operations = []
    for _ in range(RANGE * 10):
        binary_search(random.randint(0,RANGE), random.randint(0,RANGE), random.randint(0,RANGE))
    print(f"avg compare operations for binary_search: {sum(operations) / len(operations)}")
