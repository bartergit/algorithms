from graphics import *
import time

def move(from_index, to_index):
    if len(columns[to_index]) == 0 or columns[to_index][-1] > columns[from_index][-1]:
        columns[to_index].append(columns[from_index].pop())
    else:
        raise ValueError

def draw(columns):
    for item in win.items[:]:
        item.undraw()
    win.update()
    width = (WIDTH - 40) / n / 3
    height = HEIGHT / 2 / n
    x = width/2 * n + 10
    for column in columns:
        line = Line(Point(x, HEIGHT/2), Point(x, HEIGHT))
        line.draw(win)
        y = HEIGHT
        for value in column:
            rect = Rectangle(Point(x - value * width/2, y), Point(x + value * width/2, y - height))
            rect.setFill(colors.get(value,"black"))
            rect.draw(win)
            y -= height
        x += width * n + 10


def recursion_step(this, where, level):
    free = 3 - this - where
    if level == 1:
        time.sleep(0.2)
        move(this, where)
        draw(columns)
        global step
        step += 1
        print("step:", step, "out of", 2**n - 1)
    if level >= 2:
        recursion_step(this, free, level - 1)
        recursion_step(this, where, 1)
        recursion_step(free, where, level - 1)


def solve_hanoi(n):
    draw(columns)
    recursion_step(0, 1, n)



if __name__ == "__main__":
    WIDTH = 950
    HEIGHT = 400
    step = 0
    n = 6
    colors = ["yellow", "red", "green", "blue", "white", "brown", "orange", "pink", "gray"]
    colors = dict(zip(list(range(n)),colors))
    print(colors)
    column0 = [i for i in range(n, 0, -1)]
    column1 = []
    column2 = []
    columns = [column0, column1, column2]
    flag = True
    win = GraphWin('hanoi towers', 950, 400)
    solve_hanoi(n)
    win.getMouse()
    win.close()
