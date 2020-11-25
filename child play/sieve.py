from graphics import *
import time

def draw(n:int):
    total = int(n ** 0.5) + 1
    width = WIDTH / total
    for i in range(total):
        for j in range(total):
            rect = Rectangle(Point(j * width, i * width), Point((j + 1) * width, (i + 1) * width))
            rect.draw(win)
            value = i * total + j
            if value <= n:
                label = Text(Point((j + 0.5) * width, (i + 0.5) * width), str(value))
                text_size = min(width / max(len(str(value)), 2), 30)
                print(text_size)
                label.setSize(int(text_size))
                label.draw(win)

def draw_cross(num, n):
    total = int(n ** 0.5) + 1
    i = num // total
    j = num % total
    width = WIDTH / total   
    line = Line(Point(j * width, i * width), Point((j + 1) * width, (i + 1) * width))
    line.setWidth(2)
    line.setOutline("red")
    line.draw(win)
    line = Line(Point((j+1) * width, i * width), Point(j * width, (i + 1) * width))
    line.setOutline("red")
    line.setWidth(2)
    line.draw(win)
    time.sleep(0.1)

def draw_circle(num, n):
    total = int(n ** 0.5) + 1
    i = num // total
    j = num % total
    width = WIDTH / total   
    circle = Circle(Point((j + 0.5) * width, (i + 0.5) * width), int(width / 2))
    circle.setOutline("green")
    circle.setWidth(2)
    circle.draw(win)
    time.sleep(0.1)

def sieve_and_draw(n:int):
    draw(n)
    prime_numbers = [False, False] + [True] * (n - 1)
    draw_circle(0, n)
    draw_circle(1, n)
    for number in range(len(prime_numbers[2:])):
        number += 2
        if number * number > n:
            if prime_numbers[number]:
                draw_circle(number, n)
            continue
        if prime_numbers[number]:
            draw_circle(number, n)
            for i in range(number * number, n + 1, number):
                prime_numbers[i] = False
                draw_cross(i, n)
    # for i in range(len(prime_numbers)):
    #     print(i, prime_numbers[i], end = ", ", sep = ": ")
    win.getMouse()
    win.close()
    return prime_numbers


if __name__ == '__main__':
    WIDTH = 800
    colors = ["yellow", "red", "green", "blue", "white", "brown", "orange", "pink", "gray"]
    colors = dict(zip(list(range(4)),colors))
    win = GraphWin('Face', WIDTH, WIDTH)
    try:
        sieve_and_draw(30)
    except:
        win.close()