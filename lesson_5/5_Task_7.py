#TODO - 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import os
import json

path = 'C:\\Users\\Olga\\Desktop\\QA\\Задание PY с файлами\\'
os.chdir(path)


lineList, lst_key, lst_values = [], [], []
i = 0
summ = 0
with open('Файл для задания 7.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lineList.append(line.split())
        lst_key.append(lineList[i][0])
        pr = int(lineList[i][2]) - int(lineList[i][3])
        lst_values.append(pr)
        if pr > 0:
            summ += pr
        i += 1

dct_frm = dict(zip(lst_key, lst_values))

avg = summ / len(lineList)
dct_avg = dict(average_profit=avg)

fl_for_json = [dct_frm, dct_avg]

with open("Файл для задания 7_1.json", "w") as f_j:
    json.dump(fl_for_json, f_j)
