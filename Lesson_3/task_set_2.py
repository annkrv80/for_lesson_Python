my_set = {1, 2, 4, 6}
other_set = {3, 4, 44, 777}
new_set = my_set.intersection(other_set)
print(f'{my_set}\n{other_set}\n{new_set}')
new_set_2 = my_set & other_set
print(f'{my_set}\n{other_set}\n{new_set_2}')

new_set = my_set.union(other_set)
print(f'{my_set}\n{other_set}\n{new_set}')

new_set_2 = my_set | other_set
print(f'{my_set}\n{other_set}\n{new_set_2}')

n_set = my_set.difference(other_set)
print(f'{my_set}\n{other_set}\n{n_set}')
n_set_2 = my_set - other_set
print(f'{my_set}\n{other_set}\n{n_set_2}')

print(42 in my_set)
