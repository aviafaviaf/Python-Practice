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
    return noise(x, y)


def noise(x, y):
    colors = [(0, 0, 0), (0.5, 0.5, 0.5), (1, 1, 1)]
    color_index = int(x * 3000 ** y * 3000 ** x * 25555 ** x * 999 ** x * 1000) % 3
    return colors[color_index]


main(shader)