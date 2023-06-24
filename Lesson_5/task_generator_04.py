data = [1, 2, 4, 6, 11, 13]
res = []
for item in data:
    if item % 2 == 0:
        res.append(item)
print(f'{res=}')

data = [1, 2, 4, 6, 11, 13]
res = [item for item in data if item % 2 == 0]
print(f'{res=}')

