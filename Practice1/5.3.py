import math
from math import cos, sin
import tkinter as tk


def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def main(shader):
    label = tk.Label()
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()


def sdf_func(x, y):
    return difference(box(x, y, 0.4), circle(x, y, 0.3))


def circle(x, y, radius):
    return x ** 2 + y ** 2 - radius ** 2


def box(x, y, radius):
    rads = 45 * math.pi / 180
    return (abs(x * cos(rads) - y * sin(rads)) + abs(x * sin(rads) + y * cos(rads)) - radius * 1.4) / 1.3


def difference(func1, func2):
    if func2 < 0:
        return -func2
    if func2 > 0 > func1:
        return max(-func2, func1)
    return func1


def shader(x, y):
    d = sdf_func(x - 0.5, y - 0.5)
    return d > 0, abs(d) * 3, 0


main(shader)