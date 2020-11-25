from help import insertion_sort, test_k

def quicksort(arr, k = 0, start = 0, end = None):
    if end is None:
        end = len(arr) - 1
    if end <= start:
        return
    if len(arr) <= k:    
        insertion_sort(arr)
        return
    div_ind = (start + end) // 2
    divider = arr[div_ind]
    i, j = start, end
    while i <= j:
        while arr[i] < divider:
            i += 1
        while arr[j] > divider:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    quicksort(arr, k, start, j)
    quicksort(arr, k, i, end)
    return arr

if __name__ == "__main__":
    test_k(quicksort)

    

