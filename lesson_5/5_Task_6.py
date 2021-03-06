#TODO - 6. Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
# Физика:   30(л)   —   10(лаб)
# Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import os

path = 'C:\\Users\\Olga\\Desktop\\QA\\Задание PY с файлами\\'
os.chdir(path)

d = {}

with open('Файл для задания 6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lineList = line.split()
        key = lineList[0][0:-1]
        lineList.reverse()
        lineList.pop()
        d[key] = 0
        for x in lineList:
            i = x.find('(')
            if i != -1:
                value = x[0:i]
                d[key] = d.get(key) + int(value)

print(d)
