#TODO - 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


cnt = input('Введите любое число:')
sp = [x for x in cnt]
sp_r = []
for x in range(len(sp)):
    if (x + 1) % 2 != 0:
        sp_r.append(sp[x])
    else:
        sp_r.insert(x - 1, sp[x])
print(sp_r)

