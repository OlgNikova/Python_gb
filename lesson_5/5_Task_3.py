#TODO - 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

import os


path = 'C:\\Users\\Olga\\Desktop\\QA\\Задание PY с файлами\\'
os.chdir(path)

f = open(r'Файл для задания 3.txt', 'r', encoding='utf-8')

lst_rnd = []
for x in f:
    lst_rnd.append(x.split())
    dct = dict(lst_rnd)

summ = 0
lst = []
for y in dct.keys():
    summ += int(dct.get(y))
    if int(dct.get(y)) > 20000:
        lst.append(y)


avg_salary = summ / len(dct)
sp_name = ', '.join(lst)
print(f'Сотрудники, имеющие оклад менее 20000.0 руб.: {sp_name}.')
print(f'Средний оклад сотрудников: {avg_salary} руб.')
f.close()
