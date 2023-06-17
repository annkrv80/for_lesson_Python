def func(y):
    global x
    x += 100
    print(x)
    return y + 1


x = 42
print(x)
z = func(x)
print(f'{x}\t{z}')