#TODO - 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:

    @classmethod
    def separate(cls, date_created):
        dd, mm, year = map(int, date_created.split('-'))
        #print(f'День: {dd} \nМесяц: {mm} \nГод: {year}')
        return dd, mm, year

    @staticmethod
    def validate(date_created):
        list = Date.separate(date_created)
        if (list[0] <= 0 or list[0] > 31) or (list[1] <= 0 or list[1] > 12) or (list[2] <= 0 or list[2] > 2999):
            return print('Валидация не пройдена')


Date.validate('10-12-1993')

        

