def shcool_print(**kwargs):
    for key, values in kwargs.items():
        print(f'По впредмету {key} получена оценка {values=}')

shcool_print(химия=5, физика=5)
