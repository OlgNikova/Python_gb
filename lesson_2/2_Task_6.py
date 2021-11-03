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
lst = [dict(zip(keys, ('Принтер', 2000.00, 6, 'ед.'))), dict(zip(keys, ('Сканер', 4000.00, 3, 'ед.'))), dict(zip(keys, ('Монитор', 5000.00, 2, 'ед.')))]
lst_new = []
for x in range(3):
    v = (x + 1, lst[x])
    lst_new.append(v)
lst_new1, lst_new2 = [], []
for x1 in keys:
    lst_new2.clear()
    for x2 in lst_new:
        v2 = x2[1].get(x1)
        lst_new2.append(v2)
    lst_new1.append(list(set(lst_new2)).copy())
dct1 = dict(zip(keys, lst_new1))
print(dct1)
