# Программа получает в качестве аргументов имена фалов
# и проводит их объединение

import sys

file_names = sys.argv
# Если аргументы не переданы, завершаем программу
if len(file_names) <2:
    print('Необходимо в качестве аргументов передать имена файлов')
    sys.exit()

for i in range(1, len(file_names)):
    try:
        with open(file_names[i], 'r', encoding='utf-8') as f:
             file_text = f.read()
    except FileNotFoundError:
        print(f'Файл {file_names[i]} не найден.')
        continue

    with open('result_file.txt', 'a', encoding='utf-8') as f:
        f.write((file_text + '\n'))
        print(f'{i}: File {file_names[i]} successful copied')