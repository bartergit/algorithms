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

def worst_fit(container_capacity, container_num, weights):
    container_weights = [container_capacity for _ in range(container_num)]
    for bin_weight in weights:
        max_difference = None
        max_index = None
        for i, container_weight in enumerate(container_weights):
            difference = container_weight - bin_weight
            if difference >= 0 and (max_difference is None or difference > max_difference):
                max_index = i
                max_difference = difference
        if max_index is None:
            return None
        container_weights[max_index] -= bin_weight
    return container_num - container_weights.count(container_capacity)


def main():
    container_capacity = 1
    container_num = 5
    weights = [0.3, 0.7, 0.4, 0.9, 1, 0.5]
    b1 = next_fit(container_capacity, container_num, weights)
    b2 = first_fit(container_capacity, container_num, weights)
    b3 = ordered_first_fit(container_capacity, container_num, weights)
    b4 = best_fit(container_capacity, container_num, weights)
    print("next_fit", b1)
    print("first_fit", b2)
    print("ordered_first_fit", b3)
    print("best_fit", b4)
    print("worst_fit", worst_fit(container_capacity, container_num, weights))


if __name__ == '__main__':
    main()
