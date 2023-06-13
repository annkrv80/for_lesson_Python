name = 'Alex'
age = 20
text = 'Привет, меня зовут %s и мне %d лет' % (name, age)
print(text)
text = 'Привет, меня зовут {} и мне {} лет'.format(name, age)
print(text)
text = f'Привет, меня зовут {name} и мне {age} лет'
print(text)
print(f'{{Фигурная скобка}}')