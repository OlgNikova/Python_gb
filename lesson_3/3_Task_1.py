#TODO - 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

'''
#вариант1
def func1(x, y):
    try:
        if y != 0:
            result = x / y
    except:
        pass
    return result

'''

'''
#вариант2
def func1(x, y):
    if y != 0:
        result = x / y
    else:
        return print('Деление на ноль невозможно')
    return result
'''


#вариант3
def func1(x, y):
    if y != 0:
        result = x / y
        return round(result, 2)
    return 'Деление на ноль невозможно'


x1 = int(input('Какое число будет первым? '))
y1 = int(input('Какое число будет вторым? '))

result1 = func1(x1, y1)
print(result1)


