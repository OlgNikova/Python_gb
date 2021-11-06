#TODO - 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами

from sys import argv

script_name, hours_work, hours_tax, premium = argv

print("Имя скрипта: ", script_name)
print("Отработанные часы: ", hours_work)
print("Часовая ставка: ", hours_tax)
print("Премия: ", premium)


def func_salary(hours_work, hours_tax, premium):
    salary = (int(hours_work) * int(hours_tax)) + int(premium)
    return salary


print('Заработная плата:', func_salary(hours_work, hours_tax, premium), 'руб.')

















