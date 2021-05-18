import random


# procedure 2optSwap(route, i, k) {
#     1. take route[0] to route[i-1] and add them in order to new_route
#     2. take route[i] to route[k] and add them in reverse order to new_route
#     3. take route[k+1] to end and add them in order to new_route
#     return new_route;
# }
# repeat until no improvement is made {
#     best_distance = calculateTotalDistance(existing_route)
#     start_again:
#     for (i = 0; i <= number of nodes eligible to be swapped - 1; i++) {
#         for (k = i + 1; k <= number of nodes eligible to be swapped; k++) {
#             new_route = 2optSwap(existing_route, i, k)
#             new_distance = calculateTotalDistance(new_route)
#             if (new_distance < best_distance) {
#                 existing_route = new_route
#                 best_distance = new_distance
#                 goto start_again
#             }
#         }
#     }
# }
from pprint import pprint


def two_opt_swap(route, i, k):
    new_route = []
    new_route += route[0:i]  # i i +1   k k +1  -> i k i+1 k + 1
    new_route += reversed(route[i:k + 1])
    new_route += route[k + 1:]
    return new_route


def calculate_total_distance(route, distance_matrix):
    sum = 0
    for i, _ in enumerate(route):
        if i == len(route) - 1:
            return sum
        sum += distance_matrix[route[i]][route[i+1]]

def find_path(route, distance_matrix):
    best_distance = calculate_total_distance(route, distance_matrix)
    for i in range(len(route)):
        for k in range(i + 1, len(route)):
            new_route = two_opt_swap(route, i, k)
            new_distance = calculate_total_distance(new_route, distance_matrix)
            if new_distance < best_distance:
                return find_path(new_route, distance_matrix)
    return route


def create_distance_matrix(n: int):
    return [[random.randint(1, 50) for _ in range(n)] for _ in range(n)]

def beauty_print_matrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matrix]))

def main() -> None:
    random.seed(50)
    N = 10
    distance_matrix = create_distance_matrix(N)
    beauty_print_matrix(distance_matrix)
    initial_route = list(range(N))
    result_route = find_path(initial_route, distance_matrix)
    distance = calculate_total_distance(result_route, distance_matrix)
    print(result_route, distance)
    assert len(result_route) == N


if __name__ == '__main__':
    main()
