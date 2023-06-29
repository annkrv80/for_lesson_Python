import random as rnd

data = [2, 6, 8, 22, 114]

print(f'{data = }')
rnd.shuffle(data)
print(f'{data = }')


print(f'{rnd.sample(data, 3) = }')
print(f'{rnd.sample(data, 3, counts=[1, 1, 1, 1, 100]) = }')