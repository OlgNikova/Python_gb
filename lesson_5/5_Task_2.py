#TODO - 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

import os


path = 'C:\\Users\\Olga\\Desktop\\QA\\Задание PY с файлами\\'
os.chdir(path)


f = open(r'Файл для задания 2.txt', 'r', encoding='utf-8')

content = f.readlines()
print(f'Количество строк в данном файле: {len(content)}')

i = 1
for x in content:
    cnt_str = len(x.split())
    print(f'Количество слов в {i} строке: {cnt_str}')
    i += 1

f.close()
