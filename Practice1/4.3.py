import math
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


def shader(x, y):
    return pacman(x, y), pacman(x, y), 0


def pacman(x, y):
    return (x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.13 and (x - 0.6) ** 2 + (y - 0.3) ** 2 > 0.005\
            and (y + 0.07 < 1 - 4 * x / 5 or y - 0.07 > 4 * x / 5)


main(shader)