from matplotlib import pyplot as plt
import numpy as np

SIZE = 5

sprite = np.random.randint(0, 2, size=(SIZE, SIZE))
sprite = np.maximum(sprite, list(map(lambda line: line[::-1], sprite)))
plt.imshow(sprite, cmap='gray')
plt.show()