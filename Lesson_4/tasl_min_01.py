lst_1 = []
lst_2 = [42, -854, 9652]
lst_3 = [('Иван', 125000),('Ян', 109000), ('Петр', 196000)]
print(min(lst_1, default='NONE'))
print(min(*lst_2))
print(min(lst_3, key=lambda x: x[1]))