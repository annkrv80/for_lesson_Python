import random as rnd

START = -100
STOP = 1000
STEP = 10
data = [2, 8, 10, 15, 25, 145]

print(f'{rnd.randint(START, STOP) = }')
print(f'{rnd.uniform(START, STOP) = }')
print(f'{rnd.choice(data) = }')
print(f'{rnd.randrange(START, STOP, STEP) = }')