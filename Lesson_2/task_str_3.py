txt = input('Введите текст: ')
if txt.isdigit():
    txt=int(txt)
    print(bin(txt))
    print(oct(txt))
    print(hex(txt))
elif txt.isascii():
    print('Текст написан в ASCII')
else:
    print('Тест написан не в ASCII')