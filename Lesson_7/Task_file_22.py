last = before = 0
text =['Ты мой ребёнок, мой друг, мой брат',
    'Ты мой любовник, мой дуэлянт',
    'Люблю как ты выключаешь свет'
    'И говоришь: «Привет!»']
with open('new_text_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
        print(f'{last = }, {before = }')
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write("\n".join(text))