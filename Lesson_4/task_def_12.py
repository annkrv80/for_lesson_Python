LIMIT = 1000

def func (x, y):
    result = x ** y % LIMIT
    return result

print(func(42, 73))