# 1) в пустой (мёртвой) клетке, рядом с которой ровно три живые клетки, зарождается жизнь;
# 2) если у живой клетки есть две или три живые соседки, то эта клетка продолжает жить; в противном случае, 
# если соседей меньше двух или больше трёх, клетка умирает («от одиночества» или «от перенаселённости»)
import time


def count_neighbours(x, y, live_cells, to_die, to_add, size, is_alive=True):
    counter = 0
    directions = (1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1), (-1, -1), (1, 1)
    for dx, dy in directions:
        if ((x + dx) % size, (y + dy) % size) in live_cells:
            counter += 1
        elif is_alive:
            count_neighbours((x + dx) % size, (y + dy) % size, live_cells, to_die, to_add, size, False)
    if counter == 3 and not is_alive:
        to_add.add((x, y))
    if counter < 2 or counter > 3:
        to_die.add((x, y))


def print_grid():
    for i in range(size):
        for j in range(size):
            print("#" if (i, j) in live_cells else "-", end="")
        print()
    time.sleep(0.3)


def evolve(live_cells, to_die, to_add):
    return (live_cells - to_die) | to_add


# different shapes of life
def blinker(x, y):
    return {(x, y), (x + 1, y), (x + 2, y)}


def glider(x, y):
    return {(x, y), (x + 1, y + 1), (x + 2, y + 1), (x + 1, y + 2), (x, y + 2)}


def tub(x, y):
    return {(x, y), (x + 1, y + 1), (x - 1, y - 1), (x, y + 2)}


def toad(x, y):
    return {(x, y), (x, y + 1), (x + 1, y + 2), (x + 2, y - 1), (x + 3, y), (x + 3, y + 1)}


def block(x, y):
    return {(x, y), (x + 1, y + 1), (x + 1, y), (x, y + 1)}


# ----------------------------

if __name__ == "__main__":
    size = 10
    live_cells = glider(7, 7)
    i = 0
    print(f"generation number: {i}")
    print_grid()
    while live_cells:
        to_die = set()
        to_add = set()
        i += 1
        print(f"generation number: {i}")
        for cell in live_cells:
            count_neighbours(*cell, live_cells, to_die, to_add, size)
        live_cells = evolve(live_cells, to_die, to_add)
        print_grid()
        print()
