name = input('Введи имя: ')
if name:
    print('Привет, ', + name)
else:
    print('Привет, аноним')

data = [2, 6, 21, 18, 45, 88]
while data:
    print(data.pop())