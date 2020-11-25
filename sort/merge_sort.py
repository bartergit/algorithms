from help import insertion_sort, test_k
import time
import random

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(array, k):
    if len(array) <= k or len(array) == 1:
        return insertion_sort(array)
    else:
        middle = int(len(array) / 2)
        left = merge_sort(array[:middle], k)
        right = merge_sort(array[middle:], k)
        return merge(left, right)

if __name__ == "__main__":
    start_time = time.time()
    for N in range(1000):
        merge_sort([random.randint(0,10_000) for x in range(10_000)], k = 0)
    print(time.time() - start_time)