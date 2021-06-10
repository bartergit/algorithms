import random


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
    best_route = route
    while True:
        for i in range(len(route)):
            for k in range(i + 1, len(route)):
                new_route = two_opt_swap(best_route, i, k)
                new_distance = calculate_total_distance(new_route, distance_matrix)
                if new_distance < calculate_total_distance(best_route, distance_matrix):
                    best_route = new_route
        if route is best_route:
            break
        route = best_route
        print(best_route, calculate_total_distance(best_route, distance_matrix))
    return route


def create_distance_matrix(n: int):
    return [[random.randint(1, 30) for _ in range(n)] for _ in range(n)]

def beauty_print_matrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matrix]))

def main() -> None:
    random.seed(4)
    N = 100
    distance_matrix = create_distance_matrix(N)
    beauty_print_matrix(distance_matrix)
    initial_route = list(range(N))
    print(calculate_total_distance(initial_route, distance_matrix))
    result_route = find_path(initial_route, distance_matrix)
    distance = calculate_total_distance(result_route, distance_matrix)
    print(result_route, distance)
    assert len(result_route) == N


if __name__ == '__main__':
    main()
