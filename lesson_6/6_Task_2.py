#TODO - 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
# depth = 5 # initial coverage depth (in sm)
# mass_per_sq_m = 25 # initial mass per square meter (in kg)

class Road:

    def __init__(self, length, width):
        Road._length = length
        Road._width = width

    def m_asfalt(self, depth, mass_per_sq_m):
        #depth = int(input('Задайте толщину: '))
        #mass_per_sq_m = int(input('Задайте массу для 1ого кв.м.: '))
        mass_asfalt = Road._length * Road._width * depth * mass_per_sq_m
        print(f'Масса асфальта: {mass_asfalt} т.')


a = Road(3, 2)
a.m_asfalt(4, 6)
