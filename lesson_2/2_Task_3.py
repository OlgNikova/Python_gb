#TODO - 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


mnth = int(input('Введите номер месяца: '))
keys = [x for x in range(1, 13)]
values = ['Зима' for x in range(2)] + ['Весна' for x in range(3)] + ['Лето' for x in range(3)] + ['Осень' for x in range(3)] + ['Зима' for x in range(1)]
dct1 = dict(zip(keys, values))
print(dct1.get(mnth + 1))


###or###

mnth = int(input('Введите номер месяца: '))
keys = [x for x in range(1, 13)]
values = ['Зима' for x in range(2)], ['Весна' for x in range(3)], ['Лето' for x in range(3)], ['Осень' for x in range(3)], ['Зима' for x in range(1)]
season = sum(values, [])
dct1 = dict(zip(keys, season))
print(dct1.get(mnth + 1))
