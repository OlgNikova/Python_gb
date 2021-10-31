import pandas
import numpy

# TODO - 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_sec = int(input("Сколько времени у вас это занимает (сек.)?"))
hours = time_sec // 3600
minute = time_sec % 3600 // 60
sec = time_sec % 3600 % 60
print(f'{hours:02}:{minute:02}:{sec:02}')
