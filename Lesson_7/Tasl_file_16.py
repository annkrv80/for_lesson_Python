text="Ну где ты был, ну обними меня скорей!"
with open('text_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')