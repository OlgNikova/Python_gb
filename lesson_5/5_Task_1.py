#TODO - 1.Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

import os

path = 'C:\\Users\\Olga\\Desktop\\QA\\Задание PY с файлами\\'
os.chdir(path)


with open('Файл для задания 1.txt', 'w', encoding='utf-8') as f:
    while True:
        date_user = input('Введите данные: ')
        if len(date_user.split()) == 0:
            break
        else:
            f.writelines(date_user + '\n')

#f = open(r'Файл для задания 1.txt', 'r')
#f.close()
#content = f.read()
#print(content)
