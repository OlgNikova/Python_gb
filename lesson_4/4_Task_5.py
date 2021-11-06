#TODO - 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce()

from functools import reduce


def func(param1, param2):
    return param1 * param2


lst = [x for x in range(100, 1001) if x % 2 == 0]
result = reduce(func, lst)
print(result)

