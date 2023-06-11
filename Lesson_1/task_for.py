num = int(input('Введите число: '))
for i in range(0,num,2):
    print(i)

animals = ['Кошка','Собака','Волк','Лиса','Тигр']
for i, animal in enumerate(animals, start=1):
    print(i,animal)