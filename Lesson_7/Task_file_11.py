SIZE = 100 #читаем по 100 символов за раз
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res :=f.read(SIZE):
        print(res)