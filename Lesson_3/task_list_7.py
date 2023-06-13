my_list = [2, 4, 6, 2, 8, 12, 8, 4, 2, 15, 22, 2]
spam = my_list.index(4) #первое вхождение элемента 
print(spam)
eggs = my_list.index(4, spam + 1, 90) #задаем участок поиска от предидущего значения до 90
print(eggs)
my_list.insert(2, 555) #вставить элемент на заданное место
print(my_list)
my_list.insert(-2, 777)
print(my_list)
my_list.remove(8) #удаление элемента по значению
print(my_list)