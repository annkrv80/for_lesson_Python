a = 5                 #числа и строки неизменяемые типы данных
print(a, id(a))
a += 1
print(a, id(a))

txt =  'Hello world'
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))

# hash - проверка на изменяемость hash нельзя вычеслить для неизменяемого обьекта

x = 42
y = 'text'
z = 3.14
print(hash(x), hash(y), hash(z))
my_list = [x, y, z] # изменяемый тип данных
print(hash(my_list))

