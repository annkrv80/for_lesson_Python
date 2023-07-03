text =['Ты мой ребёнок, мой друг, мой брат',
    'Ты мой любовник, мой дуэлянт',
    'Люблю как ты выключаешь свет'
    'И говоришь: «Привет!»']
with open('new_text_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell()) #tell передает информацию о положении курсора
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())
print(f.tell())# ошибка файл закрыт