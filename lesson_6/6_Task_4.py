#TODO - 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


#изначально не так поняла задание, обелегченный вариант ниже
class Car:

    def __init__(self, speed, color, name, is_police, type):
        Car.speed = speed
        Car.color = color
        Car.name = name
        Car.type = type
        Car.is_police = is_police

    def go(self):
        return print(f'{Car.color} {Car.name} едет')

    def stop(self):
        return print(f'{Car.color} {Car.name} остановилась')

    def turn(self, direction):
        return print(f'{Car.color} {Car.name} повернула {direction}')

    def show_speed(self):
        return print(f'{Car.color} {Car.name} едет со скоростью {Car.speed} км/ч.')


class TownCar(Car):

    def show_speed(self):
        if Car.speed > 60:
            return print('Скорость превышена')
        else:
            return print(f'{Car.color} {Car.name} едет со скоростью {Car.speed} км/ч.')

class SportCar(Car):

    def show_speed(self):
        return print(f'{Car.color} {Car.name} едет со скоростью {Car.speed} км/ч.')


class WorkCar(Car):

    def show_speed(self):
        if Car.speed > 40:
            return print('Скорость превышена')
        else:
            return print(f'{Car.color} {Car.name} едет со скоростью {Car.speed} км/ч.')


class PoliceCar(Car):

    def stop_police(self):
        if Car.is_police == True:
            if Car.type == "TownCar" and Car.speed > 60:
                print(f'{Car.color} {Car.name} остановитесь! Вы превысили скорость на {Car.speed - 60} км/ч.')
                a.stop()
            if Car.type == "WorkCar" and Car.speed > 40:
                print(f'{Car.color} {Car.name} остановитесь! Вы превысили скорость на {Car.speed - 40} км/ч.')
                a.stop()
            else:
                print(f'{Car.color} {Car.name} не нарушает правила')


a = Car(40, 'Желтая', 'Лада', True, 'WorkCar')
a.go()
turn_u = input('Куда поворачивает машина? ')
a.turn(turn_u)

if a.type == 'TownCar':
    b = TownCar(40, 'Желтая', 'Лада', True, 'TownCar')
    f = PoliceCar(40, 'Желтая', 'Лада', True, 'TownCar')
    b.show_speed()
    f.stop_police()
if a.type == 'WorkCar':
    c = WorkCar(40, 'Желтая', 'Лада', True, 'WorkCar')
    f = PoliceCar(40, 'Желтая', 'Лада', True, 'WorkCar')
    c.show_speed()
    f.stop_police()
if a.type == 'SportCar':
    d = SportCar(40, 'Желтая', 'Лада', True, 'SportCar')
    d.show_speed()


'''
class Car:

    def __init__(self, speed, color, name, is_police):
        Car.speed = speed
        Car.color = color
        Car.name = name
        Car.is_police = is_police

    def go(self):
        return print(f'{Car.color} {Car.name} едет')

    def stop(self):
        return print(f'{Car.color} {Car.name} остановилась')

    def turn(self, direction):
        return print(f'{Car.color} {Car.name} повернула {direction}')

    def show_speed(self):
        return print(f'{Car.color} {Car.name} едет со скоростью {Car.speed} км/ч.')


class TownCar(Car):

    def show_speed(self):
        if Car.speed > 60:
            return print('Скорость превышена')
        else:
            return print(f'{Car.color} {Car.name} едет со скоростью {Car.speed} км/ч.')

class SportCar(Car):

    def show_speed(self):
        return print(f'{Car.color} {Car.name} едет со скоростью {Car.speed} км/ч.')


class WorkCar(Car):

    def show_speed(self):
        if Car.speed > 40:
            return print('Скорость превышена')
        else:
            return print(f'{Car.color} {Car.name} едет со скоростью {Car.speed} км/ч.')


class PoliceCar(Car):

    def show_speed(self):
        return print(f'{Car.color} {Car.name} едет со скоростью {Car.speed} км/ч.')


a = Car(40, 'Желтая', 'Лада', True)
b = TownCar(40, 'Желтая', 'Лада', True)
c = WorkCar(40, 'Желтая', 'Лада', True)
d = SportCar(40, 'Желтая', 'Лада', True)
f = PoliceCar(40, 'Желтая', 'Лада', True)

a.go()
a.turn('налево')
b.show_speed()
a.stop()
'''





