#TODO - 2.Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cost(self):
        pass


class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def cost(self):
        cost_v = self.size/6.5 + 0.5
        return f'На пошив пальто {self.name} израсходовано {cost_v:.3} м. ткани'


class Suit(Clothes):

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def cost(self):
        cost_h = 2 * self.height + 0.3
        return f'На пошив кастюма {self.name} израсходовано {cost_h:.3} м. ткани'


b = Coat('Adidas', 4)
c = Suit('Nike', 5)
print(b.cost)
print(c.cost)

