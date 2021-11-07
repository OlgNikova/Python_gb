#TODO - 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import os


path = 'C:\\Users\\Olga\\Desktop\\QA\\Задание PY с файлами\\'
os.chdir(path)

fs = open(r'Файл для задания 4_1.txt', 'w', encoding='utf-8')

dct = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('Файл для задания 4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lst = line.split()
        new_cnt = line.replace(lst[0], dct.get(lst[0]))
        fs.writelines(new_cnt)

fs.close()
