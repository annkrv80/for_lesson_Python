lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [('Иван', 125000),('Ян', 109000), ('Петр', 196000)]
print(max(lst_1, default='empty'))
print(max(*lst_2))
print(max(lst_3, key=lambda x: x[1])) #x[1] обращаемся ко второму элементу зп x[0] - обращение к имени