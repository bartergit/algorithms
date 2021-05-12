import random
def next_fit(container_capacity, container_num, weights):
    pointer = 0
    value = 0
    for weight in weights:
        while weight + value > container_capacity:
            pointer += 1
            if pointer == container_num:
                return None
            value = 0
        value += weight
    return pointer + 1


def first_fit(container_capacity, container_num, weights):
    container_weights = [container_capacity for _ in range(container_num)]
    for bin_weight in weights:
        for i, container_weight in enumerate(container_weights):
            if container_weight - bin_weight >= 0:
                container_weights[i] -= bin_weight
                break
            if i == len(container_weights) - 1:
                return None
    return container_num - container_weights.count(container_capacity)


def ordered_first_fit(container_capacity, container_num, weights):
    return first_fit(container_capacity, container_num, list(sorted(weights)))


def first_fit_decreased(container_capacity, container_num, weights):
    return first_fit(container_capacity, container_num, list(sorted(weights, reverse=True)))


def best_fit(container_capacity, container_num, weights):
    container_weights = [container_capacity for _ in range(container_num)]
    for bin_weight in weights:
        min_difference = None
        min_index = None
        for i, container_weight in enumerate(container_weights):
            difference = container_weight - bin_weight
            if difference >= 0 and (min_difference is None or difference < min_difference):
                min_index = i
                min_difference = difference
        if min_index is None:
            return None
        container_weights[min_index] -= bin_weight
    return container_num - container_weights.count(container_capacity)


def main():
    random.seed(100)
    nums = [random.uniform(0, 1) for _ in range(4000)]
    container_capacity = 1
    container_num = 4000
    print(next_fit(container_capacity, container_num, nums))
    print(best_fit(container_capacity, container_num, nums))
    print(first_fit(container_capacity, container_num, nums))
    print(first_fit_decreased(container_capacity, container_num, nums))


if __name__ == '__main__':
    main()
