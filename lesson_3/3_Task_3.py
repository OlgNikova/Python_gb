#TODO - 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.


#вариант2 - если любой размер списка, но всегда нужно сумму 2 элементов
def my_func(lst):
    for x in range(len(lst) - 2):
        v = lst.remove(min(lst))
    summ = sum(lst)
    return summ


print(my_func([3, 6, 2]))



'''
#еще можно через сортировку, это было бы корректно? или нужно через if? как оптимальнее?
#вариант1 - работает только для трех значений
def my_func(lst):
    v = lst.remove(min(lst))
    summ = sum(lst)
    return summ
'''


'''
#вариант3
def my_func(lst):
    lst1 = []
    for x in range(2):
        lst1.append(max(lst))
        lst.remove(max(lst))
    summ = sum(lst1)
    return summ
'''