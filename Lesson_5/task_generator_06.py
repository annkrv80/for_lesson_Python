x = [1, 1, 2, 5, 6, 7, 12]
y = [3, 44, 5, 6, 8, 10]
print(f'{len(x)=} \t{len(y)=}')
res = [i + j for i in x if i % 2 != 0 for j in y if j != 1] #если нужен доспут ко всем данным сразу
print(f'{len(res)=}\n{res}')

mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)#если нужен дрспут к каждому элементу
for item in mult:
    print(f'{item =}')