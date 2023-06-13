my_set = {1, 2, 3, 4, 5, 10, 2} #хранит только уникальные элементы
print(my_set)

my_f_set = frozenset((1, 4, 7, 2, 10, 10))
print(my_f_set)
my_set.add(7)
print(my_set)
my_set.add((9, 10))
print(my_set)
my_set.remove(2)
print(my_set)
my_set.discard(10)
print(my_set)
my_set.discard(12) #при попытке удалить несуществующий элемент discard не вызывает ошибку
print(my_set)