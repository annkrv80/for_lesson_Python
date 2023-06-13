import copy


my_list = [2, 4, 10, 3, 6, 0, 24, 77, 71]
new_list = my_list.copy()
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n')

matrix =[ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = matrix.copy()
print(matrix, new_matrix, sep='\n')
matrix[0][1] = 555
print(matrix, new_matrix, sep='\n')
new_m  = copy.deepcopy(matrix)
matrix[0][1] = 777
print(matrix, new_m, sep='\n')