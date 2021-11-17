#TODO - 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, surname, name, position):
        Worker.name = name
        Worker.surname = surname
        Worker.position = position
        Worker._income = {2000: 100, 3000: 200, 4000: 300}


class Position(Worker):

    def get_full_name(self):
        self.full_name = (f'{Worker.surname} {Worker.name}')
        return self.full_name
        #print(f'Сотрудник {full_name}')

    def get_position(self):
        return self.position

    def get_total_income(self, wage):
        self.salary = Worker._income.get(wage) + int(wage)
        return self.salary


a = Position('Петров', 'Олег', 'Менеджер')
a.get_full_name()
a.get_total_income(2000)
print(f'Сотрудник {a.full_name} с должностью {a.position} получает запрплату {a.salary} тыс. руб.')
