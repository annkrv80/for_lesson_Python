data = 45
print(isinstance(data, int))

data = True
print(isinstance(data, int)) #TRUE and FALSE наследуются от класса int

data = 3.14
print(isinstance(data, (int, float, complex)))