#TODO - 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

sp = [2, 2.9, 'Petr', False, [3, 5, 6], {'key_1': 'Petr', 'key_2': 'Ivan'}]
sp_type = []
for x in sp:
    sp_type.append(type(x))
print(sp_type)

###or###

sp = [2, 2.9, 'Petr', False, [3, 5, 6], {'key_1': 'Petr', 'key_2': 'Ivan'}]
for x in sp:
    sp_type = type(x)
    print(sp_type)









#TODO - 6.Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
'''
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название. Тогда значение — список значений-характеристик, например, список названий товаров.

Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
'''

keys = ('Name', 'Price', 'Count', 'Ul')
dist1 = dict(zip(keys, ('Принтер', 2000.00, 6, 'ед.')))
dist2 = dict(zip(keys, ('Сканер', 4000.00, 3, 'ед.')))
dist3 = dict(zip(keys, ('Монитор', 5000.00, 2, 'ед.')))
lst = [dist1, dist2, dist3]
lst_new = []
for x in range(3):
    v = (x + 1, lst[x])
    lst_new.append(v)
print(lst)
lst_new1 = []
for x in lst:
    dicth = x
    name = dicth.get(Name)
    Price = dicth.get(Price)
    Count = dicth.get(Count)
    Ul = dicth.get(Ul)
    lst_new1.append(name)
dct1 = dict(zip(keys, lst_new1))



