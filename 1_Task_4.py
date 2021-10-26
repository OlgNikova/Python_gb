import pandas
import numpy

# TODO - 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input("Введите любое положительное число: ")
length = len(number)
i = 0
x = number[i]
while i < length:
        if number[i] > x:
            x = number[i]
        i += 1
print(x)