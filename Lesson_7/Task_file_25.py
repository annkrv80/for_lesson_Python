SIZE = 33
with open('new_text_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(SIZE)) # в файле осталось ровно 33 симовла