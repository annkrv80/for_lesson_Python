text = ['И вот однажды я поняла',
    'Что без тебя словно не жила',
    'Когда ты даришь мне роз букет',
    'Я говорю: «Привет!»']
with open('text_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(f'{line}\n')#добавим \n чтобы записать построчно
        print(f'{res = }\n{len(line) = }')