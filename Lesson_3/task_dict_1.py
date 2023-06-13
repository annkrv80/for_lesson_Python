my_dict = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
b = dict(one=42, two=3.14, ten='Hello world!')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
print(my_dict == b == c)
x = 10
my_dict['four'] = x
TEN = 'ten'
print(my_dict)
print(my_dict['two'])
print(my_dict[TEN])

print(my_dict.get('one'))
print(my_dict.get('five'))
print(my_dict.get('five', 5)) #5 значание по умолчанию
print(my_dict.get('ten', 4))