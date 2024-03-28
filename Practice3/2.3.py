from random import randint, choice

PALETTE = [
    0x1D2B53,
    0x7E2553,
    0x008751,
    0xAB5236,
    0x5F574F,
    0xC2C3C7,
    0xFFF1E8,
    0xFF004D,
    0xFFA300,
    0xFFEC27,
    0x00E436,
    0x29ADFF,
    0x83769C,
    0xFF77A8,
    0xFFCCAA
]

ROW_SIZE = 16
COLUMN_SIZE = 8
SPACE = 3
SIZE = 10
COLORS_FOR_SPRITE_COUNT = 4

s = SIZE + SPACE * 2
rgb_palette = list(map(lambda color: [color >> 16, (color >> 8) & 0xFF, color & 0xFF], PALETTE))

sprites = np.zeros(s * s * COLUMN_SIZE * ROW_SIZE * 3).reshape(s * COLUMN_SIZE, s * ROW_SIZE, 3)
for i_column in range(COLUMN_SIZE):
    for i_row in range(ROW_SIZE):
        colors = np.array([choice(rgb_palette) for _ in range(COLORS_FOR_SPRITE_COUNT)])
        for i in range(SIZE):
            for j in range(SIZE):
                sprites[i_column * s + i + SPACE][i_row * s + j + SPACE] = randint(0, 1) * choice(colors)
                sprites[i_column * s + i + SPACE][i_row * s + (s - SPACE) - j - 1] = sprites[i_column * s + i + SPACE][
                    i_row * s + j + SPACE]

plt.imshow(sprites.astype('uint8'), interpolation='none')
plt.show()