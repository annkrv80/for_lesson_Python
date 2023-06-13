my_list = [4, 8, 2, 12, 6, 3, 18]
sort_list = sorted(my_list) #функция sorted не меняет список, который получила в качестве агрумента
print(my_list, sort_list, sep='\n')
rev_list = sorted(my_list, reverse=True)
print(my_list, rev_list, sep=('\n'))
my_list.sort() #метод сорт менят первоночальный список
print(my_list)
my_list.sort(reverse=True)
print(my_list)