#TODO - 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(x):
    sp = x.split()
    sp1 = []
    for i in sp:
        sp1.append(i[0].upper() + i[1:])
    return ' '.join(sp1)


sp_ttl = input('Напишите слова: ')
wrd = int_func(sp_ttl)
print(wrd)
