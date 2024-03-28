from random import randint
import numpy as np
from matplotlib import pyplot as plt

ROW_SIZE = 16
COLUMN_SIZE = 8
SPACE = 3
SIZE = 10

s = SIZE + SPACE * 2

sprites = np.zeros(s * s * COLUMN_SIZE * ROW_SIZE).reshape(s * COLUMN_SIZE, s * ROW_SIZE)
for i_column in range(COLUMN_SIZE):
    for i_row in range(ROW_SIZE):
        for i in range(SIZE):
            for j in range(SIZE):
                sprites[i_column * s + i + SPACE][i_row * s + j + SPACE] = randint(0, 1)
                sprites[i_column * s + i + SPACE][i_row * s + (s - SPACE) - j - 1] = sprites[i_column * s + i + SPACE][
                    i_row * s + j + SPACE]

plt.imshow(sprites, cmap='gray', interpolation='none')
plt.show()