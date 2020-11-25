import random
import time

def insertion_sort(arr):
    i = 1
    ops = 3                               
    while i < len(arr):                 
        ops += 2
        x = arr[i]                        
        ops += 2
        j = i - 1                         
        ops += 3
        while j >= 0 and arr[j] > x:     
            ops += 3
            arr[j + 1] = arr[j]            
            ops += 4
            j -= 1                          
            ops += 2
        arr[j + 1] = x                    
        ops += 3
        i += 1                            
        ops += 2
    print(ops, end=" ")
    return arr
    #1 + (N-1)11 + (N-1)4.5N
    #3 + (N-1)14 + (N-1)4.5N


def test_basic_python_sort(function):  
    for k in range(0, 20):
        start_time = time.time()
        arr = [random.randint(0, 10_000 + random.randint(0, 2)) for x in range(10)]
        function(arr[:], k)
        quick_time = time.time() - start_time
        start_time = time.time()
        arr.sort()
        py_time = time.time() - start_time
        print(quick_time < py_time)

def test_k(function):
    times = []
    NUMBER_OF_SORTS = 10
    ARRAY_LEN = 10_000
    ARRAY_RANGE = 100_000
    K_RANGE = 30
    arrays = [[random.randint(0, ARRAY_RANGE + random.randint(0, 2)) for x in range(ARRAY_LEN)] for i in range(NUMBER_OF_SORTS)]
    for k in range(K_RANGE):
        start_time = time.time()
        for i in range(NUMBER_OF_SORTS):
            # function(arrays[i][:], k)
            if function(arrays[i][:], k) != sorted(arrays[i]):
                raise Exception("wrong result")
        times.append(time.time() - start_time)
    print(times)
    print(times.index(min(times)))



if __name__ == "__main__":
    # start_time = time.time()
    # for N in range(1000):
    #     merge_sort([randint(0,10_000) for x in range(10_000)])
    # print(time.time() - start_time)
    for N in range(1,15):
        insertion_sort(list(reversed(list(range(N)))))
        print( 3 + (N-1)*12 + (N-1)*4.5*N)
