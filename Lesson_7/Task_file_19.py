text =['Ты мой ребёнок, мой друг, мой брат',
    'Ты мой любовник, мой дуэлянт',
    'Люблю как ты выключаешь свет'
    'И говоришь: «Привет!»']
with open('new_text_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, file=f)