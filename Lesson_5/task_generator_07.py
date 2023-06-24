my_setcomp = {chr(i) for i in range(97, 123)}
print(my_setcomp)
for char in my_setcomp:
    print(char)


x = [1, 1, 2, 5, 6, 7, 12]
y = [3, 44, 5, 6, 8, 10]
print(f'{len(x)=} \t{len(y)=}')
res = {i + j for i in x if i % 2 != 0 for j in y if j != 1} 
print(f'{len(res)=}\n{res}')