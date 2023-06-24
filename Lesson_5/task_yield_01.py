def factorial(n):
    number = 1
    res = []
    for i in range (1, n + 1):
        number *= i
        res.append(number)
    return res

for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')