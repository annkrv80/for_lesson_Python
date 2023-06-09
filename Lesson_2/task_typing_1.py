def my_fuc(data: list[int, float]) -> float:
    res = sum(data) / len (data)
    return res

print(my_fuc([2, 3.14, 5, 6.95, 10]))