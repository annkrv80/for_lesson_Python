f = open('data.txt', 'wb')
f.write('Привет ' .encode('utf-8') + 'мир!'.encode('cp1251'))
f.close()

#f = open('data.txt', 'r', encoding='utf-8')#Ошибка прочтение файла не в той кодировке
#print(list(f))
#f.close()

f = open('data.txt', 'r', encoding='utf-8', errors=('replace'))
print(list(f))
f.close()