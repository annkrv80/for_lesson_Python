def add_two_def(a, b):
    return a + b 


add_two_def_lambda = lambda a, b: a + b #lambda анонимная функция и присаевать ее неверно

print(add_two_def(42, 3.14))
print(add_two_def_lambda(42, 3.14))

my_dict = {'one': 1, 'two': 2, 'tree': 3, 'ten': 10}
s_key = sorted(my_dict.items())
s_values = sorted(my_dict.items(), key= lambda x: x[1])
print(s_key)
print(s_values)
