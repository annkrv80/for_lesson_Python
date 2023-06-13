my_list = [4, 8, 2, 12, 6, 3, 18]
res = reversed(my_list)
print(res)

res = list(reversed(my_list)) #для того чтобы развернуть список оборачиваем его в list
print(res)


for item in reversed(my_list): #Перебираем элементы задом на перед 
    print(item)

my_list.reverse() #метод reverse разворачивает список на месте не создавая новый обьект
print(my_list)

new_my_list = my_list[::-1] #разворот срезом от начало до конца списка в обратном порядке
print(new_my_list)


