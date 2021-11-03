#TODO - 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def func1(firstName, lastName, bYear, city, email, phone):
    print(f"{firstName}; {lastName}; {bYear}; {city}; {email}; {phone}")
#вариант2
    #data = [firstName, lastName, bYear, city, email, phone]
    #sp = '; '.join(data)
    #return print(sp)


func1(firstName='Ольга', lastName='Петрова', bYear='1996', city='Омск', email='qwe@qwe.ru', phone='89078765678')


