#TODO - 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import functools
import os


def func(param1, param2):
    return int(param1) + int(param2)


path = 'C:\\Users\\Olga\\Desktop\\QA\\Задание PY с файлами\\'
os.chdir(path)

lst = []
sp_cnt = input('Введите числа: ')
with open('Файл для задания 5.txt', '+w', encoding='utf-8') as f:
    f.write(sp_cnt)
    f.seek(0)
    for line in f:
        lst = line.split()
    result = functools.reduce(func, lst)
    print(f'Сумма введенных значений: {result}')
