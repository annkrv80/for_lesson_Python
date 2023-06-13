my_dict = {'one':1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault('five')
print(f'{spam = }\t{my_dict}')

eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict}')

for key in my_dict.keys():
    print(key)

for values in my_dict.values():
    print(values)


my_dict_2 = {'one':1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict_2.items())

for key, value in my_dict_2.items():
    print(f'{key = } value before 100 {100 - value}')

sp = my_dict_2.popitem()
print(f'{sp = }\t{my_dict_2}')

eg = my_dict_2.pop('two')
print(f'{eg}\t{my_dict_2}')

my_dict_2.update(dict(six=6))
print(my_dict_2)

my_dict_2.update(dict([('one', 42), ('two', 55) ]))
print(my_dict_2)