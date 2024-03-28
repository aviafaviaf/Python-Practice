from random import choice, randint
from string import ascii_uppercase

print(''.join([choice(ascii_uppercase) for _ in range(randint(0, 100))]))