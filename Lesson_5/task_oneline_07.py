a = b = c = 0
a  += 42
print(f'{a = } {b = } {c = }')

a = b = c = {1, 2, 3} # ПЛОХО!!!
a.add(42)
print(f'{a = } {b = } {c = }')