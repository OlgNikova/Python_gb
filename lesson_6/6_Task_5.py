#TODO - 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        Stationery.title = title

    def draw(self):
        return print(f'Запуск отрисовки. Используется {Stationery.title}')


class Pen(Stationery):

    def draw(self):
        return print(f'Запуск отрисовки. Используется {Stationery.title}')


class Pencil(Stationery):

    def draw(self):
        return print(f'Запуск отрисовки. Используется {Stationery.title}')


class Handle(Stationery):

    def draw(self):
        return print(f'Запуск отрисовки. Используется {Stationery.title}')


b = Pen('Острая ручка')
c = Pencil('Красный карандаш')
d = Handle('Синий маркер')

b.draw()
